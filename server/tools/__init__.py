from langchain.tools import BaseTool

from server.tools.test import search_news
from .structure import plan_song
from .midi_gen import (
    generate_midi_data,
    get_melody, get_drop_chord,
    get_drop_bass,
    get_normal_chord,
    get_normal_bass
)
from .save import make_project_file

def get_tools():
    return [
        value for value in globals().values()
        if isinstance(value, BaseTool)
    ]

if __name__ == "__main__":
    for tool in get_tools():
        print(f"도구 이름 {tool.name}")