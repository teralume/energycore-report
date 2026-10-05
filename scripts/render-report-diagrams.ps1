param(
    [Parameter(Mandatory = $false)]
    [string]$PlantUmlExecutable = "plantuml"
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$sourceDirectories = @(
    (Join-Path $repoRoot "assets\architecture\source"),
    (Join-Path $repoRoot "assets\diagrams\source")
)

foreach ($sourceDirectory in $sourceDirectories) {
    if (-not (Test-Path -LiteralPath $sourceDirectory -PathType Container)) {
        throw "Diagram source directory not found: $sourceDirectory"
    }

    $sources = Get-ChildItem -LiteralPath $sourceDirectory -Filter "*.puml" -File
    if ($sources.Count -eq 0) {
        throw "No PlantUML sources found in: $sourceDirectory"
    }

    & $PlantUmlExecutable -tsvg -charset UTF-8 -o ".." (Join-Path $sourceDirectory "*.puml")
    if ($LASTEXITCODE -ne 0) {
        throw "PlantUML failed for: $sourceDirectory"
    }
}

Write-Output "Rendered PlantUML diagrams under assets/architecture and assets/diagrams."
