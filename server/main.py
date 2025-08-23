from flask import Flask, render_template, request, jsonify
from server.tools import get_tools
from server.agent import get_agent, get_formatted_prompt
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()
api_key:str = os.getenv("OPENAI_API_KEY") # type: ignore
agent = get_agent(api_key, get_tools())
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
    prompt = request.form.get('prompt', '') # 어두운 느낌의 퓨처 바운스를 원해
    print(f"Received prompt: {prompt}")  # 디버깅용 로그

    try:
        result = agent.invoke({"input": get_formatted_prompt(prompt, get_tools())})
        return jsonify({"output": result["output"]})
    except Exception as e:
        print(f"Error during agent invocation: {e}")
        return jsonify({"error": str(e)}), 500