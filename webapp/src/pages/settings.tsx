import { useState } from 'react'
import { Save } from 'lucide-react'

export default function Settings() {
  const [backendPort, setBackendPort] = useState('10800')
  const [saved, setSaved] = useState(false)

  const handleSave = () => {
    setSaved(true)
    setTimeout(() => setSaved(false), 2000)
  }

  return (
    <div className="max-w-xl space-y-6">
      <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
        <h2 className="text-base font-semibold text-zinc-100 mb-4">Connection</h2>
        <div className="space-y-4">
          <div>
            <label className="block text-sm text-zinc-400 mb-1">
              Backend Port
            </label>
            <input
              type="text"
              value={backendPort}
              onChange={(e) => setBackendPort(e.target.value)}
              className="w-full bg-zinc-800 border border-zinc-700 rounded-md px-3 py-2 text-sm text-zinc-200 focus:outline-none focus:ring-1 focus:ring-amber-500"
            />
          </div>
          <button
            onClick={handleSave}
            className="flex items-center gap-2 bg-amber-500 hover:bg-amber-600 text-black text-sm font-medium px-4 py-2 rounded-md transition-colors"
          >
            <Save size={16} />
            {saved ? 'Saved' : 'Save'}
          </button>
        </div>
      </div>

      <div className="bg-zinc-900 border border-zinc-800 rounded-lg p-5">
        <h2 className="text-base font-semibold text-zinc-100 mb-4">Environment</h2>
        <div className="space-y-3 text-sm text-zinc-400">
          <p>Configure environment variables in your .env file:</p>
          <code className="block bg-zinc-950 rounded-md p-3 text-xs text-zinc-300">
            MCP_PORT=10800{'\n'}
            MCP_HOST=127.0.0.1{'\n'}
            VIRTUALDJ_PORT=10877{'\n'}
            PLEX_URL=http://localhost:32400{'\n'}
            SONG_GEN_PORT=10885{'\n'}
            REAPER_PORT=10996{'\n'}
            OBS_WS_PORT=4444
          </code>
        </div>
      </div>
    </div>
  )
}
