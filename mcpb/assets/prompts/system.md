# AI Producer Hub — MCP Server Capabilities

## Server Overview

AI Producer Hub is a FastMCP 3.2 composite server that integrates AI music production with DJ mixing, media library management, DAW control, and live streaming. It mounts five specialized MCP servers (VirtualDJ-MCP, Plex-MCP, SongGeneration-MCP, Reaper-MCP, OBS-MCP) and layers cross-server AI workflows on top.

The server enables autonomous music production: generate a track from a text prompt, load it to a DJ deck, mix it with AI-generated tracks, and stream the result — all orchestrated through a single MCP interface. It supports MIDI device management, BPM-synced transitions, album factory workflows, karaoke generation, and AI-powered mashups.

**Core architecture:** AI Producer Hub is not a standalone server — it imports and mounts multiple external MCP servers using FastMCP's `mcp.mount()` API. This means it exposes 100+ tools total across all mounted servers, plus its own cross-orchestration tools. Each mounted server's tools are prefixed by their mount path (e.g., `/dj/*` for VirtualDJ, `/plex/*` for Plex, `/songgen/*` for SongGeneration).

## Tools

### songgen_to_deck

Generate an AI track using the LeVo AI model and load it directly to a VirtualDJ deck. This is the core AI Producer workflow: take lyrics and musical parameters, generate a professional track, and make it ready for mixing.

**Parameters:**
- `lyrics` (str, required): Complete lyrics for the song. Supports Markdown formatting for verse/chorus/bridge structure.
- `genre` (str, default `"Electronic"`): Musical genre — e.g., Electronic, Pop, Rock, Hip-Hop, Jazz, Classical, Lo-Fi, Trance, House, Techno, R&B, Country.
- `mood` (str, default `"Energetic"`): Overall vibe — e.g., Energetic, Melancholic, Happy, Dark, Calm, Euphoric, Aggressive, Dreamy.
- `tempo` (int, default `128`): Beats Per Minute, range 60-180.
- `voice` (str, default `"Male"`): Vocal type — `"Male"` or `"Female"`.
- `deck_id` (int, default `1`): VirtualDJ deck to load the track into (1-8).
- `separate_stems` (bool, default `False`): If True, generates separate vocal and instrument tracks.

**Return format:**
```json
{
  "workflow": "songgen_to_deck",
  "lyrics_preview": "Verse about coding all night...",
  "genre": "Electronic",
  "mood": "Energetic",
  "tempo": 128,
  "voice": "Male",
  "deck": 1,
  "separate_stems": false,
  "status": "generation_started",
  "message": "LeVo AI generation started - high-quality vocals + professional production!"
}
```

### ai_dj_set

Generates a complete AI-mixed DJ set from multiple track descriptions. Takes a setlist description and generates each track, transitions between them with BPM-synced crossfades, and loads them into VirtualDJ decks for playback. Supports auto-mixing of generated tracks with harmonic mixing.

**Parameters:**
- `set_theme` (str, required): Theme or description for the DJ set (e.g., "Sunset beach party mix", "Late night techno session").
- `track_count` (int, default `8`): Number of tracks to generate for the set (1-20).
- `genre` (str, default `"Electronic"`): Base genre for the set.
- `mood` (str, default `"Energetic"`): Overall vibe for the set.
- `voice` (str, default `"Male"`): Vocal type preference.
- `bpm_range` (str, default `"120-130"`): BPM range for the set (e.g., "120-130").
- `auto_transition` (bool, default `True`): Auto-calculates BPM-synced transitions between tracks.

**Return format:**
```json
{
  "set_theme": "Sunset beach party mix",
  "track_count": 8,
  "genre": "Electronic",
  "status": "generating",
  "setlist": [{"track": 1, "bpm": 120, "key": "A min"}, {"track": 2, "bpm": 124, "key": "C maj"}],
  "message": "AI DJ set generation started"
}
```

### remix_plex_track

Takes an existing track from a Plex library, analyzes it for structure (BPM, key, segment analysis), and generates an AI-powered remix using the LeVo model. The remix is stored back to the Plex library.

**Parameters:**
- `track_key` (str, required): Plex rating key of the track to remix.
- `remix_style` (str, default `"Extended Mix"`): Remix type — Extended Mix, Radio Edit, Dub Mix, Acoustic, Orchestral, Ambient, Drum and Bass, Chillstep.
- `bpm_adjust` (int, default `0`): BPM adjustment in percent (e.g., +10 for sped up).
- `key_shift` (str, optional): Key shift (e.g., "+2" for 2 semitones up).

### bpm_bridge_generator

Creates a BPM-synced transition bridge between two songs. Analyzes both tracks, calculates the optimal transition path (key, BPM, energy level), and generates a custom bridge audio file that smoothly transitions between them. Supports harmonic mixing and energy curve matching.

**Parameters:**
- `track_a` (str, required): Plex rating key or file path of the first track.
- `track_b` (str, required): Plex rating key or file path of the second track.
- `bridge_duration` (int, default `32`): Duration of the bridge in beats (default 32 beats).
- `transition_type` (str, default `"smooth"`): Transition style — smooth, hard_cut, echo_fade, filter_sweep, loop_roll, backspin.
- `harmonic_mix` (bool, default `True`): Enable harmonic mixing (key-aware transition).

### live_stream_producer

Produces a complete live-streamable audio broadcast. Generates or selects content, applies real-time mixing, configures OBS streaming settings, and starts broadcasting. Integrates with OBS-MCP for visual streaming and VirtualDJ-MCP for audio mixing.

**Parameters:**
- `stream_title` (str, required): Title for the live stream.
- `duration_minutes` (int, default `60`): Stream duration in minutes.
- `content_source` (str, default `"ai_generated"`): Source of content — "ai_generated", "plex_library", "mixed".
- `genre` (str, default `"Electronic"`): Genre for AI-generated content.
- `enable_video` (bool, default `False`): Enable OBS visual streaming.
- `video_source` (str, optional): OBS scene or source for video overlay.

### album_factory

Generates a complete multi-track album from a theme or description. Creates track listing, generates each track with appropriate styles, adds metadata (album art, track numbers, genre tags), and optionally uploads to Plex library. Supports concept albums with narrative structure.

**Parameters:**
- `theme` (str, required): Theme or concept for the album (e.g., "Journey through the digital realm").
- `track_count` (int, default `10`): Number of tracks in the album.
- `album_title` (str, optional): Album title. Auto-generated if omitted.
- `genre` (str, default `"Electronic"`): Primary genre.
- `vocal_style` (str, default `"mixed"`): Vocal approach — "male", "female", "mixed", "instrumental".
- `upload_to_plex` (bool, default `True`): Upload generated album to Plex library.

### karaoke_generator

Converts any track to a karaoke version by extracting vocals and generating synchronized lyrics display. Supports the fleet VirtualDJ karaoke deck workflow. Can generate instrumental-only versions with scrolling lyrics.

**Parameters:**
- `source_track` (str, required): Plex track key or file path to convert.
- `lyrics_input` (str, optional): Manual lyrics text. Will be auto-generated if omitted (uses AI transcription).
- `output_format` (str, default `"virtualdj"`): Output format — "virtualdj", "mp4", "cdg", "lrc".
- `vocal_removal_strength` (float, default `1.0`): Strength of vocal removal (0.0-1.0).

### ai_mashup

Creates a mashup of multiple tracks using AI analysis. Takes 2-4 tracks, analyzes their structure, aligns them by BPM and key, and generates a professionally mixed mashup. Supports section-level arrangement (e.g., "use chorus of track A with verse of track B").

**Parameters:**
- `track_keys` (list[str], required): Plex rating keys of tracks to mashup (2-4 tracks).
- `mashup_structure` (str, optional): Custom arrangement description (e.g., "A chorus, B verse, A drop, B chorus").
- `target_bpm` (int, optional): Target BPM. Auto-calculated if omitted.

### hub_status

Returns the health and availability status of all mounted servers (VirtualDJ, Plex, SongGeneration, Reaper, OBS) along with the overall hub version and tool counts.

**Parameters:** None.

**Return format:**
```json
{
  "server": "AI-Producer-Hub",
  "version": "1.0.0",
  "mounted_servers": {
    "virtualdj": {"mount": "/dj", "status": "connected", "tools": 61},
    "plex": {"mount": "/plex", "status": "connected", "tools": 15}
  },
  "midi_available": true,
  "total_tools": 100
}
```

### producer_help

Returns documentation about available tools, workflows, and integration points. Can filter by tool name or category.

**Parameters:**
- `tool_name` (str, optional): Specific tool to get help for.
- `category` (str, optional): Category filter — "generation", "djing", "midi", "streaming", "mixing".

### list_midi_devices

Lists all MIDI input and output devices available on the system. Returns device names, port numbers, and capabilities (input/output/both).

**Parameters:**
- `type` (str, default `"all"`): Filter by type — "input", "output", "all".

### record_midi_performance

Records a MIDI performance from a connected MIDI input device. Supports recording with metronome, count-in, and quantize options. Saves as a MIDI file and returns the file path.

**Parameters:**
- `device_index` (int, default `0`): Index of the MIDI input device to record from.
- `duration_seconds` (int, default `30`): Recording duration in seconds.
- `metronome` (bool, default `True`): Enable metronome during recording.
- `quantize` (bool, default `True`): Quantize recorded notes to grid.
- `output_name` (str, optional): Output filename for the MIDI file.

### send_midi_note

Sends a single MIDI note message to a connected MIDI output device. Useful for testing MIDI connectivity, triggering hardware synths, or adding accent notes to a live performance.

**Parameters:**
- `device_index` (int, default `0`): MIDI output device index.
- `note` (int, required): MIDI note number (0-127, where 60 = middle C).
- `velocity` (int, default `100`): Note velocity/volume (0-127).
- `channel` (int, default `1`): MIDI channel (1-16).
- `duration_ms` (int, default `500`): Note duration in milliseconds.

### midi_to_reaper

Exports recorded MIDI data to a REAPER DAW project. Creates a new REAPER project file with the MIDI track loaded, ready for further editing, effects processing, and mixing.

**Parameters:**
- `midi_file` (str, required): Path to the MIDI file to export.
- `project_name` (str, default `"MIDI Import"`): Name for the new REAPER project.
- `output_path` (str, optional): Output directory. Defaults to user's Documents folder.
- `tempo` (int, default `120`): Project tempo in BPM.

### midi_to_ai_seed

Converts a MIDI performance or file into an AI generation seed. The MIDI is analyzed for melodic patterns, chord progressions, and rhythmic structure, which are then used as conditioning input for the LeVo AI model to generate a track based on the MIDI's musical DNA.

**Parameters:**
- `midi_file` (str, required): Path to the MIDI file to analyze.
- `genre` (str, default `"Electronic"`): Target genre for the AI generation.
- `preserve_melody` (bool, default `True`): If True, preserves the original melody.

### play_midi_file

Plays a MIDI file through the system's default MIDI player or a specified output device. Supports loop, tempo override, and channel muting.

**Parameters:**
- `midi_file` (str, required): Path to the MIDI file to play.
- `device_index` (int, default `0`): MIDI output device index. Use -1 for system default.
- `tempo_percent` (int, default `100`): Playback speed (50-200 percent).
- `loop` (bool, default `False`): Loop playback.

### midi_monitor

Opens a real-time MIDI monitor that displays incoming MIDI messages from connected devices. Shows note on/off, control change, pitch bend, and other MIDI events with timestamps. Stops when the CLI context exits.

**Parameters:**
- `device_index` (int, default `0`): MIDI input device to monitor.
- `duration_seconds` (int, default `30`): Monitoring duration. Use -1 for continuous.

## Configuration

### Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `AI_PRODUCER_HUB_PORT` | 10899 | Backend HTTP port |
| `VIDEODJ_PORT` | 10877 | VirtualDJ-MCP bridge port |
| `PLEX_URL` | `http://127.0.0.1:32400` | Plex server URL |
| `PLEX_TOKEN` | — | Plex authentication token |
| `SONGGEN_URL` | `http://127.0.0.1:10885` | SongGeneration-MCP URL |
| `REAPER_MCP_URL` | `http://127.0.0.1:10797` | Reaper-MCP bridge URL |
| `OBS_WS_URL` | `ws://127.0.0.1:4455` | OBS WebSocket URL |
| `OBS_WS_PASSWORD` | — | OBS WebSocket password |
| `AI_API_KEY` | — | API key for AI model services |

## Data Sources

### Mounted MCP Servers

1. **VirtualDJ-MCP** (`/dj/*`): 61 tools — mixing, stems, 8-deck control, effects, video mixing, looping, sampling, BPM analysis, beatgrid, playlist management, track analysis, waveform display, recording.

2. **Plex-MCP** (`/plex/*`): 15 tools — media library browsing, track search, playlist management, loudness analysis, track metadata, library statistics, watch history, collections.

3. **SongGeneration-MCP** (`/songgen/*`): 7 tools — LeVo AI model track generation, voice cloning, style transfer, stem separation, mastering, audio analysis, lyrics generation.

4. **Reaper-MCP** (`/reaper/*`): DAW control tools — transport, track management, FX insertion, automation, routing, recording, mixing console, project management.

5. **OBS-MCP** (`/obs/*`): Streaming tools — scene switching, source visibility, recording, streaming toggle, audio mixer, filters, transitions, media sources.

### AI Agent (ctx.sample)

The server uses FastMCP sampling (`ctx.sample()`) for AI-powered workflows, enabling autonomous multi-step music production. The AI agent can plan and execute complex production pipelines without manual step-by-step tool calls.

## Error Handling

All tools return structured JSON with `status` field. On failure, errors include:
- `error` (str): Human-readable error message
- `step` (str): Which pipeline step failed
- `recovery_options` (list[str]): Suggested next steps

Known failure modes:
- **MIDI device not found**: Check device connectivity and driver installation
- **AI generation timeout**: Reduce track complexity or check AI API connectivity
- **Server mount failure**: The required MCP server (VirtualDJ, Plex, etc.) is not installed
- **Plex track not found**: Verify track key and Plex server connectivity

## Integration Points

- **VirtualDJ-MCP** (port 10877): Deck control, mixing, effects
- **Plex-MCP** (port 32400): Media library access
- **SongGeneration-MCP** (port 10885): AI music generation
- **Reaper-MCP** (port 10797): DAW production control
- **OBS-MCP** (port 4455): Live streaming
- **LeVo AI Model**: Local AI music generation via SongGeneration API
