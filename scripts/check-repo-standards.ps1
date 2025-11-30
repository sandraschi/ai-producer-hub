# Check repository standards for ai-producer-hub
$errors = @()

# Check required files
$requiredFiles = @("README.md", "LICENSE", "pyproject.toml", "manifest.json")
foreach ($file in $requiredFiles) {
    if (-not (Test-Path $file)) {
        $errors += "Missing: $file"
    }
}

# Check required directories
$requiredDirs = @("src", "tests", "scripts")
foreach ($dir in $requiredDirs) {
    if (-not (Test-Path $dir)) {
        $errors += "Missing directory: $dir"
    }
}

# Check for .cursorrules
if (-not (Test-Path ".cursorrules")) {
    $errors += "Missing: .cursorrules"
}

# Check for CI
if (-not (Test-Path ".github\workflows")) {
    $errors += "Missing: .github/workflows (CI)"
}

if ($errors.Count -eq 0) {
    Write-Host "All standards met!" -ForegroundColor Green
} else {
    Write-Host "Standards issues found:" -ForegroundColor Yellow
    $errors | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
}

