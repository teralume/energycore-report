[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$courseRoot = Split-Path $repoRoot -Parent
$mobileRoot = Join-Path $courseRoot 'energycore-mobile\flutter'
$platformRoot = Join-Path $courseRoot 'energycore-platform'
$interviewRoot = Join-Path $courseRoot 'Entrevistas'
$outputDirectory = Join-Path $repoRoot 'output\zip'
$outputFile = Join-Path $outputDirectory 'upc-pre-202610-1asi0732-9100-teralume-artifacts-av1.zip'
$tempRoot = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath()).TrimEnd('\')
$staging = Join-Path $tempRoot ("energycore-av1-artifacts-{0}" -f [guid]::NewGuid().ToString('N'))

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

try {
    New-Item -ItemType Directory -Force -Path $staging | Out-Null
    $resolvedStaging = (Resolve-Path -LiteralPath $staging).Path
    if (-not $resolvedStaging.StartsWith($tempRoot + '\', [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Unsafe staging directory: $resolvedStaging"
    }

    Copy-RequiredFile (Join-Path $repoRoot 'README.md') (Join-Path $staging 'report\README.md')
    Copy-RequiredFile (Join-Path $repoRoot 'delivery\av1-artifact-manifest.md') (Join-Path $staging 'MANIFEST.md')
    Copy-RequiredFile (Join-Path $repoRoot 'delivery\av1-closure-status.md') (Join-Path $staging 'delivery\av1-closure-status.md')

    foreach ($folder in @('assets\design', 'assets\evidence\implemented', 'assets\evidence\interviews')) {
        $sourceFolder = Join-Path $repoRoot $folder
        $destinationFolder = Join-Path $staging $folder
        New-Item -ItemType Directory -Force -Path $destinationFolder | Out-Null
        Copy-Item -Path (Join-Path $sourceFolder '*') -Destination $destinationFolder -Recurse -Force
    }

    $presentationDestination = Join-Path $staging 'presentation'
    New-Item -ItemType Directory -Force -Path $presentationDestination | Out-Null
    Copy-Item -Path (Join-Path $repoRoot 'presentation\*.md') -Destination $presentationDestination -Force

    Copy-RequiredFile `
        (Join-Path $repoRoot 'output\docx\upc-pre-202610-1asi0732-9100-teralume-performance-av1.docx') `
        (Join-Path $staging 'performance\upc-pre-202610-1asi0732-9100-teralume-performance-av1.docx')
    Copy-RequiredFile `
        (Join-Path $repoRoot 'output\pdf\upc-pre-202610-1asi0732-9100-teralume-performance-av1.pdf') `
        (Join-Path $staging 'performance\upc-pre-202610-1asi0732-9100-teralume-performance-av1.pdf')
    Copy-RequiredFile `
        (Join-Path $interviewRoot 'Entrevista 1.mp4') `
        (Join-Path $staging 'interviews\Entrevista 1.mp4')
    Copy-RequiredFile `
        (Join-Path $platformRoot 'scripts\deployment-result.local.json') `
        (Join-Path $staging 'deployment\deployment-result.local.json')
    Copy-RequiredFile `
        (Join-Path $mobileRoot 'build\app\outputs\flutter-apk\app-release.apk') `
        (Join-Path $staging 'mobile\app-release.apk')
    Copy-RequiredFile `
        (Join-Path $mobileRoot 'build\app\outputs\flutter-apk\app-release.apk.sha1') `
        (Join-Path $staging 'mobile\app-release.apk.sha1')

    $checksumLines = Get-ChildItem -LiteralPath $staging -Recurse -File |
        Sort-Object FullName |
        ForEach-Object {
            $relative = [System.IO.Path]::GetRelativePath($staging, $_.FullName).Replace('\', '/')
            $hash = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLowerInvariant()
            "$hash  $relative"
        }
    Set-Content -LiteralPath (Join-Path $staging 'SHA256SUMS.txt') -Value $checksumLines -Encoding utf8

    New-Item -ItemType Directory -Force -Path $outputDirectory | Out-Null
    Compress-Archive -Path (Join-Path $staging '*') -DestinationPath $outputFile -CompressionLevel Optimal -Force
    Write-Host "AV1 artifact package created: $outputFile" -ForegroundColor Green
}
finally {
    if (Test-Path -LiteralPath $staging) {
        $resolvedStaging = (Resolve-Path -LiteralPath $staging).Path
        if ($resolvedStaging.StartsWith($tempRoot + '\', [System.StringComparison]::OrdinalIgnoreCase)) {
            Remove-Item -LiteralPath $resolvedStaging -Recurse -Force
        }
    }
}
