# Backup script for ai-producer-hub
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupDir = "D:\Backups\mcp-repos\ai-producer-hub"
$backupPath = "$backupDir\ai-producer-hub_$timestamp"

if (-not (Test-Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir -Force
}

Copy-Item -Path "." -Destination $backupPath -Recurse -Exclude @(".venv", "__pycache__", "*.egg-info", ".git")
Write-Host "Backup created at: $backupPath"

