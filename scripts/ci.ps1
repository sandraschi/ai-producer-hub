$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot\..
uv sync --extra dev --extra ai
uv run ruff check src tests
uv run ruff format --check src tests
uv run pytest -q --tb=short
exit $LASTEXITCODE
