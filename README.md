# AI Producer Hub

Fleet orchestration MCP server for the audio production stack. Generates songs via SongGeneration LeVo, loads them to VirtualDJ decks, produces multi-track albums, and sets up live streaming.

## Quick Start

```powershell
git clone https://github.com/sandraschi/ai-producer-hub
cd ai-producer-hub
uv sync
uv run -m ai_producer_hub    # MCP server (MIDI tools)
```

Webapp: `cd webapp && npm install && npx vite --port 10707`

## Tools

| Tool | What it does |
|------|-------------|
| `songgen_to_deck(lyrics, genre, tempo, deck_id)` | Generate song via LeVo → load to VDJ deck |
| `ai_dj_set(theme, num_tracks, bpm)` | Generate multi-track DJ set across decks |
| `album_factory(theme, num_tracks)` | Multi-track album, optionally to Plex |
| `live_stream_producer(theme, duration)` | Set up streaming with AI-generated music |
| `ai_mashup(track_a, track_b)` | Mashup plan from VDJ library search |
| `hub_status()` | Check all fleet server health |
| `list_midi_devices()` | Enumerate MIDI hardware |
| `record_midi_performance(device, duration)` | Record MIDI to file |

## Architecture

```
AI Producer Hub (MCP stdio)
  ├──→ songgeneration-mcp (HTTP :10885) — LeVo AI generation
  ├──→ virtualdj-mcp (HTTP :10877) — DJ decks, stems, mixing
  ├──→ reaper-mcp (HTTP :10797) — DAW mastering
  └──→ obs-mcp (HTTP :10819) — Live streaming
```

Sub-servers can run on any reachable host. Configure via `SONGGEN_BASE`, `VDJ_BASE`, `REAPER_BASE`, `OBS_BASE` env vars.

## Requirements

- Python 3.11+
- Running sub-servers (songgeneration-mcp, virtualdj-mcp) for orchestration tools
- `python-rtmidi` + `mido` for MIDI tools
