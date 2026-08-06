import { useState } from 'react'
import { Send, Eraser } from 'lucide-react'

export default function Chat() {
  const [messages, setMessages] = useState<{ role: string; content: string }[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const send = async () => {
    if (!input.trim() || loading) return
    const userMsg = { role: 'user', content: input }
    setMessages((m) => [...m, userMsg])
    setInput('')
    setLoading(true)
    try {
      setMessages((m) => [...m, { role: 'assistant', content: 'Use hub_status() to check fleet health, songgen_to_deck() to generate music.' }])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div data-testid="chat-page" className="flex flex-col h-full max-w-3xl mx-auto">
      <div data-testid="chat-controls" className="flex items-center gap-2 mb-4">
        <span className="text-xs text-zinc-500">AI Producer Hub</span>
        <button data-testid="chat-clear" onClick={() => setMessages([])} className="p-1.5 rounded hover:bg-zinc-800 text-zinc-400" title="Clear">
          <Eraser size={14} />
        </button>
      </div>
      <div data-testid="chat-messages" className="flex-1 overflow-auto space-y-4 mb-4">
        {messages.length === 0 && (
          <p className="text-zinc-600 text-sm text-center mt-8">Ask me to generate music or check fleet status.</p>
        )}
        {messages.map((m, i) => (
          <div key={i} className={`p-3 rounded-lg ${m.role === 'user' ? 'bg-zinc-800 ml-8' : 'bg-zinc-900 mr-8'}`}>
            <p className="text-sm text-zinc-300">{m.content}</p>
          </div>
        ))}
        {loading && <p className="text-zinc-500 text-sm text-center animate-pulse">Thinking...</p>}
      </div>
      <div className="flex gap-2">
        <input data-testid="chat-input"
          className="flex-1 bg-zinc-900 border border-zinc-700 rounded-lg px-4 py-2 text-sm text-zinc-100 outline-none focus:border-amber-500"
          placeholder="Generate a synthwave track..."
          value={input} onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && send()}
        />
        <button data-testid="chat-send" onClick={send} disabled={loading}
          className="p-2 bg-amber-600 rounded-lg hover:bg-amber-500 disabled:opacity-50">
          <Send size={16} />
        </button>
      </div>
    </div>
  )
}
