import { Outlet, useLocation } from 'react-router-dom'
import Sidebar from './sidebar'
import Topbar from './topbar'

const pageTitles: Record<string, string> = {
  '/': 'Dashboard',
  '/tools': 'Tools',
  '/midi': 'MIDI',
  '/settings': 'Settings',
  '/help': 'Help',
}

export default function AppLayout() {
  const location = useLocation()
  const title = pageTitles[location.pathname] || 'AI Producer Hub'

  return (
    <div className="flex h-screen bg-zinc-950 text-zinc-100">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Topbar title={title} />
        <main className="flex-1 overflow-auto p-6">
          <Outlet />
        </main>
      </div>
    </div>
  )
}
