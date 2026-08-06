import { Radio, Cpu, Zap, Disc } from 'lucide-react'

const toolCategories = [
  {
    title: 'Generation', icon: Zap,
    description: 'AI music generation via SongGeneration LeVo.',
    tools: [
      'songgen_to_deck(lyrics, genre, tempo) - Generate song -> Load to VDJ',
      'album_factory(theme, num_tracks) - Multi-track album from theme',
      'ai_dj_set(theme, num_tracks) - Generate DJ set across decks',
    ],
  },
  {
    title: 'Production', icon: Radio,
    description: 'Live and batch production workflows.',
    tools: [
      'live_stream_producer(theme, duration) - Set up live stream with AI music',
      'ai_mashup(track_a, track_b) - Mashup plan from VDJ library search',
    ],
  },
  {
    title: 'MIDI', icon: Cpu,
    description: 'MIDI hardware tools (requires python-rtmidi).',
    tools: [
      'list_midi_devices() - Enumerate connected MIDI devices',
      'record_midi_performance(device, duration) - Record MIDI to file',
      'send_midi_note(device, note, velocity) - Send MIDI note',
      'play_midi_file(file, device) - Play MIDI file through output',
      'midi_monitor(device) - Live MIDI message viewer',
      'midi_to_ai_seed(midi_file) - Analyze MIDI for AI seed prompt',
    ],
  },
  {
    title: 'Fleet', icon: Disc,
    description: 'Fleet status and cooperation with audio stack servers.',
    tools: [
      'hub_status() - Check all fleet server health',
      'producer_help(topic) - Help for workflows',
    ],
  },
]

export default function Tools() {
  return (
    <div className="space-y-6" data-testid="tools-page">
      {toolCategories.map((cat) => (
        <div key={cat.title} className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
          <div className="flex items-center gap-3 mb-2">
            <cat.icon size={20} className="text-amber-500" />
            <h2 className="text-base font-semibold text-zinc-100">{cat.title}</h2>
          </div>
          <p className="text-sm text-zinc-500 mb-3">{cat.description}</p>
          <ul className="space-y-1.5">
            {cat.tools.map((tool) => (
              <li key={tool} className="text-sm text-zinc-300 flex items-start gap-2">
                <span className="text-amber-500 mt-0.5">-</span>
                <span>{tool}</span>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  )
}
