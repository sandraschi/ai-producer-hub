import { createBrowserRouter } from 'react-router-dom'
import AppLayout from './components/layout/app-layout'
import Dashboard from './pages/dashboard'
import Tools from './pages/tools'
import Midi from './pages/midi'
import Settings from './pages/settings'
import Help from './pages/help'

export const router = createBrowserRouter([
  {
    element: <AppLayout />,
    children: [
      { path: '/', element: <Dashboard /> },
      { path: '/tools', element: <Tools /> },
      { path: '/midi', element: <Midi /> },
      { path: '/settings', element: <Settings /> },
      { path: '/help', element: <Help /> },
    ],
  },
])
