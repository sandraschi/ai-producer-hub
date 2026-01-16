"""Tests for AI Producer Hub server."""

import pytest


def test_imports():
    """Test that main modules can be imported."""
    from ai_producer_hub import server
    assert hasattr(server, 'mcp')
    assert hasattr(server, 'main')


def test_mcp_instance():
    """Test that MCP instance is properly configured."""
    from ai_producer_hub.server import mcp
    assert mcp.name == "AI-Producer-Hub"


def test_tools_registered():
    """Test that workflow tools are defined."""
    from ai_producer_hub import server
    
    # Check workflow functions exist
    assert hasattr(server, 'songgen_to_deck')
    assert hasattr(server, 'ai_dj_set')
    assert hasattr(server, 'remix_plex_track')
    assert hasattr(server, 'bpm_bridge_generator')
    assert hasattr(server, 'live_stream_producer')
    assert hasattr(server, 'album_factory')
    assert hasattr(server, 'karaoke_generator')
    assert hasattr(server, 'ai_mashup')
    assert hasattr(server, 'hub_status')
    assert hasattr(server, 'producer_help')


@pytest.mark.asyncio
async def test_hub_status():
    """Test hub_status returns expected structure."""
    from ai_producer_hub.server import hub_status
    
    result = await hub_status()
    
    assert "hub_name" in result
    assert result["hub_name"] == "AI-Producer-Hub"
    assert "workflows" in result
    assert "capabilities" in result


@pytest.mark.asyncio
async def test_producer_help():
    """Test producer_help returns help text."""
    from ai_producer_hub.server import producer_help
    
    result = await producer_help("overview")
    
    assert isinstance(result, str)
    assert "AI Producer Hub" in result


@pytest.mark.asyncio
async def test_songgen_to_deck_framework():
    """Test songgen_to_deck returns framework response."""
    from ai_producer_hub.server import songgen_to_deck

    result = await songgen_to_deck(
        lyrics="test lyrics",
        genre="Electronic",
        deck_id=1
    )

    assert "workflow" in result
    assert result["workflow"] == "songgen_to_deck"
    assert "lyrics_preview" in result


@pytest.mark.asyncio
async def test_ai_dj_set_framework():
    """Test ai_dj_set returns framework response."""
    from ai_producer_hub.server import ai_dj_set
    
    result = await ai_dj_set("test theme", num_tracks=4)
    
    assert "workflow" in result
    assert result["workflow"] == "ai_dj_set"
    assert "prompts" in result
    assert len(result["prompts"]) == 4

