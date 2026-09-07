const http = require('node:http');

const now = new Date();
const isoNow = now.toISOString();
const today = isoNow.slice(0, 10);
const user = { id: 1, fullName: 'Jean Franck Loa Rojas', email: 'loarojas1@gmail.com', accessProfileId: 1, accessProfileName: 'OWNER', status: 'ACTIVE', createdAt: isoNow };
const locations = [{ id: 1, userId: 1, name: 'Campus inteligente', address: 'Monterrico, Lima', type: 'BUSINESS', createdAt: isoNow }];
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
  return {
    id: index + 1,
    userId: 1,
    deviceId,
    deviceName: ['Climatización central', 'Iluminación colaborativa', 'Estación de prototipado'][deviceId - 1],
    watts,
    kilowattHours: Number((watts * 0.25 / 1000).toFixed(4)),
    estimatedCost: Number((watts * 0.25 / 1000 * 0.78).toFixed(4)),
    sampleSeconds: 900,
    recordedAt: new Date(now.getTime() - (11 - index) * 15 * 60 * 1000).toISOString(),
    status: watts > 850 ? 'HIGH' : 'NORMAL',
  };
});
const summary = {
  currentWatts: 1465, todayKilowattHours: 9.84, todayEstimatedCost: 7.68,
  projectedMonthlyCost: 230.4, costPerHour: 1.14, peakWatts: 967, averageWatts: 512,
  activeDevices: 3, monitoredDevices: 3, normalReadings: 9, highReadings: 3,
  efficiencyScore: 86, operationalStatus: 'ATTENTION',
  recommendation: 'Revisa la estación de prototipado: concentra el pico del periodo.',
  activeAlerts: 1, criticalAlerts: 0, latestAlertLevel: 'HIGH', latestAlertTitle: 'Pico controlable detectado',
  trend: [], topDevices: [], rooms: [],
  activeDeviceDetails: [
    { deviceId: 1, name: 'Climatización central', room: 'Laboratorio de software', type: 'OTHER', watts: 420, costPerHour: 0.33 },
    { deviceId: 2, name: 'Iluminación colaborativa', room: 'Zona colaborativa', type: 'LIGHT', watts: 155, costPerHour: 0.12 },
    { deviceId: 3, name: 'Estación de prototipado', room: 'Laboratorio de software', type: 'PLUG', watts: 890, costPerHour: 0.69 },
  ],
};

function payloadFor(request) {
  const endpoint = new URL(request.url, 'http://127.0.0.1:4500').pathname.replace('/api/v1/', '');
  if (endpoint === 'auth/me') return user;
  if (endpoint === 'auth/sign-in') return { user, token: 'energycore-evidence-token' };
  if (endpoint === 'billing/subscriptions/current') return { id: 1, userId: 1, planCode: 'PROFESSIONAL', status: 'ACTIVE', active: true, startDate: today, nextBillingDate: today, endDate: null };
  if (endpoint === 'workplace/locations') return locations;
  if (endpoint.startsWith('workplace/rooms')) return rooms;
  if (endpoint.startsWith('workplace/device-assignments')) return assignments;
  if (endpoint === 'energy-readings/dashboard-summary') return summary;
  if (endpoint === 'energy-readings/sampling-settings') return { sampleSeconds: 15 };
  if (endpoint.startsWith('energy-readings')) return readings;
  if (endpoint === 'users/me/ui-preferences') return { theme: 'DARK', language: 'ES', notificationsEnabled: true };
  return [];
}

http.createServer((request, response) => {
  process.stdout.write(`${request.method} ${request.url}\n`);
  const headers = {
    'Access-Control-Allow-Headers': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Private-Network': 'true',
    'Content-Type': 'application/json; charset=utf-8',
  };
  if (request.method === 'OPTIONS') {
    response.writeHead(204, headers).end();
    return;
  }
  response.writeHead(200, headers).end(JSON.stringify(payloadFor(request)));
}).listen(4500, '127.0.0.1', () => process.stdout.write('Evidence API ready at http://127.0.0.1:4500/api/v1\n'));
