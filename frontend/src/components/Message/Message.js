import React from 'react';
import './Message.scss';
import { AUTHOR_BOT } from '../../constants';
import Avatar from '@material-ui/core/Avatar/Avatar';

const Message = ({ author, text, timestamp, showAvatar }) => {
  return (
    <div className={`message message--${ author } message--${ showAvatar ? 'avatar' : 'plain'}`}>
      <Avatar className="message__avatar">{author === AUTHOR_BOT ? 'FP' : 'Me'}</Avatar>
      <div className="message__text-wrapper">
        <div className="message__text">{ text }</div>
      </div>
      <div className="message__time">{ timestamp.format('LT') }</div>
    </div>
  );
};

export default Message;
