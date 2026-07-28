"""HTTP client for the audio fleet sub-servers."""

import logging
from typing import Any

import httpx

from .config import SubServerConfig

logger = logging.getLogger(__name__)


class FleetClient:
    def __init__(self, cfg: SubServerConfig):
        self.cfg = cfg
        self._client = httpx.AsyncClient(timeout=60.0)

    async def close(self):
        await self._client.aclose()

    # --- songgeneration-mcp ---

    async def songgen_generate(
        self,
        lyrics: str,
        genre: str = "Pop",
        mood: str = "Happy",
        tempo: int = 120,
        voice: str = "Female",
        title: str | None = None,
    ) -> dict[str, Any]:
        payload = {
            "lyrics": lyrics,
            "genre": genre,
            "mood": mood,
            "tempo": tempo,
            "voice": voice,
            "separate_stems": True,
        }
        if title:
            payload["title"] = title
        r = await self._client.post(f"{self.cfg.songgen_base}/api/generate", json=payload)
        r.raise_for_status()
        return r.json()

    async def songgen_status(self) -> dict[str, Any]:
        r = await self._client.get(f"{self.cfg.songgen_base}/api/studio/status")
        r.raise_for_status()
        return r.json()

    async def songgen_export_vdj(
        self, repo_id: str, deck: int = 1, load: bool = True, play: bool = False
    ) -> dict[str, Any]:
        r = await self._client.post(
            f"{self.cfg.songgen_base}/api/export/virtualdj",
            json={"repo_id": repo_id, "deck": deck, "load": load, "play": play},
        )
        r.raise_for_status()
        return r.json()

    async def songgen_export_plex(self, repo_id: str) -> dict[str, Any]:
        r = await self._client.post(
            f"{self.cfg.songgen_base}/api/export/plex", json={"repo_id": repo_id}
        )
        r.raise_for_status()
        return r.json()

    async def songgen_export_reaper(self, repo_id: str) -> dict[str, Any]:
        r = await self._client.post(
            f"{self.cfg.songgen_base}/api/export/reaper", json={"repo_id": repo_id}
        )
        r.raise_for_status()
        return r.json()

    async def songgen_list_songs(self) -> list[dict[str, Any]]:
        r = await self._client.get(f"{self.cfg.songgen_base}/api/songs")
        r.raise_for_status()
        data = r.json()
        return data if isinstance(data, list) else data.get("songs", [])

    # --- virtualdj-mcp REST API ---

    async def vdj_health(self) -> dict[str, Any]:
        r = await self._client.get(f"{self.cfg.vdj_base}/api/v1/health")
        r.raise_for_status()
        return r.json()

    async def vdj_deck_status(self, deck_id: int = 1) -> dict[str, Any]:
        r = await self._client.get(f"{self.cfg.vdj_base}/api/v1/deck/{deck_id}/status")
        r.raise_for_status()
        return r.json()

    async def vdj_deck_load(self, deck_id: int, track_path: str) -> dict[str, Any]:
        r = await self._client.post(
            f"{self.cfg.vdj_base}/api/v1/deck/{deck_id}/load", json={"track_path": track_path}
        )
        r.raise_for_status()
        return r.json()

    async def vdj_deck_play(self, deck_id: int = 1) -> dict[str, Any]:
        r = await self._client.post(
            f"{self.cfg.vdj_base}/api/v1/deck/{deck_id}/play_pause", json={}
        )
        r.raise_for_status()
        return r.json()

    async def vdj_deck_sync(self, deck_id: int = 1) -> dict[str, Any]:
        r = await self._client.post(f"{self.cfg.vdj_base}/api/v1/deck/{deck_id}/sync", json={})
        r.raise_for_status()
        return r.json()

    async def vdj_library_search(self, query: str, limit: int = 20) -> dict[str, Any]:
        r = await self._client.post(
            f"{self.cfg.vdj_base}/api/v1/library/search", json={"query": query, "limit": limit}
        )
        r.raise_for_status()
        return r.json()

    async def vdj_analyze(self, track_path: str) -> dict[str, Any]:
        r = await self._client.post(
            f"{self.cfg.vdj_base}/api/v1/audio/analyze", json={"track_path": track_path}
        )
        r.raise_for_status()
        return r.json()

    # --- reaper-mcp health ---

    async def reaper_health(self) -> dict[str, Any]:
        try:
            r = await self._client.get(f"{self.cfg.reaper_base}/health", timeout=5.0)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            return {"ok": False, "error": str(e)}

    # --- obs-mcp health ---

    async def obs_health(self) -> dict[str, Any]:
        try:
            r = await self._client.get(f"{self.cfg.obs_base}/health", timeout=5.0)
            r.raise_for_status()
            return r.json()
        except Exception as e:
            return {"ok": False, "error": str(e)}

    async def check_all_health(self) -> dict[str, Any]:
        results = {}
        for name, url in [
            ("songgeneration", self.cfg.songgen_base),
            ("virtualdj", self.cfg.vdj_base),
            ("reaper", self.cfg.reaper_base),
            ("obs", self.cfg.obs_base),
        ]:
            try:
                r = await self._client.get(f"{url}/health", timeout=5.0)
                results[name] = {"ok": r.status_code == 200}
            except Exception as e:
                results[name] = {"ok": False, "error": str(e)}
        return results
