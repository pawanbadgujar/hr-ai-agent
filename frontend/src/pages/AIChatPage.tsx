import { useState } from "react";

import Layout from "../components/Layout";
import Header from "../components/Header";
import Sidebar from "../components/Sidebar";

import ChatBox from "../components/chat/ChatBox";
import ChatInput from "../components/chat/ChatInput";

import { sendMessage } from "../services/ChatService";

import type { ChatMessage } from "../types/Chat";

function AIChatPage() {

    const [messages, setMessages] = useState<ChatMessage[]>([
        {
            id: 1,
            sender: "bot",
            text: "👋 Hello! Ask me anything about Leave, Payroll, Jobs or Workforce."
        }
    ]);

    const [input, setInput] = useState("");

    async function handleSend() {

        if (input.trim() === "") return;

        const userMessage: ChatMessage = {
            id: Date.now(),
            sender: "user",
            text: input
        };

        setMessages(prev => [...prev, userMessage]);

        const question = input;

        setInput("");

        try {

            const response = await sendMessage(question);

            const botMessage: ChatMessage = {

                id: Date.now() + 1,

                sender: "bot",

                text: response.answer

            };

            setMessages(prev => [...prev, botMessage]);

        }

        catch (error) {

            const botMessage: ChatMessage = {

                id: Date.now(),

                sender: "bot",

                text: "❌ Unable to connect with AI Server."

            };

            setMessages(prev => [...prev, botMessage]);

            console.error(error);

        }

    }

    return (

        <Layout>

            <Header />

            <div className="app-container">

                <Sidebar />

                <main className="dashboard">

                    <ChatBox messages={messages} />

                    <ChatInput
                        value={input}
                        onChange={setInput}
                        onSend={handleSend}
                    />

                </main>

            </div>

        </Layout>

    );

}

export default AIChatPage;