interface Props {

    value:string;

    onChange:(value:string)=>void;

    onSend:()=>void;

}

function ChatInput({

    value,

    onChange,

    onSend

}:Props){

    return(

        <div className="input-area">

            <input

                value={value}

                onChange={(e)=>onChange(e.target.value)}

                placeholder="Ask anything..."

            />

            <button

                onClick={onSend}

            >

                Send

            </button>

        </div>

    );

}

export default ChatInput;