import { Book, Piano, Radio, Cpu } from 'lucide-react'

const helpSections = [
  {
    title: 'Getting Started',
    icon: Book,
    content:
      'AI Producer Hub orchestrates your music production stack through MCP. Connect your MIDI controllers, configure your DAW bridge, and use AI-powered tools for generation and analysis.',
  },
  {
    title: 'MIDI Setup',
    icon: Piano,
    content:
      'Plug in your MIDI controllers via USB. Check the MIDI page to verify they are detected. Configure routing in your DAW or use the MIDI route tool to pipe messages between applications.',
  },
  {
    title: 'Cross-Server Workflows',
    icon: Radio,
    content:
      'Use the workflow tools to orchestrate across VirtualDJ, Plex, SongGeneration, Reaper, and OBS. The arr_orchestrate tool chains media requests with automatic availability checking.',
  },
  {
    title: 'AI Generation',
    icon: Cpu,
    content:
      'The AI agent tools use local models (Ollama) and cloud APIs for music generation, audio analysis, and intelligent remixing. Configure your preferred model in Settings.',
  },
]

export default function Help() {
  return (
    <div className="space-y-6">
      {helpSections.map((section) => (
        <div
          key={section.title}
          className="bg-zinc-900 border border-zinc-800 rounded-lg p-5"
        >
          <div className="flex items-center gap-3 mb-2">
            <section.icon size={20} className="text-amber-500" />
            <h2 className="text-base font-semibold text-zinc-100">
              {section.title}
            </h2>
          </div>
          <p className="text-sm text-zinc-400 leading-relaxed">
            {section.content}
          </p>
        </div>
      ))}
    </div>
  )
}
