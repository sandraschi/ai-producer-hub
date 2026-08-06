; Kill UI + backend before install/uninstall (backend locks resources/*.exe).
!macro KillAiProducerHubFleetProcesses
  DetailPrint "Stopping ai-producer-hub processes..."
  ExecWait 'taskkill /F /IM ai-producer-hub-backend.exe /T' $0
  ExecWait 'taskkill /F /IM ai-producer-hub-native.exe /T' $0
  !if "${INSTALLMODE}" == "currentUser"
    nsis_tauri_utils::KillProcessCurrentUser "ai-producer-hub-backend.exe"
    Pop $0
    nsis_tauri_utils::KillProcessCurrentUser "ai-producer-hub-native.exe"
    Pop $0
  !else
    nsis_tauri_utils::KillProcess "ai-producer-hub-backend.exe"
    Pop $0
    nsis_tauri_utils::KillProcess "ai-producer-hub-native.exe"
    Pop $0
  !endif
  Sleep 2000
!macroend

!macro NSIS_HOOK_PREINSTALL
  !insertmacro KillAiProducerHubFleetProcesses
!macroend

!macro NSIS_HOOK_PREUNINSTALL
  !insertmacro KillAiProducerHubFleetProcesses
!macroend

!macro NSIS_HOOK_POSTINSTALL
  IfFileExists "$INSTDIR\resources\install-mcp-clients.ps1" 0 mcp_hook_done
    DetailPrint "Optional: register ai-producer-hub in Cursor / Claude Desktop"
    ExecWait 'powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$INSTDIR\resources\install-mcp-clients.ps1" -Interactive'
  mcp_hook_done:
!macroend