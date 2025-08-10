from flask import Flask, render_template, request, jsonify
from langchain.agents import create_tool_calling_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from flask_cors import CORS
from tools import test
import os

# 기본 변수 설정
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(model="gpt-4o-mini", api_key=api_key) # type: ignore
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
    tool_list = [test.search_news, test.python_repl_tool]

    return ":", 200
