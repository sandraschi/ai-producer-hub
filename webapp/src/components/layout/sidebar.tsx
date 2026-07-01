import { NavLink } from 'react-router-dom'
import { useAppStore } from '@/store/app'
import { cn } from '@/lib/utils'
import {
  LayoutDashboard,
  Wrench,
  Piano,
  Settings,
  HelpCircle,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react'

const navItems = [
  { to: '/', label: 'Dashboard', icon: LayoutDashboard },
  { to: '/tools', label: 'Tools', icon: Wrench },
  { to: '/midi', label: 'MIDI', icon: Piano },
  { to: '/settings', label: 'Settings', icon: Settings },
  { to: '/help', label: 'Help', icon: HelpCircle },
]

export default function Sidebar() {
  const { sidebarOpen, toggleSidebar } = useAppStore()

  return (
    <aside
      className={cn(
        'flex flex-col bg-zinc-900 border-r border-zinc-800 transition-all duration-300',
        sidebarOpen ? 'w-56' : 'w-16',
      )}
    >
      <div className="flex items-center justify-between p-4 border-b border-zinc-800">
        {sidebarOpen && (
          <span className="text-sm font-semibold text-zinc-100 truncate">
            AI Producer Hub
          </span>
        )}
        <button
          data-testid="sidebar-collapse"
          onClick={toggleSidebar}
          className="p-1.5 rounded-md hover:bg-zinc-800 text-zinc-400 hover:text-zinc-100 transition-colors"
        >
          {sidebarOpen ? <ChevronLeft size={18} /> : <ChevronRight size={18} />}
        </button>
      </div>

      <nav className="flex-1 py-4 space-y-1 px-2">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) =>
              cn(
                'flex items-center gap-3 px-3 py-2.5 rounded-md text-sm transition-colors',
                isActive
                  ? 'bg-amber-500/10 text-amber-500'
                  : 'text-zinc-400 hover:text-zinc-100 hover:bg-zinc-800',
              )
            }
          >
            <item.icon size={18} />
            {sidebarOpen && <span>{item.label}</span>}
          </NavLink>
        ))}
      </nav>
    </aside>
  )
}
