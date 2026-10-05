[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$courseRoot = Split-Path $repoRoot -Parent
$mobileRoot = Join-Path $courseRoot 'energycore-mobile\flutter'
$platformRoot = Join-Path $courseRoot 'energycore-platform'
$outputDirectory = Join-Path $repoRoot 'output\zip'
$outputFile = Join-Path $outputDirectory 'upc-pre-202610-1asi0732-9100-teralume-artifacts-tb1.zip'
$deliveryDirectory = Join-Path $courseRoot 'Entregables\TB1'
$av1Video = Join-Path $courseRoot 'Entregables\AV1\upc-pre-202610-1asi0732-9100-teralume-expo-av1.mp4'
$aboutVideo = Join-Path $courseRoot 'About the product\upc-pre-202610-1asi0732-9100-teralume-about-the-product-sprint-1.mp4'
$tempRoot = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath()).TrimEnd('\')
$staging = Join-Path $tempRoot ("energycore-tb1-artifacts-{0}" -f [guid]::NewGuid().ToString('N'))

function Copy-RequiredFile {
    param(
        [Parameter(Mandatory)] [string] $Source,
        [Parameter(Mandatory)] [string] $Destination
    )

    if (-not (Test-Path -LiteralPath $Source -PathType Leaf)) {
        throw "Required artifact not found: $Source"
    }
    $parent = Split-Path $Destination -Parent
    New-Item -ItemType Directory -Force -Path $parent | Out-Null
    Copy-Item -LiteralPath $Source -Destination $Destination -Force
}

function Get-Sha256Hex {
    param([Parameter(Mandatory)] [string] $Path)
    $stream = [System.IO.File]::OpenRead($Path)
    try {
        $sha = [System.Security.Cryptography.SHA256]::Create()
        try {
            return ([System.BitConverter]::ToString($sha.ComputeHash($stream))).Replace('-', '').ToLowerInvariant()
        }
        finally {
            $sha.Dispose()
        }
    }
    finally {
        $stream.Dispose()
    }
}

try {
    New-Item -ItemType Directory -Force -Path $staging | Out-Null
    $resolvedStaging = (Resolve-Path -LiteralPath $staging).Path
    if (-not $resolvedStaging.StartsWith($tempRoot + '\', [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Unsafe staging directory: $resolvedStaging"
    }

    Copy-RequiredFile (Join-Path $repoRoot 'README.md') (Join-Path $staging 'report\README.md')
    Copy-RequiredFile (Join-Path $repoRoot 'presentation\test-demo-guide-tb1.md') (Join-Path $staging 'presentation\test-demo-guide-tb1.md')
    Copy-RequiredFile (Join-Path $platformRoot 'scripts\deployment-result.local.json') (Join-Path $staging 'deployment\deployment-result.local.json')
    Copy-RequiredFile (Join-Path $repoRoot 'assets\evidence\implemented\openapi-live.json') (Join-Path $staging 'evidence\openapi-live.json')
    Copy-RequiredFile (Join-Path $repoRoot 'assets\evidence\implemented\energy-power-smoke.json') (Join-Path $staging 'evidence\energy-power-smoke.json')
    Copy-RequiredFile (Join-Path $repoRoot 'assets\evidence\implemented\preferences-concurrency-smoke.json') (Join-Path $staging 'evidence\preferences-concurrency-smoke.json')
    Copy-RequiredFile (Join-Path $mobileRoot 'build\app\outputs\flutter-apk\app-release.apk') (Join-Path $staging 'mobile\app-release.apk')
    Copy-RequiredFile (Join-Path $mobileRoot 'build\app\outputs\flutter-apk\app-release.apk.sha1') (Join-Path $staging 'mobile\app-release.apk.sha1')

    $manifest = @(
        '# EnergyCore TB1 - archivos complementarios',
        '',
        'Este paquete conserva evidencia técnica verificable de la entrega acumulativa:',
        '',
        '- fuente Markdown del Project Report;',
        '- resultado del despliegue de Cloud Run sin credenciales;',
        '- contrato OpenAPI recuperado del servicio;',
        '- resultados JSON de smoke tests de energía, potencia y concurrencia;',
        '- APK release de Android y su checksum SHA-1.',
        '',
        'La exposición reutilizada de AV1 se entrega como archivo MP4 separado. El About-the-Product permanece publicado en YouTube y Microsoft Stream, con sus enlaces dentro del informe.'
    )
    Set-Content -LiteralPath (Join-Path $staging 'MANIFEST.md') -Value $manifest -Encoding utf8

    $checksumLines = Get-ChildItem -LiteralPath $staging -Recurse -File |
        Sort-Object FullName |
        ForEach-Object {
            $relative = $_.FullName.Substring($staging.Length).TrimStart('\').Replace('\', '/')
            $hash = Get-Sha256Hex -Path $_.FullName
            "$hash  $relative"
        }
    Set-Content -LiteralPath (Join-Path $staging 'SHA256SUMS.txt') -Value $checksumLines -Encoding utf8

    New-Item -ItemType Directory -Force -Path $outputDirectory | Out-Null
    Compress-Archive -Path (Join-Path $staging '*') -DestinationPath $outputFile -CompressionLevel Optimal -Force

    New-Item -ItemType Directory -Force -Path $deliveryDirectory | Out-Null
    $deliveryFiles = @(
        @{ Source = (Join-Path $repoRoot 'output\pdf\upc-pre-202610-1asi0732-9100-teralume-report-tb1.pdf'); Name = 'upc-pre-202610-1asi0732-9100-teralume-report-tb1.pdf' },
        @{ Source = (Join-Path $repoRoot 'output\keynote\upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pptx'); Name = 'upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pptx' },
        @{ Source = (Join-Path $repoRoot 'output\keynote\upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pdf'); Name = 'upc-pre-202610-1asi0732-9100-teralume-keynote-tb1.pdf' },
        @{ Source = (Join-Path $repoRoot 'output\docx\upc-pre-202610-1asi0732-9100-teralume-performance-tb1.docx'); Name = 'upc-pre-202610-1asi0732-9100-teralume-performance-tb1.docx' },
        @{ Source = (Join-Path $repoRoot 'output\pdf\upc-pre-202610-1asi0732-9100-teralume-performance-tb1.pdf'); Name = 'upc-pre-202610-1asi0732-9100-teralume-performance-tb1.pdf' },
        @{ Source = $outputFile; Name = 'upc-pre-202610-1asi0732-9100-teralume-artifacts-tb1.zip' },
        @{ Source = $av1Video; Name = 'upc-pre-202610-1asi0732-9100-teralume-expo-tb1.mp4' }
    )
    $legacyAbout = Join-Path $deliveryDirectory 'upc-pre-202610-1asi0732-9100-teralume-about-the-product-sprint-1.mp4'
    if (Test-Path -LiteralPath $legacyAbout -PathType Leaf) {
        Remove-Item -LiteralPath $legacyAbout -Force
    }
    $currentAbout = Join-Path $deliveryDirectory 'upc-pre-202610-1asi0732-9100-teralume-about-the-product-sprint-2.mp4'
    if (Test-Path -LiteralPath $currentAbout -PathType Leaf) {
        Remove-Item -LiteralPath $currentAbout -Force
    }
    foreach ($file in $deliveryFiles) {
        Copy-RequiredFile $file.Source (Join-Path $deliveryDirectory $file.Name)
    }

    Write-Host "TB1 artifact package created: $outputFile" -ForegroundColor Green
    Write-Host "TB1 delivery folder ready: $deliveryDirectory" -ForegroundColor Green
}
finally {
    if (Test-Path -LiteralPath $staging) {
        $resolvedStaging = (Resolve-Path -LiteralPath $staging).Path
        if ($resolvedStaging.StartsWith($tempRoot + '\', [System.StringComparison]::OrdinalIgnoreCase)) {
            Remove-Item -LiteralPath $resolvedStaging -Recurse -Force
        }
    }
}
