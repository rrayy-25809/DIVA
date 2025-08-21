from langchain_teddynote.tools import GoogleNews
from typing import List, Dict, Annotated
from langchain.tools import tool

# 도구 생성
@tool
def search_news(query: str) -> List[Dict[str, str]]:
    """Search Google News by input keyword"""
    news_tool = GoogleNews()
    return news_tool.search_by_keyword(query, k=5)


if __name__ == "__main__":
    print(f"도구 이름: {search_news.name}")
    print(f"도구 설명: {search_news.description}")
