import { useState } from 'react';
import { Button, Form, InputGroup } from 'react-bootstrap';
import Chat from './Chat';

function App() {
    const [prompt, setPrompt] = useState('');

    return (
        <div className="App">
            <header>Diva - 인공지능 작곡가</header>
            <div id="chat-container">
                <Chat content="안녕하세요! 저는 DIVA입니다. 어떤 곡을 작곡해 드릴까요?" type="bot" />
                <Chat content="안녕" type="user" />
            </div>
            <InputGroup className="mb-3">
                <Form.Control
                    placeholder="원하는 곡의 요구 사항을 입력하세요"
                    aria-label="prompt"
                    aria-describedby="basic-addon2"
                    value={prompt}
                    onChange={e => setPrompt(e.target.value)}
                />
                <Button variant="outline-secondary" id="button-addon2" onClick={() => {
                    send(prompt)
                    setPrompt(''); // 메시지 전송 후 입력 필드 비우기
                    }}>
                    전송
                </Button>
            </InputGroup>
        </div>
    )
}

async function send(prompt: string) {
    const formData = new FormData(); // 폼 데이터 객체 생성 (파일 업로드나 POST 요청에 사용)
    formData.append("prompt", prompt); // 폼 데이터에 사용자 입력 추가
    
    const response = await fetch("/generate", { // 서버에 POST 요청 (비동기)
        method: "POST", // HTTP 메서드 지정
        body: formData, // 요청 본문에 폼 데이터 포함
    });

    if (response.ok) { // 응답이 성공적이면
        const json = await response.json(); // 응답을 JSON으로 파싱 (비동기)
        console.log(json); // 콘솔에 응답 내용 출력
    }
}

export default App;