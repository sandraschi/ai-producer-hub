# AI Producer Hub

[![FastMCP Version](https://img.shields.io/badge/FastMCP-3.1.0-blue?style=flat-square&logo=python&logoColor=white)](https://github.com/sandraschi/fastmcp) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

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
```
User: "Create a complete electronic track about cyberpunk cities"

AI: "I'll orchestrate a full production pipeline for 'cyberpunk neon city' theme.

Starting autonomous workflow:
1. Analyzing theme and generating structured lyrics
2. Creating vocal performance with AI synthesis
3. Generating electronic backing tracks and stems
4. Mixing and mastering for professional sound
5. Loading final track to VirtualDJ deck

Progress: Lyrics generated → Vocals rendered → Stems produced → Mix complete → DJ integration finished

Track 'Neon Shadows' is ready on Deck 1. Would you like me to generate variations or start a new track?"
```

#### Conversational Production Guidance
```
User: "Help me make this mix more energetic"

AI: "I can analyze your current production and suggest improvements. Looking at the track structure...

Current analysis:
- BPM: 128, Energy level: Medium
- Frequency balance: Mids dominant, highs attenuated
- Dynamic range: Compressed, could use more punch

Suggestions:
1. Increase high-frequency EQ on percussion stems (+3dB at 8kHz)
2. Add sidechain compression on bass to create rhythmic pumping
3. Boost attack on kick drum samples for more impact
4. Layer in additional percussion elements for complexity

Would you like me to implement these changes automatically, or would you prefer to adjust specific elements?"
```

#### Large-Scale Production Orchestration
```
User: "I need a 12-track concept album about space exploration"

AI: "I'll orchestrate a complete album production using SEP-1577 sampling across all available tools.

Planning autonomous workflow:
- Album structure: 12 tracks with cohesive theme
- Parallel track generation using SongGeneration-MCP
- Consistent mastering across all tracks via Reaper-MCP
- Automated organization in Plex-MCP library
- Quality analysis and refinement iterations

Estimated completion: 45 minutes
Track list generated → Production pipeline started → Quality checks running

First track 'Launch Sequence' complete. Continuing with remaining tracks..."
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
```
User: "Produce a full album about space exploration"

AI: "I'll manage the complete album production workflow using autonomous orchestration.

Album Concept: 'Cosmic Journey' - 10 tracks exploring space themes

Workflow initiated:
- Generating track concepts and lyrics for each song
- Parallel production using SongGeneration LeVo AI
- Consistent mastering and mixing across all tracks
- Automatic organization into album structure
- Quality analysis and refinement

Status: Track 1/10 'Stellar Winds' → Complete
        Track 2/10 'Zero Gravity' → Rendering vocals...

Album completion: ~30 minutes remaining
Would you like me to adjust the production style or add specific elements?"
```

### Live Streaming
```
User: "Start a 2-hour ambient electronic stream on Twitch"

AI: "I'll set up autonomous live streaming with continuous AI-generated content.

Streaming Configuration:
- Theme: Ambient electronic atmospheres
- Duration: 2 hours (120 minutes)
- Platform: Twitch integration via OBS-MCP
- Content strategy: Progressive evolution with smooth transitions

Setup initiated:
- OBS streaming configuration established
- Initial track generation started (3 tracks pre-buffered)
- VirtualDJ automix sequence programmed
- Engagement monitoring activated

Stream Status: Pre-roll tracks loaded → Going live in 30 seconds
Content pipeline: Track generation every 12-15 minutes
Quality monitoring: Active with automatic adjustments

Stream is now live! I'll continue generating fresh content throughout."
```

## 🚀 Installation

### Prerequisites
- [uv](https://docs.astral.sh/uv/) installed (RECOMMENDED)
- Python 3.12+

### 📦 Quick Start
Run immediately via `uvx`:
```bash
uvx ai-producer-hub
```

### 🎯 Claude Desktop Integration
Add to your `claude_desktop_config.json`:
```json
"mcpServers": {
  "ai-producer-hub": {
    "command": "uv",
    "args": ["--directory", "D:/Dev/repos/ai-producer-hub", "run", "ai-producer-hub"]
  }
}
```
### Requirements
- Python 3.11 or later
- MIDI hardware (optional, for hardware integration)
- Component MCP servers (VirtualDJ, Plex, SongGeneration, Reaper, OBS)

## 🚀 Installation

### Prerequisites
- [uv](https://docs.astral.sh/uv/) installed (RECOMMENDED)
- Python 3.12+

### 📦 Quick Start
Run immediately via `uvx`:
```bash
uvx ai-producer-hub
```

### 🎯 Claude Desktop Integration
Add to your `claude_desktop_config.json`:
```json
"mcpServers": {
  "ai-producer-hub": {
    "command": "uv",
    "args": ["--directory", "D:/Dev/repos/ai-producer-hub", "run", "ai-producer-hub"]
  }
}
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
```
User: "Check my MIDI devices and record a 30-second performance"

AI: "Found MIDI devices: MPK mini 3 (input), Microsoft GS (output)

Starting 30-second recording... Play your performance now.

Recording complete! Saved as 'midi_performance_20241201_143022.mid'

Analyzing MIDI content for AI processing..."
```

### Autonomous Production
```
User: "Create a complete electronic track about cyberpunk cities"

AI: "Initiating autonomous production pipeline for 'cyberpunk city night' theme.

Production stages:
1. Theme analysis and lyric structure generation
2. Vocal synthesis using SongGeneration LeVo AI
3. Electronic backing track composition
4. Professional mixing and mastering
5. VirtualDJ deck integration

Status: Lyrics generated → Vocals rendering → Stems produced → Mix complete

Track 'Neon Metropolis' loaded to Deck 1. BPM: 130, Key: F minor.
Would you like me to generate variations or start mixing?"
```

### Large-Scale Projects
```
User: "Make me a 12-track album about urban exploration"

AI: "Planning autonomous album production for 'Urban Exploration' concept.

Album structure:
- Track 1: Street Lights - Opening ambient
- Track 2: Concrete Dreams - Driving rhythm
- Track 3: Hidden Alleys - Atmospheric interlude
- ...continuing through 12 tracks

Starting parallel production pipeline using SEP-1577 sampling:
- SongGeneration-MCP: Vocal and instrumental generation
- Reaper-MCP: Mastering and final production
- Plex-MCP: Library organization

Progress: 3/12 tracks complete. Estimated completion: 42 minutes.

First tracks available in your Plex music library."
```

### Conversational Assistance
```
User: "The mix needs more energy in the drop sections"

AI: "Analyzing your current production mix...

Current assessment:
- Energy profile: Moderate, could benefit from increased dynamics
- Frequency response: Mids-heavy, highs attenuated
- Rhythmic elements: Steady but lacking impact

Recommendations:
1. Apply upward compression to percussion bus (+4dB threshold, 3:1 ratio)
2. Add high-frequency boost to cymbals (2-3dB at 12kHz)
3. Implement sidechain ducking on pads during drops
4. Layer additional percussion hits for build-up tension

I can implement these changes automatically, or guide you through manual adjustments. Which approach would you prefer?"
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
- FastMCP 3.1.0+
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


## 🛡️ Industrial Quality Stack

This project adheres to **SOTA 14.1** industrial standards for high-fidelity agentic orchestration:

- **Python (Core)**: [Ruff](https://astral.sh/ruff) for linting and formatting. Zero-tolerance for `print` statements in core handlers (`T201`).
- **Webapp (UI)**: [Biome](https://biomejs.dev/) for sub-millisecond linting. Strict `noConsoleLog` enforcement.
- **Protocol Compliance**: Hardened `stdout/stderr` isolation to ensure crash-resistant JSON-RPC communication.
- **Automation**: [Justfile](./justfile) recipes for all fleet operations (`just lint`, `just fix`, `just dev`).
- **Security**: Automated audits via `bandit` and `safety`.

## License

MIT License

## Contributing

Contributions are welcome. Please see the development documentation for guidelines.

## Related Projects

- [SongGeneration-MCP](https://github.com/sandraschi/songgeneration-mcp) - AI music generation
- [VirtualDJ-MCP](https://github.com/sandraschi/virtualdj-mcp) - Professional DJ mixing
- [Plex-MCP](https://github.com/sandraschi/plex-mcp) - Media library management

