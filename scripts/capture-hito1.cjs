const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');

const outputDir = path.resolve(__dirname, '..', 'assets', 'evidence', 'implemented');
fs.mkdirSync(outputDir, { recursive: true });

const now = new Date();
const isoNow = now.toISOString();
const today = isoNow.slice(0, 10);
const user = {
  id: 1,
  fullName: 'Jean Franck Loa Rojas',
  email: 'loarojas1@gmail.com',
  accessProfileId: 1,
  accessProfileName: 'OWNER',
  status: 'ACTIVE',
  createdAt: isoNow,
};
const subscription = {
  id: 1,
  userId: 1,
  planCode: 'PROFESSIONAL',
  status: 'ACTIVE',
  active: true,
  startDate: today,
  nextBillingDate: `${now.getFullYear()}-${String(now.getMonth() + 2).padStart(2, '0')}-01`,
  endDate: null,
};
const locations = [
  { id: 1, userId: 1, name: 'Campus inteligente', address: 'Monterrico, Lima', type: 'BUSINESS', createdAt: isoNow },
];
const rooms = [
  { id: 1, userId: 1, locationId: 1, name: 'Laboratorio de software', floor: '7', createdAt: isoNow },
  { id: 2, userId: 1, locationId: 1, name: 'Zona colaborativa', floor: '7', createdAt: isoNow },
];
const assignments = [
  { id: 1, userId: 1, deviceId: 1, locationId: 1, roomId: 1, assignedAt: isoNow },
  { id: 2, userId: 1, deviceId: 2, locationId: 1, roomId: 2, assignedAt: isoNow },
  { id: 3, userId: 1, deviceId: 3, locationId: 1, roomId: 1, assignedAt: isoNow },
];
const readings = Array.from({ length: 12 }, (_, index) => {
  const deviceId = (index % 3) + 1;
  const watts = [420, 155, 890][deviceId - 1] + index * 7;
  const recordedAt = new Date(now.getTime() - (11 - index) * 15 * 60 * 1000).toISOString();
  return {
    id: index + 1,
    userId: 1,
    deviceId,
    deviceName: ['Climatizacion central', 'Iluminacion colaborativa', 'Estacion de prototipado'][deviceId - 1],
    watts,
    kilowattHours: Number((watts * 0.25 / 1000).toFixed(4)),
    estimatedCost: Number((watts * 0.25 / 1000 * 0.78).toFixed(4)),
    sampleSeconds: 900,
    recordedAt,
    status: watts > 850 ? 'HIGH' : 'NORMAL',
  };
});
const summary = {
  currentWatts: 1465,
  todayKilowattHours: 9.84,
  todayEstimatedCost: 7.68,
  projectedMonthlyCost: 230.4,
  costPerHour: 1.14,
  peakWatts: 967,
  averageWatts: 512,
  activeDevices: 3,
  monitoredDevices: 3,
  normalReadings: 9,
  highReadings: 3,
  efficiencyScore: 86,
  operationalStatus: 'ATTENTION',
  recommendation: 'Revisa la estacion de prototipado: concentra el pico del periodo.',
  activeAlerts: 1,
  criticalAlerts: 0,
  latestAlertLevel: 'HIGH',
  latestAlertTitle: 'Pico controlable detectado',
  trend: [],
  topDevices: [],
  rooms: [],
  activeDeviceDetails: [
    { deviceId: 1, name: 'Climatizacion central', room: 'Laboratorio de software', type: 'OTHER', watts: 420, costPerHour: 0.33 },
    { deviceId: 2, name: 'Iluminacion colaborativa', room: 'Zona colaborativa', type: 'LIGHT', watts: 155, costPerHour: 0.12 },
    { deviceId: 3, name: 'Estacion de prototipado', room: 'Laboratorio de software', type: 'PLUG', watts: 890, costPerHour: 0.69 },
  ],
};

function json(route, body, status = 200) {
  return route.fulfill({ status, contentType: 'application/json', body: JSON.stringify(body) });
}

async function mockApi(page) {
  await page.route('https://energycore-platform-vfvqevfzvq-ue.a.run.app/api/v1/**', async (route) => {
    const url = new URL(route.request().url());
    const endpoint = url.pathname.replace('/api/v1/', '');

    if (endpoint === 'auth/me') return json(route, user);
    if (endpoint === 'auth/sign-in') return json(route, { user, token: 'energycore-evidence-token' });
    if (endpoint === 'billing/subscriptions/current') return json(route, subscription);
    if (endpoint === 'workplace/locations') return json(route, locations);
    if (endpoint.startsWith('workplace/rooms')) return json(route, rooms);
    if (endpoint.startsWith('workplace/device-assignments')) return json(route, assignments);
    if (endpoint === 'energy-readings/dashboard-summary') return json(route, summary);
    if (endpoint === 'energy-readings/sampling-settings') return json(route, { sampleSeconds: 15 });
    if (endpoint.startsWith('energy-readings')) return json(route, readings);
    if (endpoint === 'users/me/ui-preferences') {
      return json(route, { theme: 'SYSTEM', language: 'ES', notificationsEnabled: true });
    }
    return json(route, []);
  });
}

async function captureLocator(page, selector, fileName) {
  const locator = page.locator(selector).first();
  await locator.waitFor({ state: 'visible', timeout: 20000 });
  await locator.screenshot({ path: path.join(outputDir, fileName), animations: 'disabled' });
}

(async () => {
  const browser = await chromium.launch({ headless: true });

  const desktop = await browser.newContext({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
  const landing = await desktop.newPage();
  await landing.goto('http://127.0.0.1:4173', { waitUntil: 'networkidle' });
  await landing.emulateMedia({ reducedMotion: 'reduce' });
  await captureLocator(landing, '.hero', 'landing-desktop.png');
  await captureLocator(landing, '#pricing', 'landing-plans.png');

  const login = await desktop.newPage();
  await mockApi(login);
  await login.goto('http://127.0.0.1:4300/iam/login', { waitUntil: 'networkidle' });
  await captureLocator(login, '.auth-card', 'webapp-login.png');

  const authenticated = await desktop.newPage();
  await mockApi(authenticated);
  await authenticated.addInitScript(({ userData }) => {
    localStorage.setItem('energycore_auth_session', JSON.stringify({
      id: userData.id,
      fullName: userData.fullName,
      email: userData.email,
      token: 'energycore-evidence-token',
      accessProfileId: userData.accessProfileId,
      accessProfileName: userData.accessProfileName,
      lastActivityAt: Date.now(),
    }));
    localStorage.setItem('energycore_language', 'es');
    localStorage.setItem('energycore_theme', 'dark');
  }, { userData: user });
  await authenticated.goto('http://127.0.0.1:4300/energy/consumption', { waitUntil: 'networkidle' });
  await captureLocator(authenticated, '.energy-dashboard-page', 'webapp-energy-dashboard.png');

  const mobile = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1 });
  const mobileLanding = await mobile.newPage();
  await mobileLanding.goto('http://127.0.0.1:4173', { waitUntil: 'networkidle' });
  await mobileLanding.emulateMedia({ reducedMotion: 'reduce' });
  await captureLocator(mobileLanding, '.hero', 'landing-mobile.png');

  const mobileLogin = await mobile.newPage();
  await mockApi(mobileLogin);
  await mobileLogin.goto('http://127.0.0.1:4300/iam/login', { waitUntil: 'networkidle' });
  await captureLocator(mobileLogin, '.auth-card', 'webapp-login-mobile.png');

  await desktop.close();
  await mobile.close();
  await browser.close();
  process.stdout.write(`Captured ${fs.readdirSync(outputDir).filter((name) => name.endsWith('.png')).length} images in ${outputDir}\n`);
})().catch((error) => {
  console.error(error);
  process.exit(1);
});
