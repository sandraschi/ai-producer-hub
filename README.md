# AI Producer Hub

A Model Context Protocol server that integrates AI-powered music generation with professional production tools, enabling autonomous music creation workflows from MIDI input to live streaming.

## Overview

The AI Producer Hub bridges traditional MIDI hardware with modern AI music generation, providing a complete production environment that combines:

- Real-time MIDI hardware integration
- AI-powered vocal and instrumental generation
- Professional mixing and mastering tools
- Automated DJ mixing and live streaming

## Architecture

## Components

The hub integrates multiple specialized MCP servers:

| Component | Mount Point | Tools | Description |
|-----------|-------------|-------|-------------|
| VirtualDJ-MCP | `/dj/*` | 61 | Professional DJ mixing, stem separation, video integration |
| Plex-MCP | `/plex/*` | 15 | Media library management and organization |
| SongGeneration-MCP | `/songgen/*` | 7 | AI-powered vocal and instrumental generation |
| Reaper-MCP | `/reaper/*` | 25 | Digital audio workstation and mastering |
| OBS-MCP | `/obs/*` | 20 | Live streaming and broadcasting |
| Local MIDI Tools | (root) | 8 | Hardware MIDI device integration |

## AI Integration

The hub includes advanced AI orchestration capabilities:

- **SEP-1577 Sampling**: Autonomous tool orchestration without client round-trips
- **Conversational AI**: Natural language production guidance
- **Autonomous Workflows**: Complete production pipelines managed by AI agents
- **Multi-Provider Support**: Integration with Anthropic Claude and OpenAI GPT models

## MIDI Integration

The hub provides comprehensive MIDI hardware integration with AI-enhanced processing:

### Basic MIDI Workflow

```python
# 1. Enumerate connected MIDI devices
list_midi_devices()
# Returns device information for inputs and outputs

# 2. Record MIDI performance
record_midi_performance(device_index=0, duration_seconds=30)
# Captures live performance to timestamped MIDI file

# 3. AI-assisted content generation
midi_to_ai_seed("recording.mid", expansion_style="full_production")
# Analyzes MIDI and generates structured content for AI processing

# 4. Generate complete track with AI vocals
songgen_to_deck(lyrics, genre="Electronic", tempo=128, deck=1)
# Produces professional vocal and instrumental tracks
```

### MIDI Tools

| Tool | Description |
|------|-------------|
| `list_midi_devices` | Enumerate connected MIDI hardware devices |
| `record_midi_performance` | Capture live MIDI performance to file |
| `send_midi_note` | Send MIDI notes to connected devices |
| `play_midi_file` | Play MIDI files through hardware outputs |
| `midi_monitor` | Monitor and debug MIDI data streams |
| `midi_to_reaper` | Import MIDI data to Reaper DAW |
| `midi_to_ai_seed` | Analyze MIDI for AI content generation |

## Workflows

### AI-Powered Production

#### Autonomous Track Generation
```python
# Generate complete track with AI orchestration
ai_produce_track(
    theme="cyberpunk neon city",
    genre="Electronic",
    bpm=128,
    voice_type="Male"
)
# AI manages: lyrics → vocals → stems → mixing → mastering → DJ integration
```

#### Conversational Production Guidance
```python
# Natural language production assistance
ai_collaborate_workflow(
    "Help me make this mix more energetic"
)
# AI provides contextual analysis and suggestions
```

#### Automated DJ Sets
```python
ai_dj_set("progressive house summer", num_tracks=6)
# Generates themed track collection with harmonic mixing analysis
```

### MIDI-to-Production Pipeline
```python
# 1. Record MIDI performance
record_midi_performance(0, 30)

# 2. AI content analysis and generation
midi_to_ai_seed("recording.mid", "full_production")

# 3. Complete track production
songgen_to_deck(lyrics, genre="Electronic", tempo=128, deck=1)
```

### Large-Scale Production
```python
# Album production with AI orchestration
ai_orchestrate_production(
    "Create a 10-track concept album about space exploration",
    available_tools=["songgen", "reaper", "plex"]
)
```

### Live Streaming
```python
# Automated streaming production
ai_stream_production(
    theme="ambient electronic",
    duration_hours=2,
    platform="twitch"
)
# AI manages continuous content generation and streaming setup
```

## Installation

### Requirements
- Python 3.11 or later
- MIDI hardware (optional, for hardware integration)
- Component MCP servers (VirtualDJ, Plex, SongGeneration, Reaper, OBS)

### Basic Installation
```bash
# Clone repository
git clone https://github.com/sandraschi/ai-producer-hub.git
cd ai-producer-hub

# Install with uv (recommended)
uv pip install -e .[dev,ai]

# Or with pip
pip install -e .[dev,ai]
```

### Component Servers
Install the required MCP server components:

```bash
# Install component servers (adjust paths as needed)
uv pip install -e /path/to/virtualdj-mcp
uv pip install -e /path/to/plex-mcp
uv pip install -e /path/to/songgeneration-mcp
uv pip install -e /path/to/reaper-mcp
uv pip install -e /path/to/obs-mcp
```

### MCP Server Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "ai-producer-hub": {
      "command": "python",
      "args": ["-m", "ai_producer_hub"],
      "cwd": "/path/to/ai-producer-hub"
    }
  }
}
```

### Optional Dependencies

For full AI functionality:
```bash
pip install ai-producer-hub[ai]
```

For development:
```bash
pip install ai-producer-hub[dev]
```

For documentation:
```bash
pip install ai-producer-hub[docs]
```

## Usage Examples

### Basic MIDI Workflow
```python
# 1. Check available MIDI devices
list_midi_devices()
# Returns: {'inputs': ['MPK mini 3'], 'outputs': ['Microsoft GS']}

# 2. Record a performance
record_midi_performance(device_index=0, duration_seconds=30)
# Saves MIDI file with timestamp

# 3. Generate AI-powered track
songgen_to_deck(
    lyrics="Electronic verse about digital dreams",
    genre="Electronic",
    tempo=128,
    deck=1
)
# Produces complete track with vocals and instrumentation
```

### Autonomous Production
```python
# AI-managed complete production pipeline
result = ai_produce_track(
    theme="cyberpunk city night",
    genre="Electronic",
    bpm=130,
    voice_type="Female"
)
# AI handles all aspects: analysis, generation, mixing, integration
```

### Large-Scale Projects
```python
# Automated album production
ai_orchestrate_production(
    "Create a 12-track electronic album about urban exploration",
    available_tools=["songgen", "reaper", "plex"]
)
# AI manages complete album workflow from concept to final product
```

### Conversational Assistance
```python
# Natural language production guidance
ai_collaborate_workflow(
    "The mix needs more energy in the drop sections"
)
# AI analyzes current state and provides specific recommendations
```

## Architecture

```
ai-producer-hub/
├── AI Integration Layer
│   ├── ai_integration.py      # SEP-1577 sampling + conversational AI
│   └── Autonomous workflows   # AI-managed production pipelines
│
├── Local MIDI Tools (8 tools)
│   ├── Device enumeration     # python-rtmidi + mido
│   ├── Performance capture    # Live recording and processing
│   ├── Hardware control       # MIDI I/O and monitoring
│   └── AI content analysis    # MIDI-to-content conversion
│
├── Component MCP Servers
│   ├── /dj/*      - VirtualDJ-MCP (61 tools) - Professional mixing
│   ├── /plex/*    - Plex-MCP (15 tools) - Media library management
│   ├── /songgen/* - SongGeneration-MCP (7 tools) - AI vocal/instrumental generation
│   ├── /reaper/*  - Reaper-MCP (25 tools) - DAW and mastering
│   └── /obs/*     - OBS-MCP (20 tools) - Live streaming
│
└── Cross-Server Orchestration
    ├── ai_produce_track()     - Autonomous track production
    ├── ai_orchestrate_production() - SEP-1577 sampling workflows
    ├── ai_collaborate_workflow() - Conversational AI assistance
    ├── ai_stream_production() - Automated live streaming
    └── ai_analyze_production() - AI-powered quality assessment
```

## Development

### Requirements
- Python 3.11+
- FastMCP 2.14.3+
- Component MCP servers (see Installation)

### Development Setup
```bash
# Install development dependencies
uv pip install -e .[dev,ai,docs]

# Run tests
pytest tests/ -v --cov=src

# Lint and format
ruff check . --fix
ruff format .

# Type checking
mypy src/
```

### Project Structure
- `src/ai_producer_hub/` - Main package
- `mcpb/` - MCPB packaging configuration
- `.zed/` - Zed editor integration
- `.github/workflows/` - CI/CD pipelines
- `tests/` - Test suite

## License

MIT License

## Contributing

Contributions are welcome. Please see the development documentation for guidelines.

## Related Projects

- [SongGeneration-MCP](https://github.com/sandraschi/songgeneration-mcp) - AI music generation
- [VirtualDJ-MCP](https://github.com/sandraschi/virtualdj-mcp) - Professional DJ mixing
- [Plex-MCP](https://github.com/sandraschi/plex-mcp) - Media library management

