import React from 'react';
import '../styles/Main.css';

function Main() {
  return (
    <div className="Main">
      <header className="Main-header">
        <img src="./main/assets/logo.svg" className="Main-logo" alt="logo" />
        <p>
          Hello from <strong>React.</strong>
        </p>
      </header>
    </div>
  );
}

export default Main;