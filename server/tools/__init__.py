#from tools.test import search_news
from structure import plan_song
from midi_gen import (
    generate_midi_data,
    get_melody, get_drop_chord,
    get_drop_bass,
    get_normal_chord,
    get_normal_bass
)
from save import make_project_file

def get_tools():
    return [
        value for value in globals().values()
        if callable(value) and not getattr(value, "__name__", "").startswith('_')
    ]

if __name__ == "__main__":

    print(get_tools())

    for tool in get_tools():
        print(f"도구 이름 {tool.name}")