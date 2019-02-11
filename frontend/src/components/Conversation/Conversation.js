import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Message from '../Message/Message';
import ThinkingIndicator from '../ThinkingIndicator/ThinkingIndicator';
import './Conversation.scss';

class Conversation extends Component {
  static propTypes = {
    messages: PropTypes.array,
    thinking: PropTypes.bool,
  };

  constructor(props) {
    super(props);

    this.messagesElement = React.createRef();
  }

  componentDidUpdate() {
    this.scrollToBottom();
  }

  scrollToBottom = () => {
    const messagesDiv = this.messagesElement.current;
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  };

  /**
   * Checks if the prior message (index) is of the same author.
   * @param index
   * @returns {boolean}
   */
  isPriorMessageSameAuthor(index) {
    const { messages } = this.props;

    if (index === 0) {
      return false;
    } else {
      const prior = messages[index - 1];
      const current = messages[index];

      return prior.author === current.author;
    }
  }

  render() {
    const { thinking, messages } = this.props;

    return (
      <div className="conversation" ref={this.messagesElement}>
        {messages.map((m, index) => (
          <Message
            id={m.messageId}
            key={m.timestamp}
            author={m.author}
            text={m.text}
            timestamp={m.timestamp}
            errors={m.errors}
            showAvatar={!this.isPriorMessageSameAuthor(index)}
          />
        ))}
        <ThinkingIndicator thinking={thinking} />
      </div>
    );
  }
}

/**
 * Creates the mapping to the Redux store
 * @param state
 * @returns {{messages: (*|*[])}}
 */
function mapStateToProps(state) {
  return {
    messages: state.conversation.messages,
    thinking: state.conversation.thinking,
  };
}

export default connect(mapStateToProps)(Conversation);
