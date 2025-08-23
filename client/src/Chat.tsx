interface ChatProps {
    content: string;
    type: string;
}

function Chat({content, type}: ChatProps) {
    return (
        <div className={`message ${type}`}>
            <span>{content}</span>
        </div>
    )
}

export default Chat;