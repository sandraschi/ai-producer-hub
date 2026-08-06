# AI Producer Hub — User Guide

## Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sandraschi/ai-producer-hub.git
   cd ai-producer-hub
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Configure environment:**
   Copy `.env.example` to `.env` and set:
   ```
   PLEX_URL=http://127.0.0.1:32400
   PLEX_TOKEN=your_plex_token
   AI_API_KEY=your_ai_api_key
   ```

4. **Run the server:**
   ```bash
   uv run python -m ai_producer_hub
   ```

5. **Add to Claude Desktop:**
   ```json
   {
     "mcpServers": {
       "ai-producer-hub": {
         "command": "uv",
         "args": ["run", "--directory", "C:\\path\\to\\ai-producer-hub", "python", "-m", "ai_producer_hub"]
       }
     }
   }
   ```

6. **Verify:**
   Call `hub_status()` to see which servers are mounted and available.

### Prerequisites

- **VirtualDJ-MCP**: Required for DJ deck workflows
- **Plex-MCP**: Required for media library access
- **SongGeneration-MCP**: Required for AI music generation
- **Reaper-MCP** (optional): Required for DAW workflows
- **OBS-MCP** (optional): Required for live streaming
- **MIDI drivers**: Required for MIDI hardware support

## Tutorials

### Tutorial 1: Generate a Song and Load to DJ Deck

The core workflow — create music from lyrics and play it immediately.

```python
# Step 1: Generate track and load to deck
result = songgen_to_deck(
    lyrics="""[Verse]
    Coding through the neon night
    AI dreams in digital light
    [Chorus]
    We are the creators of tomorrow
    Building worlds from ones and zeros
    """,
    genre="Electronic",
    mood="Energetic",
    tempo=128,
    voice="Male",
    deck_id=1
)
print(f"Track loaded to deck {result['deck']}")
```

### Tutorial 2: Generate a Full DJ Set

Create an entire AI DJ set with multiple tracks and transitions.

```python
set_result = ai_dj_set(
    set_theme="Sunset beach party mix",
    track_count=8,
    genre="House",
    mood="Euphoric",
    bpm_range="120-128",
    auto_transition=True
)
print(f"Generated {set_result['track_count']} tracks")
for track in set_result['setlist']:
    print(f"Track {track['track']}: {track['bpm']} BPM, {track['key']}")
```

### Tutorial 3: Create a BPM Bridge Between Two Tracks

Smoothly transition between two tracks with a generated BPM-synced bridge.

```python
bridge = bpm_bridge_generator(
    track_a="12345",  # Plex track key
    track_b="67890",
    bridge_duration=32,
    transition_type="smooth",
    harmonic_mix=True
)
print(f"Bridge generated: {bridge.get('bridge_file', 'pending')}")
```

### Tutorial 4: Live Stream Production

Produce and broadcast a live DJ set with AI-generated content.

```python
stream = live_stream_producer(
    stream_title="AI-Generated Sunset Session",
    duration_minutes=60,
    content_source="ai_generated",
    genre="Deep House",
    enable_video=True,
    video_source="DJ Cam"
)
print(f"Stream started: {stream.get('stream_url', '')}")
```

### Tutorial 5: Create a Full Album

Generate a complete concept album with AI.

```python
album = album_factory(
    theme="Journey through the digital realm",
    track_count=10,
    album_title="Digital Horizons",
    genre="Electronic",
    vocal_style="mixed",
    upload_to_plex=True
)
print(f"Album created: {album.get('album_title', '')}")
for track in album.get('tracks', []):
    print(f"  {track['number']}. {track['title']}")
```

### Tutorial 6: AI Remix a Plex Track

Take any track from your music library and create an AI-powered remix.

```python
remix = remix_plex_track(
    track_key="12345",
    remix_style="Drum and Bass",
    bpm_adjust=+20
)
print(f"Remix {remix.get('status', '')}")
```

### Tutorial 7: Generate a Karaoke Track

Convert any track to karaoke with synchronized lyrics.

```python
karaoke = karaoke_generator(
    source_track="12345",
    output_format="virtualdj",
    vocal_removal_strength=1.0
)
print(f"Karaoke track ready: {karaoke.get('output_file', '')}")
```

### Tutorial 8: Create an AI Mashup

Merge multiple tracks into a single professional mashup.

```python
mashup = ai_mashup(
    track_keys=["12345", "67890", "11111"],
    mashup_structure="A drop, B verse, C chorus, A breakdown, B drop, A chorus"
)
print(f"Mashup generated: {mashup.get('output_file', '')}")
```

### Tutorial 9: Record a MIDI Performance

Capture a MIDI keyboard performance for use in further production.

```python
# List MIDI devices first
devices = list_midi_devices(type="input")
print(f"Found {len(devices)} input devices")

# Record a performance
recording = record_midi_performance(
    device_index=0,
    duration_seconds=30,
    metronome=True,
    quantize=True,
    output_name="my_melody.mid"
)
print(f"Recorded: {recording.get('midi_file', '')}")
```

### Tutorial 10: Send MIDI Notes

Test MIDI connectivity by sending notes to a hardware synth.

```python
# Send a C major chord
send_midi_note(device_index=0, note=60, velocity=100, channel=1, duration_ms=500)
send_midi_note(device_index=0, note=64, velocity=100, channel=1, duration_ms=500)
send_midi_note(device_index=0, note=67, velocity=100, channel=1, duration_ms=500)
```

### Tutorial 11: Use MIDI as AI Seed

Convert a played melody into the basis for AI track generation.

```python
seed = midi_to_ai_seed(
    midi_file="my_melody.mid",
    genre="Trance",
    preserve_melody=True
)
print(f"AI generation seeded: {seed.get('seed_id', '')}")

# Then generate the actual track
songgen_to_deck(
    lyrics="From a simple melody, a world was born...",
    genre="Trance",
    tempo=138,
    deck_id=2
)
```

### Tutorial 12: Export MIDI to Reaper

Move a recorded MIDI performance into a professional DAW.

```python
midi_to_reaper(
    midi_file="my_melody.mid",
    project_name="AI Collaboration",
    tempo=128,
    output_path="D:\\Music\\Projects"
)
print("Reaper project created — open it in REAPER for further editing")
```

### Tutorial 13: Full Pipeline — Idea to Broadcast

Complete autonomous music production pipeline.

```python
# 1. Generate a track
songgen_to_deck(
    lyrics="Sunset over the digital sea...",
    genre="Progressive House",
    tempo=126,
    deck_id=1
)

# 2. Generate a second track for the set
songgen_to_deck(
    lyrics="Neon lights reflect on water...",
    genre="Progressive House",
    tempo=128,
    deck_id=2
)

# 3. Create a BPM bridge
bpm_bridge_generator(track_a="track1_path", track_b="track2_path", bridge_duration=32)

# 4. Start live streaming
live_stream_producer(
    stream_title="AI Producer Live",
    duration_minutes=120,
    content_source="mixed",
    enable_video=False
)
```

### Tutorial 14: Check Hub Status

Quick health check of all mounted servers.

```python
status = hub_status()
print(f"Server: {status['server']} v{status['version']}")
for name, info in status.get('mounted_servers', {}).items():
    print(f"{name}: {info['status']} ({info.get('tools', '?')} tools)")
print(f"MIDI: {'available' if status.get('midi_available') else 'not available'}")
```

### Tutorial 15: Get Help for a Specific Tool

Access detailed documentation for any tool.

```python
help_info = producer_help(tool_name="songgen_to_deck")
print(help_info['documentation'])

# Get tools by category
category_help = producer_help(category="generation")
for tool in category_help.get('tools', []):
    print(f"  {tool['name']}: {tool['description'][:80]}")
```

## Troubleshooting

### "Mount server not available"

If `hub_status()` shows a server as disconnected, the required MCP server package is not installed. Install the server:
```bash
uv add virtualdj-mcp
uv add plex-mcp
```

### MIDI device not detected

- Check that the MIDI device is connected and powered on
- On Windows, check Device Manager for driver issues
- Run `list_midi_devices(type="all")` to see what's detected

### AI generation fails

- Verify `AI_API_KEY` is set in your `.env` file
- Check SongGeneration-MCP is running at the configured URL
- Reduce the complexity of the generation (shorter lyrics, simpler genre)

## FAQ

**Q: Do I need all mounted servers?**
A: No. Each mounted server is optional. Missing servers simply skip tool registration. The hub works with any subset.

**Q: Can I use this without VirtualDJ?**
A: Yes. MIDI tools and basic AI generation work independently of VirtualDJ. Only `songgen_to_deck`, `ai_dj_set`, and `bpm_bridge_generator` require VirtualDJ-MCP.

**Q: What AI model powers the music generation?**
A: The LeVo model from SongGeneration-MCP provides the AI music generation. It runs locally or via API depending on configuration.

**Q: How many tracks can I generate in parallel?**
A: The hub processes one generation at a time. Multiple generations can be queued and processed sequentially.

**Q: Can I use my own lyrics?**
A: Yes. Pass complete lyrics to `songgen_to_deck`. Use Markdown formatting for verse/chorus structure.

**Q: What audio formats are supported for output?**
A: WAV, MP3, FLAC, and OGG. Output format depends on the mounted server's capabilities.

**Q: Can I connect external hardware synths?**
A: Yes, via MIDI. Use `list_midi_devices()` to detect hardware, then `send_midi_note()` or `record_midi_performance()`.

**Q: Does this support real-time streaming?**
A: Yes. `live_stream_producer()` integrates with OBS-MCP for live streaming with audio and optional video.
