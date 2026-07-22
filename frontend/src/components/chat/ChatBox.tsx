import type { ChatMessage } from "../../types/Chat";
import Message from "./Message";

interface Props {

    messages: ChatMessage[];

}

function ChatBox({ messages }: Props) {

    return (

        <div className="chat-box">

            {

                messages.map((msg)=>(

                    <Message

                        key={msg.id}

                        message={msg}

                    />

                ))

            }

        </div>

    );

}

export default ChatBox;