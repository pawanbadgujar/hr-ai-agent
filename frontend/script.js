const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

const API_URL = "http://127.0.0.1:8000/chat/?query=";

function appendMessage(message, sender) {

    const div = document.createElement("div");

    div.className = `message ${sender}`;

    div.innerHTML = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {

    const message = input.value.trim();

    if (!message) return;

    appendMessage(message, "user");

    input.value = "";

    const loading = document.createElement("div");

    loading.className = "message bot loading";

    loading.innerHTML = "Typing...";

    chatBox.appendChild(loading);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch(
            API_URL + encodeURIComponent(message),
            {
                method: "POST"
            }
        );

        loading.remove();

        if (!response.ok) {

            appendMessage("Server Error.", "bot");

            return;
        }

        const data = await response.json();

        appendMessage(data.answer, "bot");

    }

    catch (error) {

        loading.remove();

        appendMessage("Unable to connect to server.", "bot");

        console.error(error);
    }

}

sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {

        sendMessage();
    }

});