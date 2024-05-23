import React, { useState } from "react";
import "./App.css";
import Titlebar from "./Titlebar/Titlebar";
import MainContent from "./MainContent/MainContent";
import Sidenav from "./Sidenav/Sidenav";

function App() {
  const onlineCount = 0;

  // handler for number of input terminals
  const [numberOfTerminals, setNumberOfTerminals] = useState(1);
  const handleTerminalChange = (event) => {
    setNumberOfTerminals(event.target.value);
  };

  // handler for selecting input terminals
  const [selectedContent, setSelectedContent] = useState("home");
  const handleSelect = (content) => {
    setSelectedContent(content);
  };

  return (
    <div className="app">
      <Titlebar className="topbar" />
      <div className="container">
        <Sidenav
          onSelect={handleSelect}
          numberOfTerminals={numberOfTerminals}
        />
        <MainContent
          selectedContent={selectedContent}
          onlineCount={onlineCount}
        />
      </div>
    </div>
  );
}

export default App;
