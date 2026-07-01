import { HardDrive, Cpu, Music, Radio, Monitor } from 'lucide-react'

const mountedServers = [
  { name: 'VirtualDJ', icon: Radio },
  { name: 'Plex', icon: Music },
  { name: 'SongGeneration', icon: Music },
  { name: 'Reaper', icon: Monitor },
  { name: 'OBS', icon: Monitor },
]

export default function Dashboard() {
  return (
    <div data-testid="dashboard" className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div data-testid="kpi-server" className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
          <div className="flex items-center gap-3 mb-3">
            <HardDrive className="text-amber-500" size={20} />
            <span className="text-sm font-medium text-zinc-400">Server</span>
          </div>
          <p className="text-lg font-semibold text-zinc-100">AI Producer Hub</p>
        </div>
        <div data-testid="kpi-tools" className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
          <div className="flex items-center gap-3 mb-3">
            <Cpu className="text-amber-500" size={20} />
            <span className="text-sm font-medium text-zinc-400">Tools</span>
          </div>
          <p className="text-lg font-semibold text-zinc-100">21+ registered</p>
        </div>
        <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
          <div className="flex items-center gap-3 mb-3">
            <Music className="text-amber-500" size={20} />
            <span className="text-sm font-medium text-zinc-400">MIDI Devices</span>
          </div>
          <p className="text-lg font-semibold text-zinc-100">Check MIDI page</p>
        </div>
      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
        <h2 className="text-sm font-medium text-zinc-400 mb-4">Mounted Servers</h2>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
          {mountedServers.map((s) => (
            <div
              key={s.name}
              className="flex items-center gap-2 bg-zinc-800 rounded-md px-3 py-2"
            >
              <s.icon size={16} className="text-amber-500" />
              <span className="text-sm text-zinc-200">{s.name}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
