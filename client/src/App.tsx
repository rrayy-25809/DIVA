import { Button, Form, InputGroup } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
    return (
        <div>
            <header>뽀로로와 대화해요~</header>
            <div id="chat-container"></div>
            <InputGroup className="mb-3">
                <Form.Control
                    placeholder="Recipient's username"
                    aria-label="Recipient's username"
                    aria-describedby="basic-addon2"
                />
                <Button variant="outline-secondary" id="button-addon2">
                    Button
                </Button>
            </InputGroup>
        </div>
    )
}

export default App;