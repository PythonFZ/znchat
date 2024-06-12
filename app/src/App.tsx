import { useState, useEffect, useRef } from 'react';
import { socket } from './socket';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import { Card } from 'react-bootstrap';

const App = () => {
  const [messages, setMessages] = useState<string[]>([]);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleMessageSend = () => {
    const message = inputRef.current?.value;
    if (message) {
      socket.emit('message', message);
      inputRef.current.value = '';
    }
  };

  useEffect(() => {
    const handleConnect = () => {
      console.log('Connected to socket.io server');
    };

    const handleDisconnect = () => {
      console.log('Disconnected from socket.io server');
    };

    const handleMessageReceive = (message: string) => {
      setMessages((prevMessages) => [...prevMessages, message]);
    };

    socket.on('connect', handleConnect);
    socket.on('disconnect', handleDisconnect);
    socket.on('message', handleMessageReceive);

    return () => {
      socket.off('connect', handleConnect);
      socket.off('disconnect', handleDisconnect);
      socket.off('message', handleMessageReceive);
    };
  }, []);

  return (
    <Card>
      <Card.Header>
        <img src={viteLogo} className="App-logo" alt="Vite logo" />
        <img src={reactLogo} className="App-logo" alt="React logo" />
        <h1>Hello Vite + React!</h1>
      </Card.Header>
      <Card.Body>
        <h2>Messages from server:</h2>
        <ul>
          {messages.map((msg, index) => (
            <li key={index}>{msg}</li>
          ))}
        </ul>
        <div>
          <input
            type="text"
            placeholder="Type a message..."
            ref={inputRef}
            onKeyDown={(event) => {
              if (event.key === 'Enter') {
                handleMessageSend();
              }
            }}
          />
          <button onClick={handleMessageSend}>Send</button>
        </div>
      </Card.Body>
    </Card>
  );
};

export default App;
