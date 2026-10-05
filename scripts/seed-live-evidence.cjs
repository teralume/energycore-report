// Demo fixtures persisted through the real API, NOT intercepted HTTP responses.
// Only for the isolated local evidence database; never target a deployed service.
const fs = require('node:fs');
const path = require('node:path');
if (!process.argv.includes('--isolated-local-demo')) {
  throw new Error('Requiere --isolated-local-demo y Spring Boot conectado a la base aislada energycore_evidence en 55432, sin credenciales Stripe. Nunca usar con la base habitual o producción.');
}
const base = 'http://127.0.0.1:8080/api/v1';
const account = {fullName:'EnergyCore Demo', email:'evidence@energycore.test', password:'LocalEvidence2026!'};
let token;
async function api(endpoint, method='GET', body) {
  const response = await fetch(base + endpoint, {method, headers:{'Content-Type':'application/json', ...(token ? {Authorization:'Bearer '+token}: {})}, body:body ? JSON.stringify(body):undefined});
  const text=await response.text();
  if(!response.ok) throw new Error(`${method} ${endpoint}: ${response.status} ${text}`);
  return text ? JSON.parse(text):null;
}
(async()=>{
  const openapi=await fetch('http://127.0.0.1:8080/v3/api-docs');
  if(!openapi.ok) throw new Error('OpenAPI is unavailable');
  const spec=await openapi.json();
  const out=path.resolve(__dirname,'../assets/evidence/implemented');
  fs.writeFileSync(path.join(out,'openapi-live.json'),JSON.stringify(spec,null,2)+'\n');
  try { await api('/auth/sign-up','POST',account); } catch(error) {
    if(!error.message.includes('already')) throw error;
  }
  const session=await api('/auth/sign-in','POST',account);
  token=session.token;
  if(!token) throw new Error('Sign-in did not return a token');
  const current=await api('/billing/subscriptions/current');
  if(!current || !current.active) {
    await api('/billing/subscriptions/checkout','POST',{planCode:'PROFESSIONAL',holderName:'LOCAL DEMO ONLY',cardNumber:'4242424242424242',expirationDate:'12/30',cvv:'123'});
  }
  let locations=await api('/workplace/locations');
  const location=locations[0] || await api('/workplace/locations','POST',{name:'Campus EnergyCore · Demo',address:'Entorno académico local',type:'BUSINESS'});
  let rooms=await api('/workplace/rooms');
  const room=rooms[0] || await api('/workplace/rooms','POST',{locationId:location.id,name:'Laboratorio de software',floor:'7'});
  let devices=await api('/devices');
  if(!devices.length) {
    for(const item of [{name:'Iluminación LED · Demo',type:'LIGHT',powerWatts:120},{name:'Estación de trabajo · Demo',type:'PLUG',powerWatts:350},{name:'Climatización · Demo',type:'OTHER',powerWatts:900}]) {
      const device=await api('/devices','POST',{...item,room:room.name});
      await api('/workplace/device-assignments','POST',{deviceId:device.id,roomId:room.id,locationId:location.id});
      await api(`/devices/${device.id}/toggle`,'PATCH');
    }
    devices=await api('/devices');
  }
  for(const device of devices) await api('/energy-readings','POST',{deviceId:device.id,deviceName:device.name,watts:device.powerWatts});
  const summary=await api('/energy-readings/dashboard-summary');
  console.log(JSON.stringify({mode:'REAL_API_LOCAL_POSTGRES_SYNTHETIC_FIXTURES',devices:devices.length,summary},null,2));
})().catch(error=>{console.error(error.message);process.exitCode=1;});
