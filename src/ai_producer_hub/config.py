"""Sub-server configuration for the audio fleet."""

import os
from dataclasses import dataclass, field


@dataclass
class SubServerConfig:
    songgen_base: str = field(
        default_factory=lambda: os.getenv("SONGGEN_BASE", "http://127.0.0.1:10885")
    )
    vdj_base: str = field(default_factory=lambda: os.getenv("VDJ_BASE", "http://127.0.0.1:10877"))
    reaper_base: str = field(
        default_factory=lambda: os.getenv("REAPER_BASE", "http://127.0.0.1:10797")
    )
    obs_base: str = field(default_factory=lambda: os.getenv("OBS_BASE", "http://127.0.0.1:10819"))
    plex_base: str = field(default_factory=lambda: os.getenv("PLEX_BASE", "http://127.0.0.1:10741"))
    http_host: str = field(default_factory=lambda: os.getenv("HOST", "127.0.0.1"))
    http_port: int = field(default_factory=lambda: int(os.getenv("PORT", "10707")))
