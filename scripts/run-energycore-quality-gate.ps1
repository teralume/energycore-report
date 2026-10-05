[CmdletBinding()]
param(
    [switch] $SkipBuilds,
    [switch] $IncludeStaticAnalysis
)

$ErrorActionPreference = 'Stop'

$reportRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$courseRoot = Split-Path $reportRoot -Parent
$platformRoot = Join-Path $courseRoot 'energycore-platform'
$webappRoot = Join-Path $courseRoot 'energycore-webapp'
$websiteRoot = Join-Path $courseRoot 'energycore-website'
$flutterRoot = Join-Path $courseRoot 'energycore-mobile\flutter'
$jbrRoot = Join-Path $env:ProgramFiles 'Android\Android Studio\jbr'

function Invoke-GateCommand {
    param(
        [Parameter(Mandatory)] [string] $Label,
        [Parameter(Mandatory)] [string] $WorkingDirectory,
        [Parameter(Mandatory)] [scriptblock] $Command
    )

    Write-Host "`n[$Label]" -ForegroundColor Cyan
    Push-Location $WorkingDirectory
    try {
        & $Command
        if ($LASTEXITCODE -ne 0) {
            throw "$Label failed with exit code $LASTEXITCODE."
        }
    }
    finally {
        Pop-Location
    }
}

if (-not (Test-Path -LiteralPath (Join-Path $jbrRoot 'bin\java.exe') -PathType Leaf)) {
    throw "Android Studio JBR was not found at $jbrRoot. Install Android Studio or set the script to a compatible JDK 17-25."
}

$previousJavaHome = $env:JAVA_HOME
$previousPath = $env:Path
$analysisDrive = 'Q:'

try {
    $env:JAVA_HOME = $jbrRoot
    $env:Path = (Join-Path $jbrRoot 'bin') + ';' + $previousPath

    Invoke-GateCommand 'Backend: 28 JUnit + 60 Cucumber' $platformRoot { & .\mvnw.cmd verify }
    Invoke-GateCommand 'Angular: 5 tests' $webappRoot { & npm run test:ci }
    Invoke-GateCommand 'Landing Page: 5 tests' $websiteRoot { & npm test }
    Invoke-GateCommand 'Flutter: 11 tests' $flutterRoot { & flutter test }

    if (-not $SkipBuilds) {
        Invoke-GateCommand 'Angular production build' $webappRoot { & npm run build }

        if ($IncludeStaticAnalysis) {
            # The temporary drive avoids non-ASCII characters in the LSP workspace path.
            & subst $analysisDrive $flutterRoot
            if ($LASTEXITCODE -ne 0) {
                throw "Could not create temporary drive $analysisDrive for Flutter analysis."
            }
            Invoke-GateCommand 'Flutter static analysis' "$analysisDrive\" { & flutter analyze --no-pub }
        }
    }

    if ($SkipBuilds) {
        Write-Host "`nPASS: 109 automated tests." -ForegroundColor Green
    }
    else {
        Write-Host "`nPASS: 109 automated tests, backend package and Angular production build." -ForegroundColor Green
    }
}
finally {
    if (Test-Path "$analysisDrive\") {
        & subst $analysisDrive /D | Out-Null
    }
    $env:JAVA_HOME = $previousJavaHome
    $env:Path = $previousPath
}
