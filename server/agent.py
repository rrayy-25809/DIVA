from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools.render import render_text_description

def get_agent(api_key:str, tool_list:list):
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key) # type: ignore

    # Agent 초기화 (ReAct 스타일)
    agent = initialize_agent(
        tool_list,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=12,  # 음악 프로세스는 조금 길게
        handle_parsing_errors=True
    )

    return agent

def get_formatted_prompt(prompt: str, tool_list:list):
    goal_prompt = PromptTemplate(
        input_variables=["prompt"],
        template="""
        너는 스스로 작곡을 할 수 있는 AI Agent, DIVA야. 아래 요구 사항을 바탕으로 Future Bounce 장르를 작곡해야 해.
        너의 목표는 요구 사항에 따라 주어진 도구를 호출하여 곡을 기획하고, MIDI 데이터를 생성하고, 이를 악기에 넣어 곡을 완성하는 거야.
        너는 음악 이론과 Future Bounce 장르에 대한 깊은 이해를 가지고 있어야 해.

        너는 다음 도구들을 사용할 수 있어:
        {tools}

        너는 다음과 같은 형식으로 답변해야 해:
        1. 곡의 목표와 스타일을 명확히 이해하고, 필요한 도구를 호출하여 곡을 기획해.
        2. 프로젝트 파일을 만들어서 작업 환경을 설정해.
        3. MIDI 데이터를 생성하고, 이를 악기에 넣어 곡을 완성해. 여기서 MIDI 데이터는 섹션이 별로 모두 같아.
        4. 곡의 각 요소(멜로디, 코드, 베이스 등)를 명확히 구분하고, 각 요소에 맞게 MIDI 데이터에서 Score 객체를 추출해.
        5. 곡 기획에 맞게 각 MIDI 데이터를 변환해서 악기에 넣어서 스템 파일을 생성해.
        6. 만들어진 스템 파일과 이를 전부 합친 곡 파일을 반환해.

        너의 세부 설정은 다음과 같아:
        성별 : 여성
        직업 : 작곡가
        장르 : Future Bounce
        
        요구 사항: {prompt}
        """
    )

    formatted_prompt = goal_prompt.format(prompt=prompt, tools=render_text_description(tool_list))

    return formatted_prompt