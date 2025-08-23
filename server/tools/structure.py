from typing import Dict
from langchain.tools import tool
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()
GPT_api = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(model="gpt-4o-mini", api_key=GPT_api) # type: ignore

# 자료구조 정의 (pydantic)
class song_structure(BaseModel):
    name: str = Field(description="name of a song that you make structure of, ex) 'Ruin', 'Dreamy'")
    Intro: Dict[str, int | Dict[str, str]] = Field(
        description="Intro part of the song",
        default={"length": 8, "instruments": {"chord":"Piano", "bass":"Reese Bass"}}
    )
    Verse: Dict[str, int | Dict[str, str]] = Field(
        description="Verse part of the song",
        default={"length": 0, "instruments": {"chord":"Piano", "bass":"Reese Bass", "drum":"Break Beat"}}
    )
    Build_Up: Dict[str, int | Dict[str, str]] = Field(
        description="Build Up part of the song",
        default={"length": 8, "instruments": {"melody":"Bell","chord":"Piano", "bass":"Reese Bass", "drum":"KSHMR BuildUp"}}
    )
    Drop: Dict[str, int | Dict[str, str]] = Field(
        description="Drop part of the song",
        default={"length": 16, "instruments": {"melody":"Supersaw Lead","chord":"Supersaw Chord", "bass":"Growl Bass", "drum":"Drop Drum"}}
    )
    Style: Dict[str, float | str] = Field(description="Style of the song")

@tool
def plan_song(song_style: str) -> Dict[str, Dict[str, int | Dict[str, str] | str] | str]:
    """Plan a song structure based on the given style."""

    # 출력 파서 정의
    output_parser = JsonOutputParser(pydantic_object=song_structure)
    format_instructions = output_parser.get_format_instructions()

    # prompt 구성
    prompt = PromptTemplate(
        template="Make Structure of song for user's query\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": format_instructions},
    )

    chain = prompt | model | output_parser
    return chain.invoke({"query": song_style})
    