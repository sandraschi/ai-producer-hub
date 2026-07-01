const API_BASE = 'http://127.0.0.1:10800'

export async function checkHealth(): Promise<{ ok: boolean; error?: string }> {
  try {
    const r = await fetch(`${API_BASE}/api/health`)
    if (!r.ok) return { ok: false, error: `HTTP ${r.status}` }
    return { ok: true }
  } catch (e) {
    return { ok: false, error: e instanceof Error ? e.message : 'Network error' }
  }
}

export { API_BASE }
