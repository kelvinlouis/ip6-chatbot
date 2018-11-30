import React from 'react';
import './ThinkingIndicator.scss';

const ThinkingIndicator = ({ thinking }) => {
  return (
    <div className={`thinking-indicator${thinking ? ' thinking-indicator--visible' : ''}`}>
      <span className="thinking-indicator__dot" />
      <span className="thinking-indicator__dot" />
      <span className="thinking-indicator__dot" />
    </div>
  );
};

export default ThinkingIndicator;
