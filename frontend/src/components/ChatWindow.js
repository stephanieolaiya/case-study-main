import React, { useState, useEffect, useRef } from "react";
import "./ChatWindow.css";
import { getAIMessage, getContext } from "../api/api";
import { marked } from "marked";
import chatbotIcon from "../img/chatbot_icon.png"
import userIcon from "../img/user_icon.png"

function ChatWindow() {

  const defaultMessage = [{
    role: "assistant",
    content: "Hi, I am intelligent chat agent for ParkSelect who can assist you with information about Refrigerator and Dishwasher parts from our catalog.  How can I help you today?"
  }];

  const [messages, setMessages] = useState(defaultMessage)
  const [input, setInput] = useState("");

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

      // Call API & set assistant message
      const newMessage = await getAIMessage(input, messages);
      setMessages(prevMessages => [...prevMessages, newMessage]);
    }
  };

  // add example questions: 
  // 1 how can I install part number PS2358880
  // 2. what is the cost of part PS304103

  return (
    <div className="messages-container">
      {messages.map((message, index) => (
        <div key={index} className={`${message.role}-message-container`}>
          <div className={`${message.role}-message-group`}>
            <div className="user-circle">
              {message.role == "user" ? <img src={userIcon} alt="chatbot icon"></img>
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
          <div className="example-rectangle">
            How can I install part number PS2358880?
          </div>
          <div className="example-rectangle">
            What is the cost of part PS304103?
          </div>
      </div>

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
