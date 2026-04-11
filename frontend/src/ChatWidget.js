import { useState } from "react";
import axios from "axios";
import "./index.css";

export default function ChatWidget() {

  const [open,setOpen]=useState(false)
  const [messages,setMessages]=useState([])
  const [input,setInput]=useState("")
  const [loading, setLoading] = useState(false);

 const sendMessage = async () => {
  if (!input) return;

  const userMsg = { role: "user", text: input };
  setMessages((prev) => [...prev, userMsg]);
  setInput("");
  setLoading(true);

  try {
    const API_URL = "https://ai-rag-chatbot-euw3.onrender.com";

    const res = await axios.post(
      `${API_URL}/chat`,
      { message: userMsg.text }
    );

    setMessages((prev) => [
      ...prev,
      { role: "bot", text: res.data.answer }
    ]);

  } catch (err) {
    setMessages((prev) => [
      ...prev,
      { role: "bot", text: "⚠️ Server error" }
    ]);
  }

  setLoading(false);
};

  return(
    <div>

      <button
        onClick={()=>setOpen(!open)}
        className="fixed bottom-6 right-6 bg-indigo-600 text-white w-14 h-14 rounded-full shadow-lg"
      >
        💬
      </button>

      {open && (
        <div className="fixed bottom-24 right-6 w-96 h-[600px] bg-white rounded-xl shadow-2xl flex flex-col">

          <div className="bg-indigo-600 text-white p-4 rounded-t-xl">
            AI Assistant
          </div>

          <div className="flex-1 overflow-y-auto p-4 space-y-4">

            {messages.map((msg,i)=>(
              <div key={i} className={msg.role==="user"?"text-right":""}>
                <div className={
                  msg.role==="user"
                  ?"inline-block bg-indigo-600 text-white px-4 py-2 rounded-lg"
                  :"inline-block bg-gray-200 px-4 py-2 rounded-lg"
                }>
                  {msg.text}
                </div>
              </div>
            ))}

            {loading && (
              <div className="text-left">
                <div className="inline-block bg-gray-200 px-4 py-2 rounded-lg">
                  Typing...
                </div>
              </div>
            )}

          </div>

          <div className="p-3 border-t flex gap-2">

            <input
              value={input}
              onChange={(e)=>setInput(e.target.value)}
              className="flex-1 border rounded px-3 py-2"
            />

            <button
              onClick={sendMessage}
              className="bg-indigo-600 text-white px-4 py-2 rounded"
            >
              Send
            </button>

          </div>

        </div>
      )}

    </div>
  )
}