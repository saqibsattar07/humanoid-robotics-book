import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import clsx from 'clsx';
import styles from './Chatbot.module.css';

interface Citation {
  chunk_id: string;
  module: string;
  chapter: string;
  section: string;
  page_number: number;
  text_snippet: string;
  relevance_score: number;
}

interface Message {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  citations?: Citation[];
  timestamp: Date;
}

interface ChatRequest {
  query_text: string;
  query_type: 'full_book' | 'selected_text';
  selected_text?: string;
  session_id?: string;
}

interface ChatResponse {
  response_text: string;
  citations: Citation[];
  grounded: boolean;
  retrieval_time?: number;
  generation_time?: number;
}

const Chatbot: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [queryType, setQueryType] = useState<'full_book' | 'selected_text'>('full_book');
  const [selectedText, setSelectedText] = useState('');
  const [error, setError] = useState<string | null>(null);
  const messagesEndRef = useRef<null | HTMLDivElement>(null);
  const chatContainerRef = useRef<null | HTMLDivElement>(null);

  const API_BASE_URL = 'http://localhost:8000';

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    // Close chat when clicking outside
    const handleClickOutside = (event: MouseEvent) => {
      if (chatContainerRef.current && !chatContainerRef.current.contains(event.target as Node)) {
        if (isOpen) {
          setIsOpen(false);
        }
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [isOpen]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      content: inputValue,
      role: 'user',
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);
    setError(null);

    try {
      // Prepare the request
      const request: ChatRequest = {
        query_text: inputValue,
        query_type: queryType,
        selected_text: queryType === 'selected_text' ? selectedText : undefined,
      };

      // Call the backend API
      const response = await axios.post<ChatResponse>(`${API_BASE_URL}/chat`, request, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      // Add assistant message
      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: response.data.response_text,
        role: 'assistant',
        citations: response.data.citations,
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (err) {
      setError('Failed to get response. Please try again.');
      console.error('Chat error:', err);

      // Add error message to chat
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: 'Sorry, I encountered an error processing your request. Please try again.',
        role: 'assistant',
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (!isOpen) {
      // Focus the input when opening the chat
      setTimeout(() => {
        const input = document.getElementById('chatbot-input');
        if (input) input.focus();
      }, 100);
    }
  };

  const handleQueryTypeChange = (type: 'full_book' | 'selected_text') => {
    setQueryType(type);
  };

  return (
    <div className={styles.chatbotContainer} ref={chatContainerRef}>
      {/* Floating chat button */}
      {!isOpen && (
        <button
          className={styles.chatButton}
          onClick={toggleChat}
          aria-label="Open chatbot"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
            className={styles.chatIcon}
          >
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
          </svg>
        </button>
      )}

      {/* Chat window */}
      {isOpen && (
        <div className={styles.chatWindow}>
          <div className={styles.chatHeader}>
            <h3>AI Assistant</h3>
            <button
              className={styles.closeButton}
              onClick={toggleChat}
              aria-label="Close chat"
            >
              ×
            </button>
          </div>

          <div className={styles.queryTypeSelector}>
            <button
              className={clsx(styles.queryTypeButton, queryType === 'full_book' && styles.active)}
              onClick={() => handleQueryTypeChange('full_book')}
            >
              Full Book Query
            </button>
            <button
              className={clsx(styles.queryTypeButton, queryType === 'selected_text' && styles.active)}
              onClick={() => handleQueryTypeChange('selected_text')}
            >
              Selected Text Query
            </button>
          </div>

          {queryType === 'selected_text' && (
            <div className={styles.selectedTextInput}>
              <label htmlFor="selected-text">Selected Text Context:</label>
              <textarea
                id="selected-text"
                value={selectedText}
                onChange={(e) => setSelectedText(e.target.value)}
                placeholder="Paste or enter the text you want to ask about..."
                rows={3}
              />
            </div>
          )}

          <div className={styles.chatMessages}>
            {messages.map((message) => (
              <div
                key={message.id}
                className={clsx(styles.message, styles[message.role])}
              >
                <div className={styles.messageContent}>
                  {message.content}
                </div>
                {message.citations && message.citations.length > 0 && (
                  <div className={styles.citations}>
                    <h4>References:</h4>
                    <ul className={styles.citationsList}>
                      {message.citations.map((citation, index) => (
                        <li key={index} className={styles.citationItem}>
                          <div className={styles.citationMain}>
                            <strong>{citation.module} {citation.chapter}</strong> - {citation.section} (p. {citation.page_number})
                          </div>
                          <div className={styles.citationSnippet}>
                            "{citation.text_snippet}"
                          </div>
                          <div className={styles.citationScore}>
                            Relevance: {(citation.relevance_score * 100).toFixed(1)}%
                          </div>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))}
            {isLoading && (
              <div className={clsx(styles.message, styles.assistant)}>
                <div className={styles.typingIndicator}>
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {error && (
            <div className={styles.errorMessage}>
              {error}
            </div>
          )}

          <form className={styles.chatInputForm} onSubmit={handleSubmit}>
            <input
              id="chatbot-input"
              type="text"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              placeholder="Ask a question about the Physical AI & Humanoid Robotics book..."
              disabled={isLoading}
            />
            <button type="submit" disabled={isLoading || !inputValue.trim()}>
              {isLoading ? 'Sending...' : 'Send'}
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default Chatbot;