import { useState } from "react";
import axios from "axios";
import "./index.css";

export default function ChatWidget() {

const [open,setOpen]=useState(false)
const [messages,setMessages]=useState([])
const [input,setInput]=useState("")

const sendMessage=async()=>{

if(!input) return

const userMsg={role:"user",text:input}

setMessages(prev=>[...prev,userMsg])

const res=await axios.post("http://127.0.0.1:8000/chat",{
message:input
})

const botMsg={
role:"bot",
text:res.data.answer
}

setMessages(prev=>[...prev,botMsg])

setInput("")
}

return(

<div>

{/* floating button */}

<button
onClick={()=>setOpen(!open)}
className="fixed bottom-6 right-6 bg-indigo-600 text-white w-14 h-14 rounded-full shadow-lg"
>
💬
</button>

{open && (

<div className="fixed bottom-24 right-6 w-96 h-[600px] bg-white rounded-xl shadow-2xl flex flex-col">

{/* header */}

<div className="bg-indigo-600 text-white p-4 rounded-t-xl flex items-center gap-2">

<img
src="https://img.icons8.com/color/48/artificial-intelligence.png"
className="w-8"
alt="AI Assistant Icon"
/>

<div>

<div className="font-bold">
AI Assistant
</div>

<div className="text-xs">
Online
</div>

</div>

</div>

{/* messages */}

<div className="flex-1 overflow-y-auto p-4 space-y-4">

{messages.map((msg,i)=>(

<div
key={i}
className={msg.role==="user"?"text-right":""}
>

<div
className={
msg.role==="user"
?"inline-block bg-indigo-600 text-white px-4 py-2 rounded-lg"
:"inline-block bg-gray-200 px-4 py-2 rounded-lg"
}
>

{msg.text}

</div>

</div>

))}

</div>

{/* starter prompts */}

<div className="p-2 flex flex-wrap gap-2">

<button
onClick={()=>setInput("Explain your services")}
className="text-xs bg-gray-100 px-2 py-1 rounded"
>
Services
</button>

<button
onClick={()=>setInput("Help me with documentation")}
className="text-xs bg-gray-100 px-2 py-1 rounded"
>
Documentation
</button>

<button
onClick={()=>setInput("How can I use this system")}
className="text-xs bg-gray-100 px-2 py-1 rounded"
>
How it works
</button>

</div>

{/* input */}

<div className="p-3 border-t flex gap-2">

<input
value={input}
onChange={(e)=>setInput(e.target.value)}
placeholder="Type your question..."
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