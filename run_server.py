"""PyInstaller entry point — dual transport for Tauri/HTTP deployment.

Detects MCP_PORT env var (set by Tauri backend.rs) and starts uvicorn
when present, otherwise falls back to stdio for Claude Desktop.
"""

import os
import sys

port = os.environ.get("MCP_PORT") or os.environ.get("PORT")
if port:
    host = os.environ.get("MCP_HOST", "127.0.0.1")
    sys.argv = ["run_server.py", "--mode", "http", "--host", host, "--port", str(port)]

from ai_producer_hub.server import main

main()
