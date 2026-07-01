import { useEffect } from 'react'
import { useAppStore } from '@/store/app'
import { checkHealth } from '@/lib/api'
import { cn } from '@/lib/utils'

interface TopbarProps {
  title: string
}

export default function Topbar({ title }: TopbarProps) {
  const { backendStatus, setBackendStatus } = useAppStore()

  useEffect(() => {
    const check = async () => {
      const { ok } = await checkHealth()
      setBackendStatus(ok ? 'online' : 'offline')
    }
    check()
    const interval = setInterval(check, 10000)
    return () => clearInterval(interval)
  }, [setBackendStatus])

  return (
    <header className="flex items-center justify-between h-14 px-6 border-b border-zinc-800 bg-zinc-900">
      <h1 className="text-lg font-semibold text-zinc-100">{title}</h1>
      <div className="flex items-center gap-2">
        <span className="text-xs text-zinc-500">
          {backendStatus === 'unknown'
            ? 'Connecting...'
            : backendStatus === 'online'
              ? 'Connected'
              : 'Offline'}
        </span>
        <div
          data-testid="backend-dot"
          className={cn(
            'w-2 h-2 rounded-full',
            backendStatus === 'unknown' && 'bg-zinc-500',
            backendStatus === 'online' && 'bg-green-500',
            backendStatus === 'offline' && 'bg-red-500',
          )}
        />
      </div>
    </header>
  )
}
