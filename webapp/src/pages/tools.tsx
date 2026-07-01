import { Radio, Cpu, Monitor, Zap } from 'lucide-react'

const toolCategories = [
  {
    title: 'Workflow Tools',
    icon: Radio,
    description: 'Cross-server orchestration and media pipeline management.',
    tools: [
      'arr_orchestrate - Unified media request with auto-routing',
      'arr_calendar - Cross-arr release timeline',
      'arr_agentic - Natural language media management',
      'arr_stats - Consolidated stack statistics',
    ],
  },
  {
    title: 'MIDI Tools',
    icon: Cpu,
    description: 'MIDI hardware control, monitoring, and routing.',
    tools: [
      'midi_list_devices - Enumerate connected MIDI controllers',
      'midi_monitor - Live MIDI message viewer',
      'midi_send - Send MIDI messages to devices',
      'midi_route - Route MIDI between applications',
    ],
  },
  {
    title: 'AI Agent Tools',
    icon: Zap,
    description: 'AI-powered music generation and intelligent assistance.',
    tools: [
      'ai_generate - Generate music from text prompts',
      'ai_analyze - Analyze audio for key, tempo, structure',
      'ai_remix - AI-assisted remixing and arrangement',
      'ai_agent_workflow - Multi-step creative agent workflows',
    ],
  },
  {
    title: 'Integration Tools',
    icon: Monitor,
    description: 'Cross-server bridge tools for the music production stack.',
    tools: [
      'virtualdj_bridge - Deck control via VirtualDJ',
      'plex_media_bridge - Media server integration',
      'reaper_bridge - DAW transport and track control',
      'obs_mount - Scene and source management',
    ],
  },
]

export default function Tools() {
  return (
    <div className="space-y-6">
      {toolCategories.map((cat) => (
        <div
          key={cat.title}
          className="bg-zinc-900 border border-zinc-800 rounded-lg p-5"
        >
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
