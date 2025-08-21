from langchain_experimental.utilities import PythonREPL
from langchain_teddynote.tools import GoogleNews
from typing import List, Dict, Annotated
from langchain.tools import tool

# 도구 생성
@tool
def search_news(query: str) -> List[Dict[str, str]]:
    """Search Google News by input keyword"""
    news_tool = GoogleNews()
    return news_tool.search_by_keyword(query, k=5)


# 도구 생성
@tool
def python_repl_tool(
    code: Annotated[str, "The python code to execute to generate your chart."],
):
    """Use this to execute python code. If you want to see the output of a value,
    you should print it out with `print(...)`. This is visible to the user."""
    result = ""
    try:
        result = PythonREPL().run(code)
    except BaseException as e:
        print(f"Failed to execute. Error: {repr(e)}")
    finally:
        return result

if __name__ == "__main__":
    print(f"도구 이름: {search_news.name}")
    print(f"도구 설명: {search_news.description}")
    print(f"도구 이름: {python_repl_tool.name}")
    print(f"도구 설명: {python_repl_tool.description}")
