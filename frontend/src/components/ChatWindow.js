import React, { useState, useEffect, useRef } from "react";
import "./ChatWindow.css";
import { getAIMessage } from "../api/api";
import { marked } from "marked";
import chatbotIcon from "../img/chatbot_icon.png"
import userIcon from "../img/user_icon.png"
import { ClipLoader } from "react-spinners";


function ChatWindow() {

  const defaultMessage = [{
    role: "assistant",
    content: `Hi, I am intelligent chat agent for ParkSelect who can assist you with information about Refrigerator and Dishwasher parts from our catalog. I can answer questions about:

    1. Popular model and product compatibility
    2. Installation of parts
    3. Descriptions and Prices of Parts 
    4. Common issues with products and how to fix them.
  
    How can I help you today?`
  }];

  const [messages, setMessages] = useState(defaultMessage)
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async (input) => {
    if (input.trim() !== "") {
      // Set user message
      setMessages(prevMessages => [...prevMessages, { role: "user", content: input }]);
      setInput("");
      setLoading(true)

      // Call API & set assistant message
      const newMessage = await getAIMessage(input, messages);
      setLoading(false)
      setMessages(prevMessages => [...prevMessages, newMessage]);
    }
  };


  return (
    <div className="messages-container">
      {messages.map((message, index) => (
        <div key={index} className={`${message.role}-message-container`}>
          <div className={`${message.role}-message-group`}>
            <div className="user-circle">
              {message.role === "user" ? <img src={userIcon} alt="chatbot icon"></img>
              :  <img src={chatbotIcon} alt="chatbot icon"></img>}
             
            </div>
            {message.content && (
              <div className={`message ${message.role}-message`}>
                <div dangerouslySetInnerHTML={{ __html: marked(message.content).replace(/<p>|<\/p>/g, "") }}></div>
              </div>
            )}
          </div>
        </div>
      ))}
      <div ref={messagesEndRef} />
      <div className="example-questions">
          <p><strong>Example questions:</strong></p>
          <div className="example-rectangle" onClick={() => {handleSend("How can I install refrigerator part PS2358880?")}}>
            How can I install refrigerator part PS2358880?
          </div>
          <div className="example-rectangle" onClick={() => {handleSend(" What is the cost of refrigerator part PS304103?")}}>
            What is the cost of part PS304103?
          </div>
          <div className="example-rectangle" onClick={() => {handleSend("What evaporator fan motor is compatible with refrigerator model GTH18GBDCRWW?")}}>
            What evaporator fan motor is compatible with refrigerator model GTH18GBDCRWW?
          </div>
          <div className="example-rectangle" onClick={() => {handleSend("What evaporator fan motor is compatible with refrigerator model GTH18GBDCRWW?")}}>
            How can I fix my noisy dishwasher?
          </div>
      </div>
      {loading && <div style={{display:"flex", justifyContent:'center'}}>
        <ClipLoader
          aria-label="Loading Spinner"
          data-testid="loader"
        />
      </div>}
      <div className="input-area">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
          onKeyPress={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              handleSend(input);
              e.preventDefault();
            }
          }}
          rows="3"
        />
        <button className="send-button" onClick={handleSend}>
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatWindow;
