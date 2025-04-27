import React, { useState } from "react";
import "./App.css";
import ChatWindow from "./components/ChatWindow";
import companyLogoIcon from "./img/ps-25-year-logo.svg"

function App() {

  return (
    <div className="App">
      <div className="heading">
        <span> 
        <img src={companyLogoIcon} alt="partsselect-icon" width="150" height="100" />
        {'   '} PartSelect Chatbot
        </span>
      </div>
        <ChatWindow/>
    </div>
  );
}

export default App;
