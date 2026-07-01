import { Piano, AlertCircle } from 'lucide-react'

const midiDevices = [
  { name: 'Arturia KeyLab Essential 88', status: 'Connected', inputs: 1, outputs: 1 },
  { name: 'Launchpad Pro MK3', status: 'Connected', inputs: 1, outputs: 1 },
  { name: 'MIDI Fighter Twister', status: 'Connected', inputs: 1, outputs: 1 },
]

export default function Midi() {
  return (
    <div className="space-y-6">
      <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
        <div className="flex items-center gap-3 mb-4">
          <Piano size={20} className="text-amber-500" />
          <h2 className="text-base font-semibold text-zinc-100">MIDI Devices</h2>
        </div>
        <div className="space-y-2">
          {midiDevices.map((dev) => (
            <div
              key={dev.name}
              className="flex items-center justify-between bg-zinc-800 rounded-md px-4 py-3"
            >
              <div>
                <p className="text-sm text-zinc-200">{dev.name}</p>
                <p className="text-xs text-zinc-500">
                  {dev.inputs} in / {dev.outputs} out
                </p>
              </div>
              <span className="flex items-center gap-1.5 text-xs text-green-500">
                <span className="w-1.5 h-1.5 rounded-full bg-green-500" />
                {dev.status}
              </span>
            </div>
          ))}
        </div>
      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
        <div className="flex items-center gap-3 mb-4">
          <AlertCircle size={20} className="text-amber-500" />
          <h2 className="text-base font-semibold text-zinc-100">Monitor</h2>
        </div>
        <div className="bg-zinc-950 rounded-md p-4 font-mono text-xs text-zinc-600 h-48 overflow-y-auto">
          <p>Waiting for MIDI messages...</p>
        </div>
      </div>
    </div>
  )
}
