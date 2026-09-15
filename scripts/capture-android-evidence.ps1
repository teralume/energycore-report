[CmdletBinding()]
param(
    [ValidateSet('login', 'home', 'energy', 'devices')]
    [string]$Screen = 'login',
    [string]$Device = 'emulator-5554'
)
$ErrorActionPreference = 'Stop'
$adb = 'C:\Users\Asus\AppData\Local\Android\sdk\platform-tools\adb.exe'
$state = & $adb -s $Device get-state 2>$null
if ($LASTEXITCODE -ne 0 -or $state -ne 'device') {
    throw 'Abre Pixel_7 desde Android Studio > Device Manager antes de capturar.'
}
$focus = (& $adb -s $Device shell dumpsys activity activities) -join "`n"
if ($focus -notmatch '(?:mResumedActivity|topResumedActivity|ResumedActivity:)[^\r\n]*com\.teralume\.energycore_flutter') {
    throw 'EnergyCore debe estar abierta y visible. No se captura otra app ni la pantalla de inicio de Android.'
}
$outputDir = Join-Path (Split-Path -Parent $PSScriptRoot) 'assets\evidence\implemented'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$name = "android-live-$Screen-$stamp.png"
$remote = "/sdcard/Pictures/$name"
$local = Join-Path $outputDir $name
& $adb -s $Device shell screencap -p $remote
if ($LASTEXITCODE -ne 0) { throw 'Android no pudo capturar la pantalla.' }
& $adb -s $Device pull $remote $local
if ($LASTEXITCODE -ne 0) { throw 'No se pudo recuperar la captura del emulador.' }
Write-Host "Captura real guardada: $local"
Write-Host 'Revisar legibilidad, contenido y ausencia de credenciales antes de incorporarla al informe.'
Get-FileHash -LiteralPath $local -Algorithm SHA256 | Select-Object Hash, Path
