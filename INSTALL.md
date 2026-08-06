# Installation

## Quick Start

```powershell
git clone https://github.com/sandraschi/ai-producer-hub
cd ai-producer-hub
uv sync
```

## Run the MCP Server (MIDI tools)

```powershell
uv run -m ai_producer_hub
```

## Run the Webapp

```powershell
cd webapp
npm install
npx vite --port 10707 --host
```

Or via just:
```powershell
just run     # MCP server (stdio)
just dev     # Webapp frontend
```

## Requirements

The orchestration tools require the audio fleet servers running:

| Server | Port | Install |
|--------|------|---------|
| songgeneration-mcp | 10885 | `D:\Dev\repos\songgeneration-mcp` |
| virtualdj-mcp | 10877 | `D:\Dev\repos\virtualdj-mcp` |

These are called via HTTP API — they can run on any machine reachable on the network.

## Tauri Desktop Build

```powershell
just build-native
just cua-nsis-test
```

See `native/build.ps1` for the full pipeline (webapp → PyInstaller → Tauri → NSIS).
