import type { ChatMessage } from "../../types/Chat";

interface Props {

    message: ChatMessage;

}

function Message({ message }: Props) {

    return (

        <div
            className={
                message.sender === "user"
                    ? "user-message"
                    : "bot-message"
            }
        >
            {message.text}
        </div>

    );

}

export default Message;