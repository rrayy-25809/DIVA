from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
import langchain
import os

# 기본 변수 설정
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(model="gpt-4o-mini", api_key=api_key)
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
CORS(app)  # 모든 출처 허용. 필요한 경우 특정 도메인만 허용도 가능

@app.route('/generate', methods=['POST'])
def generate_response():
    prompt = request.form.get('prompt', '')
    vocal = request.files.get('vocal')
    if vocal:   # 기타 파일은 클라이언트 단에 맡기기
        Exception("보컬 파일은 아직 지원하지 않습니다.")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')