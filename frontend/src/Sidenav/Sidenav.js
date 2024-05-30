// src/components/SideNav.js
import React from "react";
import "./Sidenav.css";

const Sidenav = ({ onSelect, numberOfTerminals }) => {
  return (
    <div className="sidenav">
      <ul>
        <li onClick={() => onSelect("home")}>home</li>
        <li onClick={() => onSelect("baseTerminal")}>terminal 1</li>
        <li onClick={() => onSelect("dummyTerminal")}>dummy terminal</li>
      </ul>
    </div>
  );
};

export default Sidenav;
