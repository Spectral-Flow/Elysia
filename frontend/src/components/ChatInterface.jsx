import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { FaMicrophone, FaPaperPlane, FaSpinner } from 'react-icons/fa';

const ChatInterface = ({ token }) => {
  const [messages, setMessages] = useState([
    { type: 'assistant', content: 'Hello! I\'m Elysia, your apartment concierge. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isRecording, setIsRecording] = useState(false);
  const messagesEndRef = useRef(null);
  
  // Auto scroll to bottom of messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);
  
  const sendMessage = async () => {
    if (input.trim() === '') return;
    
    const userMessage = { type: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);
    
    try {
      const response = await axios.post('/api/chat', 
        { message: input }, 
        { headers: { Authorization: token } }
      );
      
      const assistantMessage = { type: 'assistant', content: response.data.response };
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { 
        type: 'assistant', 
        content: 'Sorry, I encountered an error. Please try again later.' 
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };
  
  const toggleRecording = async () => {
    if (!isRecording) {
      setIsRecording(true);
      // In a real app, implement speech-to-text here
      // For now, we'll just simulate it with a timeout
      setTimeout(() => {
        setInput(input + "I'd like to book the community room for Saturday.");
        setIsRecording(false);
      }, 2000);
    } else {
      setIsRecording(false);
    }
  };
  
  return (
    <div className="chat-container">
      <div className="messages-container">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.type}`}>
            {msg.content}
          </div>
        ))}
        {isLoading && (
          <div className="message assistant loading">
            <FaSpinner className="spin" />
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      
      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button 
          className={`mic-button ${isRecording ? 'recording' : ''}`}
          onClick={toggleRecording}
        >
          <FaMicrophone />
        </button>
        <button 
          className="send-button" 
          onClick={sendMessage}
          disabled={input.trim() === '' || isLoading}
        >
          <FaPaperPlane />
        </button>
      </div>
    </div>
  );
};

export default ChatInterface;