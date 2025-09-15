from typing import List, Dict
from langchain.tools import tool
import os

@tool
def make_project_file(project_name: str):
    """Create a project file. It is had to make before start project."""
    os.makedirs(f"output/{project_name}", exist_ok=True)
    #TODO: 악기 결과 파일 저장, 미디 파일 저장, 쓴다면 FLP? 혹은 비숫한 DAW 처럼 스템배치 및 수정 가능한 파일 저장 -> 이거로 최종을 뽑을 수 있으면 좋음