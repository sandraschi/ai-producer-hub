param([switch]$Headless, [switch]$NoBrowser)

$ErrorActionPreference = "Stop"
$FrontendPort = 10707
$BackendPort = 10885

# Port zombie clearing
Get-NetTCPConnection -LocalPort $FrontendPort -ErrorAction SilentlyContinue |
    ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
Get-NetTCPConnection -LocalPort $BackendPort -ErrorAction SilentlyContinue |
    ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }

$WindowStyle = if ($Headless) { 'Hidden' } else { 'Normal' }

Write-Host "Starting AI Producer Hub..." -ForegroundColor Cyan

Set-Location $PSScriptRoot
Write-Host "  MIDI tools (MCP stdio): uv run -m ai_producer_hub" -ForegroundColor Gray

# Start Vite frontend
$WebRoot = Join-Path $PSScriptRoot "webapp"
Start-Process -NoNewWindow -FilePath "npx" -ArgumentList "vite --port $FrontendPort --host" -WorkingDirectory $WebRoot

# Open browser
if (-not $NoBrowser) {
    Start-Sleep 2
    Start-Process "http://127.0.0.1:$FrontendPort"
}

Write-Host ""
Write-Host "  Webapp: http://127.0.0.1:$FrontendPort" -ForegroundColor Green
Write-Host "  For MIDI tools, also run: uv run -m ai_producer_hub" -ForegroundColor Yellow
