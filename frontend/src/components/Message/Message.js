import React from 'react';
import Avatar from '@material-ui/core/Avatar/Avatar';
import Tooltip from '@material-ui/core/Tooltip';
import './Message.scss';
import { AUTHOR_BOT } from '../../constants';

/**
 * Used to display a message of the user and chatbot. If a message contains errors,
 * the message will be separated into parts, in order to highlight the faulty sections.
 */
const Message = ({ author, text, timestamp, showAvatar, errors }) => {
  const parts = [];

  if (errors != null && errors.length > 0) {
    let errorIndex = 0;
    let startPos = 0;
    let endPos = errors[errorIndex].start_pos;

    while (endPos != null) {
      // Everything prior to the first occurrence of an error is regarded as correct
      parts.push({ error: false, text: text.substring(startPos, endPos) });

      startPos = endPos;
      endPos = errors[errorIndex].end_pos;

      parts.push({ error: errors[errorIndex], text: text.substring(startPos, endPos) });

      startPos = endPos;
      endPos = errors[errorIndex + 1] ? errors[errorIndex + 1].start_pos : null;
      errorIndex++;
    }

    // Mark the rest of the text correct
    parts.push({ error: false, text: text.substring(startPos, text.length) });
  } else {
    // No errors were found => everything is correct
    parts.push({ error: false, text });
  }

  return (
    <div className={`message message--${ author } message--${ showAvatar ? 'avatar' : 'plain'}`}>
      <Avatar className="message__avatar">{author === AUTHOR_BOT ? 'FP' : 'Me'}</Avatar>
      <div className="message__text-wrapper">
        <div className="message__text">
          {parts.map((part, index) => {
            if (part.error) {
              return (
                <Tooltip key={index} title={part.error.message}>
                  <span className={"message__error message__error--" + part.error.type}>{part.text}</span>
                </Tooltip>
              );
            } else {
              return <span key={index}>{part.text}</span>
            }
          })}
        </div>
      </div>
      <div className="message__time">{ timestamp.format('LT') }</div>
    </div>
  );
};

export default Message;
