set windows-shell := ["powershell.exe", "-NoProfile", "-Command"]
set shell := ["powershell.exe", "-NoProfile", "-Command"]

default:
    @just --list

# Start the MCP server (stdio)
run:
    uv run -m ai_producer_hub

# Start frontend webapp
dev:
    cd webapp && npx vite --port 10707 --host

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

# Build Tauri NSIS installer
build-native:
    powershell.exe -NoProfile -File native/build.ps1

# CUA-NSIS smoke test
cua-nsis-test:
    uv run python scripts/cua-smoke.py

# Bootstrap: install dev deps + pre-commit hook
bootstrap:
    uv sync --group dev
    uv run pre-commit install
    Write-Host "Pre-commit hooks installed." -ForegroundColor Green

# Run CUA webapp test (pre-Tauri: start.ps1 stack + nav walk in browser)
cua-webapp-test:
    powershell.exe -NoProfile -File "{{justfile_directory()}}\scripts\just\cua-webapp-test.ps1"