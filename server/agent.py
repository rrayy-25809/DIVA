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
        input_variables=["prompt"],
        template="""
        너는 스스로 작곡을 할 수 있는 AI Agent, DIVA야. 아래 요구 사항을 바탕으로 Future Bounce 장르를 작곡해야 해
        주어진 목표를 달성하기 위해 필요한 단계들을 계획하고, 필요한 경우 도구를 호출하여 결과를 도출해라.
        
        요구 사항: {prompt}
        """
    )

    formatted_prompt = goal_prompt.format(goal=prompt)

    return formatted_prompt