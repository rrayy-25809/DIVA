from typing import List, Dict
from langchain.tools import tool
from HarmonyMIDIToken import HarmonyMIDIToken as Tokenizer
from music21.stream.base import Score
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
import pandas as pd
import torch
import io
import requests
import json

def get_model():
    # .pt 파일 경로 - 모델 경로에 따라 수정 필요
    url = "https://huggingface.co/<username>/<repo>/resolve/main/your_model.pt"

    # 인증이 필요한 경우
    # headers = {"Authorization": f"Bearer hf_your_token"}
    # response = requests.get(url, headers=headers)

    # 공개 모델이면 헤더 없이 가능
    response = requests.get(url)

    # 메모리 버퍼로 읽기
    buffer = io.BytesIO(response.content)

    # 모델 로드 - 저장 방식에 따라 아래 중 하나 사용
    # 1. 전체 모델이 저장된 경우
    model = torch.load(buffer, map_location='cpu')

def data_to_tensor(data:pd.DataFrame):
    # 전처리 파이프라인
    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(sparse_output=False), ["mode", "mood", "key"]),
        ("num", MinMaxScaler(), ["bpm", "chord_complexity", "melody_density", "syncopation", "pitch_range"])
    ])

    X = preprocessor.transform(data)

    return torch.tensor(X, dtype=torch.float32)

@tool
def generate_midi_data(vector: str) -> Dict[str, int|List[Dict[str, str | float]]]:
    """Generate MIDI data as JSON form Dictionary based on the input style vector."""
    device = torch.device('cuda')

    model = torch.load('model/DIVA_Model_full.pt', map_location=device)
    data = pd.DataFrame([json.loads(vector)])
    X = data_to_tensor(data).to(device)
    
    model.generate(X[0], device=device)

    return 

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