$ErrorActionPreference = "Stop"

$Repo = "https://github.com/Mahesh-Revenueholic/internal-skills.git"
$Target = if ($args[0]) { $args[0] } else { "$env:USERPROFILE\.ai-skills" }
$Temp = Join-Path $env:TEMP "internal-skills-$(New-Guid)"

Write-Host "→ Cloning internal-skills..."
git clone --depth 1 $Repo $Temp 2>$null

Write-Host "→ Installing skills to $Target..."
New-Item -ItemType Directory -Path $Target -Force | Out-Null

$installed = 0

$files = @()
$files += Get-ChildItem -Path "$Temp\*.md" -File -ErrorAction SilentlyContinue
$files += Get-ChildItem -Path "$Temp\*.py" -File -ErrorAction SilentlyContinue

foreach ($file in $files) {
    Copy-Item $file.FullName -Destination $Target -Force
    Write-Host "  ✓ $($file.Name)"
    $installed++
}

Remove-Item -Path $Temp -Recurse -Force

Write-Host ""
Write-Host "✓ Installed $installed files to $Target"
Write-Host ""
Write-Host "Next: paste this in your AI tool:"
Write-Host "  Load skills from $Target and run the SEO blog pipeline."
