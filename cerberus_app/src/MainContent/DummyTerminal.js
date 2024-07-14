import React, { useEffect, useState } from "react";

const DummyTerminal = () => {
  const [data, setData] = useState({
    message: "",
    matches: 0,
    matched_keywords: [],
    match_dict: {},
  });

  const [terminalStatus, setStatus] = useState(0);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8765");

    socket.onmessage = (event) => {
      const receivedData = JSON.parse(event.data);
      setData(receivedData);
      setStatus(1);
    };

    socket.onclose = () => {
      console.log("WebSocket connection closed");
    };

    return () => {
      socket.close();
      setStatus(0);
    };
  }, []);

  const baseContent = (
    <p className="main-content">Conversations are displayed here.</p>
  );

  const rtContent = (
    <div>
      <p className="header-content">{data.message}</p>
      <p className="main-content"> Matches count: {data.matches} </p>
      <p className="main-content">Matched keywords: {data.matched_keywords}</p>
    </div>
  );

  return (
    <div>
      <p className="header-content">Listening to DUMMY TERMINAL.</p>
      {terminalStatus === 0 && baseContent}
      {terminalStatus === 1 && rtContent}
    </div>
  );
};

export default DummyTerminal;
