import React from "react";
import "./MainContent.css";
import DummyTerminal from "./DummyTerminal";

const MainContent = ({ selectedContent, onlineCount }) => {
  // initialising base downloaded content
  const baseContent = (
    <div>
      <p className="header-content">
        Welcome. There are currently {onlineCount} input terminals online.
      </p>
      <p className="main-content">
        Online terminals are displayed on the left.
      </p>
    </div>
  );

  const terminal = (
    <div>
      <p className="header-content">Listening to terminal 1.</p>
      <p className="main-content">Conversations are displayed here.</p>
    </div>
  );

  const activeTerminal = (
    <div>
      <DummyTerminal />
    </div>
  );

  return (
    <div className="main-body">
      {/* Example of handling different content based on selectedContent */}
      {selectedContent === "home" && baseContent}
      {selectedContent === "baseTerminal" && terminal}
      {selectedContent === "dummyTerminal" && activeTerminal}
    </div>
  );
};

export default MainContent;
