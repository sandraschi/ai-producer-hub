set windows-shell := ["powershell.exe", "-NoProfile", "-Command"]
set shell := ["powershell.exe", "-NoProfile", "-Command"]

default:
    @just --list

# Start the MCP server (stdio)
run:
    uv run -m ai_producer_hub

# Start frontend webapp
dev:
    cd webapp; npx vite --port 10707 --host

# START: Standard startup
start:
    powershell.exe -NoProfile -ExecutionPolicy Bypass -File ./start.ps1

lint:
    uv run ruff check src/

fix:
    uv run ruff check --fix src/
    uv run ruff format src/

test:
    uv run pytest

# Bootstrap: install dev deps + pre-commit hook
bootstrap:
    uv sync --group dev
    uv run pre-commit install
    Write-Host "Pre-commit hooks installed." -ForegroundColor Green

# CUA smoke test with detailed report to reports and mcd
cua-nsis-test:
	uv run python scripts/cua-smoke.py --output-dir cua-reports
	$date = Get-Date -Format "yyyy-MM-dd"; $md = "reports/cua-ai-producer-$date.md"; if (Test-Path $md) { Copy-Item $md "D:/Dev/repos/mcp-central-docs/reports/" -Force; Write-Host "Synced $md to mcd" }

cua-webapp-test:
	uv run python scripts/cua-webapp-test.py --output-dir cua-reports
	$date = Get-Date -Format "yyyy-MM-dd"; $md = "reports/cua-ai-producer-$date.md"; if (Test-Path $md) { Copy-Item $md "D:/Dev/repos/mcp-central-docs/reports/" -Force; Write-Host "Synced $md to mcd" }

build-native:
	$env:Path = "$env:USERPROFILE\.cargo\bin;$env:Path"; Set-Location "{{justfile_directory()}}/src-tauri"; powershell -NoProfile -ExecutionPolicy Bypass -File "src-tauri/build.ps1"
