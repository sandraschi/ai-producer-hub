# ai-producer-hub (MCPB Bundle)

AI Music Producer - Generate, Mix, Master, Stream (VirtualDJ + LeVo AI + Plex + Reaper + OBS)

## Usage

Add to \claude_desktop_config.json\:
\\\json
{
  "mcpServers": {
    "ai-producer-hub": {
      "command": "uv",
      "args": ["run", "--directory", "\D:\Dev\repos", "python", "-m", "ai_producer_hub"],
      "env": { "PYTHONPATH": "\D:\Dev\repos/src" }
    }
  }
}
\\\

## Tools

- **songgen_to_deck**: songgen_to_deck
- **ai_dj_set**: ai_dj_set
- **remix_plex_track**: remix_plex_track
- **bpm_bridge_generator**: bpm_bridge_generator
- **live_stream_producer**: live_stream_producer
- **album_factory**: album_factory
- **karaoke_generator**: karaoke_generator
- **ai_mashup**: ai_mashup
- **hub_status**: hub_status
- **producer_help**: producer_help
- **list_midi_devices**: list_midi_devices
- **record_midi_performance**: record_midi_performance
- **send_midi_note**: send_midi_note
- **midi_to_reaper**: midi_to_reaper
- **midi_to_ai_seed**: midi_to_ai_seed
- **play_midi_file**: play_midi_file
- **midi_monitor**: midi_monitor

## Requirements

- Python 3.12+
- uv
