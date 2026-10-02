# Per-repo fleet start config for ai-producer-hub
# Edit ports/backend target here - start.ps1 is fleet-standard.
@{
    Name         = 'ai-producer-hub'
    BackendPort  = 11171
    FrontendPort = 10707
    HealthPath   = '/health'
    WebRoot      = 'webapp'
    Backend = @{
        Kind       = 'module-serve'
        Module     = 'ai_producer_hub'
        ServeArgs  = @('--serve', '--port', '11171')
        SyncExtras = @('dev')
    }
    Frontend = @{
        Kind           = 'vite-npm'
        PackageManager = 'npm'
        PortEnvVar     = 'VITE_PORT'
        ApiTargetEnv   = 'VITE_API_TARGET'
    }
}
