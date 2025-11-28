# AI Producer Hub 🎹🤖

**1983 MIDI Standard + 2025 AI = The Future of Music Production**

Plink a melody on your synth. AI turns it into a full track. Load it to VirtualDJ. Mix 8 decks. Stream live.

All in one server.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   🎹 MIDI In ──► 🤖 AI Generation ──► 🎧 DJ Mix ──► 📺 Live Stream         │
│                                                                             │
│   Your 4-bar melody becomes a 3-minute banger in 60 seconds                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## The Vision

**NO HUMAN CAN:**
- Generate a track from a prompt in 30 seconds
- Mix 8 AI-generated tracks simultaneously  
- Create a full album in an hour
- Live stream with infinite unique content
- Turn a MIDI doodle into a produced track instantly

**AI CAN.** This hub makes it happen.

## Mounted Servers

| Server | Mount | Tools | Purpose |
|--------|-------|-------|---------|
| VirtualDJ-MCP | `/dj/*` | 61 | Mixing, stems, video, 8 decks |
| Plex-MCP | `/plex/*` | 15 | Media library |
| Suno-MCP | `/suno/*` | ? | AI music generation |
| Reaper-MCP | `/reaper/*` | ? | DAW/mastering |
| OBS-MCP | `/obs/*` | ? | Live streaming |
| **+ Local MIDI** | (root) | 8 | Hardware I/O |

## MIDI Tools - Your Hardware, AI's Brain

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  Your Synth/     │    │  AI Producer     │    │  Full Track      │
│  Keyboard        │───►│  Hub             │───►│  Ready to Mix    │
│  (MIDI out)      │    │  (MIDI → AI)     │    │  (VirtualDJ)     │
└──────────────────┘    └──────────────────┘    └──────────────────┘
```

### MIDI Workflow

```python
# 1. Check your devices
list_midi_devices()
# Returns: {"inputs": ["MPK mini 3", "Arturia KeyLab"], ...}

# 2. Record your melody (play something!)
record_midi_performance(device_index=0, duration_seconds=30)
# Saves to: ~/Music/AI-Producer-Hub/MIDI-Recordings/recording_20251128_143022.mid

# 3. AI analyzes and generates a prompt
midi_to_ai_seed("recording.mid", expansion_style="full_production")
# Returns: "Create a full production track in C major, 
#           with drums, bass, pads, target duration 120 seconds"

# 4. Generate the full track!
suno_to_deck(generated_prompt, deck=1)
# Your 4-bar melody is now a full track on Deck 1!
```

### Available MIDI Tools

| Tool | Description |
|------|-------------|
| `list_midi_devices` | Scan for connected MIDI hardware |
| `record_midi_performance` | Capture your playing to MIDI file |
| `send_midi_note` | Send notes to synths/modules |
| `play_midi_file` | Play MIDI through your hardware |
| `midi_monitor` | Debug/test MIDI connections |
| `midi_to_reaper` | Import MIDI to DAW for rendering |
| `midi_to_ai_seed` | Analyze MIDI → Generate AI prompt |

## Cross-Server Workflows

### Generate & Mix
```python
# AI DJ set from a theme
ai_dj_set("dark techno warehouse", num_tracks=6)

# Single track to deck
suno_to_deck("synthwave 128bpm neon city", deck=1)
```

### MIDI → AI → DJ
```python
# Record your melody
record_midi_performance(0, 30)

# AI expands it
midi_to_ai_seed("recording.mid", "full_production")

# Generate and load
suno_to_deck(prompt, deck=1)

# Mix with 7 other tracks!
```

### Live Stream Producer
```python
live_stream_producer(
    theme="lo-fi study beats",
    duration_hours=2,
    platform="twitch"
)
# AI generates tracks continuously while you stream!
```

### Album Factory
```python
album_factory(
    "cyberpunk noir detective neo-tokyo",
    num_tracks=12,
    album_title="Neon Shadows"
)
# Full album, saved to Plex library!
```

## Installation

```powershell
# Clone
git clone https://github.com/sandraschi/ai-producer-hub.git
cd ai-producer-hub

# Create venv (Python 3.11 for aubio compatibility)
uv venv --python 3.11
.venv\Scripts\Activate.ps1

# Install
uv pip install -e .

# Install component servers
uv pip install -e D:\Dev\repos\virtualdj-mcp
uv pip install -e D:\Dev\repos\plexmcp
uv pip install -e D:\Dev\repos\suno-mcp
# ... etc
```

### MIDI Requirements

For MIDI functionality on Windows:
- `python-rtmidi` requires Visual C++ Build Tools
- Or install pre-built wheel: `pip install python-rtmidi`

## Claude Desktop Config

```json
{
  "mcpServers": {
    "ai-producer-hub": {
      "command": "python",
      "args": ["-m", "ai_producer_hub"],
      "cwd": "D:\\Dev\\repos\\ai-producer-hub"
    }
  }
}
```

## Example Sessions

### Session 1: MIDI Jam to Full Track

```
You: "List my MIDI devices"
AI:  {"inputs": ["MPK mini 3"], "outputs": ["Microsoft GS"]}

You: "Record from device 0 for 30 seconds"
AI:  [You play a melody on your keyboard]
AI:  "Recorded 47 events to recording_20251128.mid"

You: "Turn that into a full synthwave track"
AI:  [Analyzes MIDI, generates prompt, calls Suno]
AI:  "Generated 'Neon Dreams' - loaded to Deck 1!"

You: "Generate 3 more tracks in similar style, load to decks 2-4"
AI:  [Generates and loads]
AI:  "4 tracks ready. Start mixing?"
```

### Session 2: Live Stream Producer

```
You: "Start a 2-hour lo-fi stream on Twitch"
AI:  [Starts OBS, generates initial tracks, begins automix]
AI:  "Streaming! Generating new tracks every 10 minutes."
AI:  [2 hours later]
AI:  "Stream complete. 12 unique AI tracks played. Recording saved."
```

### Session 3: Album in an Hour

```
You: "Make me a 10-track album about space exploration"
AI:  [Generates track list with variations]
     Track 1: "Launch Sequence" - epic orchestral intro
     Track 2: "Zero Gravity" - ambient floating
     Track 3: "First Contact" - mysterious tension
     ... etc
AI:  [Generates all tracks via Suno]
AI:  [Masters in Reaper]
AI:  [Adds to Plex library]
AI:  "Album 'Beyond the Stars' complete. 10 tracks, 42 minutes."
```

## Architecture

```
AI-Producer-Hub
├── Local Tools
│   └── MIDI (8 tools) ─── python-rtmidi + mido
│
├── Mounted Servers
│   ├── /dj/*     ─── VirtualDJ-MCP (61 tools)
│   ├── /plex/*   ─── Plex-MCP (15 tools)
│   ├── /suno/*   ─── Suno-MCP (AI generation)
│   ├── /reaper/* ─── Reaper-MCP (DAW)
│   └── /obs/*    ─── OBS-MCP (streaming)
│
└── Cross-Server Workflows
    ├── suno_to_deck()
    ├── ai_dj_set()
    ├── midi_to_ai_seed()
    ├── live_stream_producer()
    ├── album_factory()
    └── ... more
```

## MIDI + AI: The Bridge

**MIDI (1983)**: A 41-year-old standard that still connects every piece of music hardware.

**AI (2025)**: Models that can generate music from text descriptions.

**This Hub**: The bridge between your physical instruments and AI's creative power.

```
Your fingers on keys → MIDI bytes → AI understanding → Full production
     (1983 tech)      (serial data)   (2025 magic)    (instant result)
```

Play 4 bars. Get a track. That's the future.

## License

MIT License

---

**Made with 🎹 + 🤖 for musicians who want AI as their co-producer**

*Your melody. AI's production. Your mix. Infinite possibilities.*

