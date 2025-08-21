from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType


def get_agent(api_key:str, tool_list:list):
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key) # type: ignore

    # Agent 초기화 (ReAct 스타일)
    agent = initialize_agent(
        tool_list,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=5
    )

    return agent

def get_formatted_prompt(prompt: str):
    goal_prompt = PromptTemplate(
        input_variables=["goal"],
        template="""
        너는 사용자의 목표를 달성하기 위해 도구와 지식을 활용하는 지능형 에이전트야.
        목표: {goal}

        주어진 목표를 달성하기 위해 필요한 단계들을 계획하고, 필요한 경우 도구를 호출하여 결과를 도출해라.
        """
    )

    formatted_prompt = goal_prompt.format(goal=prompt)

    return formatted_prompt