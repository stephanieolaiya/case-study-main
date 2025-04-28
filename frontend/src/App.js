import React from "react";
import "./App.css";
import ChatWindow from "./components/ChatWindow";
import companyLogoIcon from "./img/ps-25-year-logo.svg"
import redirectLogo from './img/go_to_website_icon.png'

function App() {

  return (
    <div className="App">
      <div className="heading">
        <span> 
        <img src={companyLogoIcon} alt="partselect-icon" width="200" height="100" />
        </span>
        <div className="contact-info">
          <div style={{fontSize: 18}}>1-866-319-8402</div>
          <div style={{fontSize: 12}}>Monday to Saturday</div>
          <div style={{fontSize: 12}}>8am - 9pm EST</div>
        </div>
          <a href="https://www.partselect.com/" style={{color:'black'}}> Go To Site
          <img src={redirectLogo} alt="go to website logo" width="100" height="100"></img>
        </a>
          
      </div>
        <ChatWindow/>
    </div>
  );
}

export default App;
