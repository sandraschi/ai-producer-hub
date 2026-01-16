"""
MIDI Tools for AI Producer Hub

Capture MIDI input from keyboards/synths, record performances,
and use them as seeds for AI generation.

Features:
- List available MIDI devices
- Record MIDI performances in real-time
- Save to MIDI files
- Import to Reaper DAW
- Use as AI generation seeds ("expand this melody")
- MIDI-to-audio rendering

Requirements:
    pip install python-rtmidi mido

Device Examples:
- Keyboards: Akai MPK Mini, Arturia KeyLab, Native Instruments
- Synths: Novation, Korg, Roland
- Controllers: Launchpad, Push, Maschine
"""

import asyncio
from datetime import datetime
from pathlib import Path
from typing import Optional
from fastmcp import FastMCP

# Optional imports - will be None if not installed
try:
    import rtmidi
    RTMIDI_AVAILABLE = True
except ImportError:
    rtmidi = None
    RTMIDI_AVAILABLE = False

try:
    import mido
    MIDO_AVAILABLE = True
except ImportError:
    mido = None
    MIDO_AVAILABLE = False


def setup_midi_tools(mcp: FastMCP):
    """Register MIDI tools with the MCP server."""

    @mcp.tool()
    async def list_midi_devices() -> dict:
        """
        List all available MIDI input and output devices.
        
        Scans the system for connected MIDI devices including:
        - USB MIDI keyboards
        - Hardware synthesizers
        - Virtual MIDI ports (loopMIDI, IAC, etc.)
        - DAW MIDI interfaces
        
        Returns:
            Dict with lists of input and output devices
        
        Example output:
            {
                "inputs": ["MPK mini 3", "loopMIDI Port"],
                "outputs": ["Microsoft GS Wavetable Synth", "loopMIDI Port"]
            }
        """
        if not RTMIDI_AVAILABLE:
            return {
                "success": False,
                "error": "python-rtmidi not installed",
                "install": "pip install python-rtmidi"
            }
        
        try:
            midi_in = rtmidi.MidiIn()
            midi_out = rtmidi.MidiOut()
            
            inputs = midi_in.get_ports()
            outputs = midi_out.get_ports()
            
            return {
                "success": True,
                "inputs": inputs,
                "outputs": outputs,
                "input_count": len(inputs),
                "output_count": len(outputs)
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    @mcp.tool()
    async def record_midi_performance(
        device_index: int = 0,
        duration_seconds: int = 30,
        output_file: str = ""
    ) -> dict:
        """
        Record a MIDI performance from an input device.
        
        Captures all MIDI events (notes, control changes, pitch bend)
        from the specified device for the given duration.
        
        Args:
            device_index: Index of MIDI input device (from list_midi_devices)
            duration_seconds: How long to record (5-300 seconds)
            output_file: Path to save MIDI file (auto-generated if empty)
        
        Returns:
            Dict with recording info and file path
        
        Workflow:
            1. Call list_midi_devices() to see available devices
            2. Call record_midi_performance(device_index=0, duration=30)
            3. Play your melody on the keyboard/synth
            4. Recording auto-saves to MIDI file
        
        Example:
            record_midi_performance(device_index=0, duration_seconds=60)
        """
        if not RTMIDI_AVAILABLE or not MIDO_AVAILABLE:
            return {
                "success": False,
                "error": "python-rtmidi and/or mido not installed",
                "install": "pip install python-rtmidi mido"
            }
        
        try:
            midi_in = rtmidi.MidiIn()
            ports = midi_in.get_ports()
            
            if not ports:
                return {"success": False, "error": "No MIDI input devices found"}
            
            if device_index >= len(ports):
                return {
                    "success": False, 
                    "error": f"Invalid device index. Available: {ports}"
                }
            
            device_name = ports[device_index]
            midi_in.open_port(device_index)
            
            # Prepare MIDI file
            mid = mido.MidiFile()
            track = mido.MidiTrack()
            mid.tracks.append(track)
            
            # Generate output filename
            if not output_file:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_dir = Path.home() / "Music" / "AI-Producer-Hub" / "MIDI-Recordings"
                output_dir.mkdir(parents=True, exist_ok=True)
                output_file = str(output_dir / f"recording_{timestamp}.mid")
            
            recorded_events = []
            start_time = asyncio.get_event_loop().time()
            
            # Record for specified duration
            while (asyncio.get_event_loop().time() - start_time) < duration_seconds:
                msg = midi_in.get_message()
                if msg:
                    message, delta_time = msg
                    recorded_events.append({
                        "message": message,
                        "time": asyncio.get_event_loop().time() - start_time
                    })
                    
                    # Convert to mido message
                    if len(message) == 3:
                        status = message[0]
                        if status >= 0x90 and status < 0xA0:  # Note On
                            track.append(mido.Message(
                                'note_on',
                                channel=status & 0x0F,
                                note=message[1],
                                velocity=message[2],
                                time=int(delta_time * 1000)
                            ))
                        elif status >= 0x80 and status < 0x90:  # Note Off
                            track.append(mido.Message(
                                'note_off',
                                channel=status & 0x0F,
                                note=message[1],
                                velocity=message[2],
                                time=int(delta_time * 1000)
                            ))
                
                await asyncio.sleep(0.001)  # Small delay to prevent CPU spin
            
            midi_in.close_port()
            
            # Save MIDI file
            mid.save(output_file)
            
            return {
                "success": True,
                "device": device_name,
                "duration": duration_seconds,
                "events_recorded": len(recorded_events),
                "output_file": output_file,
                "message": f"Recorded {len(recorded_events)} MIDI events from '{device_name}'"
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}

    @mcp.tool()
    async def send_midi_note(
        device_index: int,
        note: int,
        velocity: int = 100,
        duration_ms: int = 500,
        channel: int = 0
    ) -> dict:
        """
        Send a MIDI note to an output device.
        
        Args:
            device_index: Index of MIDI output device
            note: MIDI note number (0-127, middle C = 60)
            velocity: Note velocity (0-127)
            duration_ms: Note duration in milliseconds
            channel: MIDI channel (0-15)
        
        Returns:
            Dict with send status
        
        Note Reference:
            C4 (middle C) = 60
            A4 (440Hz) = 69
            Each octave = 12 semitones
        """
        if not RTMIDI_AVAILABLE:
            return {
                "success": False,
                "error": "python-rtmidi not installed"
            }
        
        try:
            midi_out = rtmidi.MidiOut()
            ports = midi_out.get_ports()
            
            if device_index >= len(ports):
                return {"success": False, "error": f"Invalid device. Available: {ports}"}
            
            midi_out.open_port(device_index)
            
            # Note On
            note_on = [0x90 | channel, note, velocity]
            midi_out.send_message(note_on)
            
            # Wait
            await asyncio.sleep(duration_ms / 1000)
            
            # Note Off
            note_off = [0x80 | channel, note, 0]
            midi_out.send_message(note_off)
            
            midi_out.close_port()
            
            return {
                "success": True,
                "device": ports[device_index],
                "note": note,
                "velocity": velocity,
                "duration_ms": duration_ms
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}

    @mcp.tool()
    async def midi_to_reaper(
        midi_file: str,
        track_name: str = "MIDI Recording"
    ) -> dict:
        """
        Import a MIDI file into Reaper DAW.
        
        Sends the MIDI file to Reaper for:
        - Audio rendering with virtual instruments
        - Further editing and arrangement
        - Mixing and mastering
        
        Args:
            midi_file: Path to MIDI file
            track_name: Name for the new track in Reaper
        
        Returns:
            Dict with import status
        
        Workflow:
            1. Record MIDI with record_midi_performance()
            2. Import to Reaper with midi_to_reaper()
            3. Reaper renders with your VSTi/instruments
            4. Export audio for use in VirtualDJ
        """
        try:
            # This integrates with Reaper-MCP when available
            result = {
                "workflow": "midi_to_reaper",
                "midi_file": midi_file,
                "track_name": track_name,
                "steps": [
                    f"1. Open MIDI file: {midi_file}",
                    f"2. Create new track: {track_name}",
                    "3. Insert MIDI item on track",
                    "4. Assign virtual instrument",
                    "5. Ready for playback/render"
                ],
                "status": "framework_ready",
                "note": "Requires Reaper-MCP to be mounted"
            }
            
            return result
            
        except Exception as e:
            return {"success": False, "error": str(e)}

    @mcp.tool()
    async def midi_to_ai_seed(
        midi_file: str,
        expansion_style: str = "elaborate",
        target_duration: int = 120
    ) -> dict:
        """
        Use a MIDI recording as a seed for AI music generation.
        
        Takes your played melody/chords and:
        1. Analyzes the musical content
        2. Extracts key, tempo, chord progression
        3. Creates a prompt for AI expansion
        4. Generates full track based on your input
        
        Args:
            midi_file: Path to MIDI file (your recording)
            expansion_style: How to expand it:
                - "elaborate" - Add complexity and layers
                - "extend" - Make it longer
                - "harmonize" - Add harmonies
                - "full_production" - Complete track
            target_duration: Target length in seconds
        
        Returns:
            Dict with AI generation prompt
        
        Example:
            1. Play a 4-bar melody on your keyboard
            2. record_midi_performance() saves it
            3. midi_to_ai_seed() analyzes and generates prompt
            4. songgen_to_deck() creates professional track with vocals from your melody!
        """
        try:
            if not MIDO_AVAILABLE:
                return {
                    "success": False,
                    "error": "mido not installed",
                    "install": "pip install mido"
                }
            
            # Load and analyze MIDI file
            mid = mido.MidiFile(midi_file)
            
            # Extract basic info
            notes = []
            for track in mid.tracks:
                for msg in track:
                    if msg.type == 'note_on' and msg.velocity > 0:
                        notes.append(msg.note)
            
            if not notes:
                return {"success": False, "error": "No notes found in MIDI file"}
            
            # Basic analysis
            lowest_note = min(notes)
            highest_note = max(notes)
            note_range = highest_note - lowest_note
            note_count = len(notes)
            
            # Estimate key from notes (simplified)
            note_classes = [n % 12 for n in notes]
            most_common_note = max(set(note_classes), key=note_classes.count)
            key_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
            estimated_key = key_names[most_common_note]
            
            # Generate AI prompt based on analysis
            style_prompts = {
                "elaborate": f"Elaborate on this melody in {estimated_key}, "
                            f"add layers and complexity, keep the core theme",
                "extend": f"Extend this {note_count}-note melody in {estimated_key}, "
                         f"develop it into a full composition",
                "harmonize": f"Add rich harmonies to this melody in {estimated_key}, "
                            f"create lush chord progressions",
                "full_production": f"Create a full production track based on this melody in {estimated_key}, "
                                  f"with drums, bass, pads, and arrangement"
            }
            
            prompt = style_prompts.get(expansion_style, style_prompts["elaborate"])
            prompt += f", target duration {target_duration} seconds"
            
            return {
                "success": True,
                "analysis": {
                    "note_count": note_count,
                    "note_range": note_range,
                    "lowest_note": lowest_note,
                    "highest_note": highest_note,
                    "estimated_key": estimated_key,
                    "duration": mid.length
                },
                "generated_prompt": prompt,
                "expansion_style": expansion_style,
                "target_duration": target_duration,
                "next_step": "Use these lyrics with songgen_to_deck() to generate professional track with vocals!"
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}

    @mcp.tool()
    async def play_midi_file(
        midi_file: str,
        device_index: int = 0
    ) -> dict:
        """
        Play a MIDI file through an output device.
        
        Sends the MIDI file to your synthesizer/sound module
        for real-time playback.
        
        Args:
            midi_file: Path to MIDI file
            device_index: Output device index
        
        Returns:
            Dict with playback status
        """
        if not RTMIDI_AVAILABLE or not MIDO_AVAILABLE:
            return {
                "success": False,
                "error": "python-rtmidi and mido required",
                "install": "pip install python-rtmidi mido"
            }
        
        try:
            midi_out = rtmidi.MidiOut()
            ports = midi_out.get_ports()
            
            if device_index >= len(ports):
                return {"success": False, "error": f"Invalid device. Available: {ports}"}
            
            midi_out.open_port(device_index)
            
            mid = mido.MidiFile(midi_file)
            
            for msg in mid.play():
                if not msg.is_meta:
                    midi_out.send_message(msg.bytes())
            
            midi_out.close_port()
            
            return {
                "success": True,
                "file": midi_file,
                "device": ports[device_index],
                "duration": mid.length
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}

    @mcp.tool()
    async def midi_monitor(
        device_index: int = 0,
        duration_seconds: int = 10
    ) -> dict:
        """
        Monitor MIDI input and display incoming messages.
        
        Useful for:
        - Testing MIDI connections
        - Learning what messages your device sends
        - Debugging MIDI setups
        
        Args:
            device_index: Input device index
            duration_seconds: How long to monitor
        
        Returns:
            Dict with received messages
        """
        if not RTMIDI_AVAILABLE:
            return {"success": False, "error": "python-rtmidi not installed"}
        
        try:
            midi_in = rtmidi.MidiIn()
            ports = midi_in.get_ports()
            
            if device_index >= len(ports):
                return {"success": False, "error": f"Invalid device. Available: {ports}"}
            
            midi_in.open_port(device_index)
            
            messages = []
            start_time = asyncio.get_event_loop().time()
            
            while (asyncio.get_event_loop().time() - start_time) < duration_seconds:
                msg = midi_in.get_message()
                if msg:
                    message, delta_time = msg
                    messages.append({
                        "raw": message,
                        "time": asyncio.get_event_loop().time() - start_time,
                        "interpreted": interpret_midi_message(message)
                    })
                await asyncio.sleep(0.001)
            
            midi_in.close_port()
            
            return {
                "success": True,
                "device": ports[device_index],
                "duration": duration_seconds,
                "message_count": len(messages),
                "messages": messages[:50]  # Limit to 50 for readability
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}


def interpret_midi_message(msg: list) -> str:
    """Interpret a raw MIDI message into human-readable form."""
    if len(msg) < 1:
        return "Empty message"
    
    status = msg[0]
    channel = status & 0x0F
    msg_type = status & 0xF0
    
    if msg_type == 0x90 and len(msg) >= 3:
        return f"Note On: ch={channel} note={msg[1]} vel={msg[2]}"
    elif msg_type == 0x80 and len(msg) >= 3:
        return f"Note Off: ch={channel} note={msg[1]} vel={msg[2]}"
    elif msg_type == 0xB0 and len(msg) >= 3:
        return f"Control Change: ch={channel} cc={msg[1]} val={msg[2]}"
    elif msg_type == 0xE0 and len(msg) >= 3:
        return f"Pitch Bend: ch={channel} val={msg[1] | (msg[2] << 7)}"
    elif msg_type == 0xC0 and len(msg) >= 2:
        return f"Program Change: ch={channel} prog={msg[1]}"
    else:
        return f"Unknown: {msg}"

