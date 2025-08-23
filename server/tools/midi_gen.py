from typing import List, Dict
from langchain.tools import tool
from HarmonyMIDIToken import HarmonyMIDIToken as Tokenizer
from music21.stream.base import Score
import json

@tool
def generate_midi_data(vector: str) -> Dict[str, int|List[Dict[str, str | float]]]:
    """Generate MIDI data as JSON form Dictionary based on the input style vector."""
    data = '{"BPM": 128, "Melody": [{"note": "E6", "duration": 0.6666666666666666}, {"note": "", "duration": -0.16666666666666663}, {"note": "D6", "duration": 0.25}], "Chord": [{"chord": "CM7", "duration": 0.6666666666666666}, {"chord": "", "duration": -0.16666666666666663}, {"chord": "CM7", "duration": 0.25}], "Bass": [{"note": "C3", "duration": 0.6666666666666666}, {"note": "", "duration": 0.33333333333333337}, {"note": "C3", "duration": 0.25}]}'

    return json.loads(data)

@tool
def get_melody(midi_data: List[Dict[str, str | float]]) -> Score:
    """melody MIDI data to music21 Score"""
    melody = Tokenizer()
    melody.melody = midi_data

    return melody.to_midi()

@tool
def get_drop_chord(midi_data: List[Dict[str, str | float]]) -> Score:
    """Drop chord MIDI data to music21 Score"""
    chord = Tokenizer()
    chord.chords = midi_data

    return chord.to_midi()

@tool
def get_drop_bass(midi_data: List[Dict[str, str | float]]) -> Score:
    """Drop bass MIDI data to music21 Score"""
    bass = Tokenizer()
    bass.bass = midi_data

    return bass.to_midi()

@tool
def get_normal_chord(midi_data: List[Dict[str, str | float]]) -> Score:
    """Drop chord MIDI data to normal chord music21 Score"""
    melody = Tokenizer()
    melody.melody = midi_data

    return melody.to_midi() #TODO: midi data를 normal chord로 변환하는 로직 추가

@tool
def get_normal_bass(midi_data: List[Dict[str, str | float]]) -> Score:
    """Drop bass MIDI data to normal bass music21 Score"""
    bass = Tokenizer()
    bass.bass = midi_data

    return bass.to_midi() #TODO: midi data를 normal bass로 변환하는 로직 추가