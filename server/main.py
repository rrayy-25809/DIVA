from flask import Flask, render_template, request, jsonify
from langchain.agents import initialize_agent, AgentType
from tools import search_news, python_repl_tool
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from flask_cors import CORS
import os

# 기본 변수 설정
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key) # type: ignore
app = Flask(__name__, template_folder='../dist/client', static_folder='../dist/assets')
app.secret_key = os.getenv("FLASK_SECRET_KEY")
CORS(app)  # 모든 출처 허용. 필요한 경우 특정 도메인만 허용도 가능

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path): # type: ignore
        return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate_response():
    prompt = request.form.get('prompt', '')
    tool_list = [search_news, python_repl_tool]

    # Agent 초기화 (ReAct 스타일)
    agent = initialize_agent(
        tool_list,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=5
    )

    goal_prompt = PromptTemplate(
        input_variables=["goal"],
        template="""
        너는 사용자의 목표를 달성하기 위해 도구와 지식을 활용하는 지능형 에이전트야.
        목표: {goal}

        주어진 목표를 달성하기 위해 필요한 단계들을 계획하고, 필요한 경우 도구를 호출하여 결과를 도출해라.
        """
    )

    try:
        result = agent.invoke({"input": prompt})
        return jsonify({"output": result["output"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
