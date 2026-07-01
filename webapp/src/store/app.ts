import { create } from 'zustand'

type BackendStatus = 'unknown' | 'online' | 'offline'

interface AppState {
  sidebarOpen: boolean
  backendStatus: BackendStatus
  toggleSidebar: () => void
  setBackendStatus: (status: BackendStatus) => void
}

export const useAppStore = create<AppState>((set) => ({
  sidebarOpen: true,
  backendStatus: 'unknown',
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
  setBackendStatus: (status) => set({ backendStatus: status }),
}))
