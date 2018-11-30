import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import Fab from '@material-ui/core/Fab';
import Icon from '@material-ui/core/Icon';

import './InputMask.scss';
import { addUserMessage } from '../../actions';

/**
 * Enter key for events
 * @type {number}
 */
const KEY_CODE_ENTER = 13;

export class InputMask extends Component {
  static propTypes = {
    onMessageSend: PropTypes.func,
    spellCheck: PropTypes.bool,
  };

  static defaultProps = {
    onMessageSend: (text) => {},
    spellCheck: false,
  };

  constructor(props) {
    super(props);

    // Allows accessing the DOM element
    this.input = React.createRef();

    // Disable spell check
    this.state = {
      spellCheck: props.spellCheck,
    };
  }

  componentDidMount() {
    this.focus();
  }

  focus() {
    this.input.current.focus();
  }

  clearInput() {
    this.input.current.innerText = '';
  }

  /**
   * Checks whether the enter key was pressed without using shift.
   * @param event
   * @returns {boolean}
   */
  isJustEnterKey(event) {
    return event.keyCode === KEY_CODE_ENTER && !event.shiftKey;
  }

  /**
   * Checks if the input is empty.
   * @returns {boolean}
   */
  isEmpty() {
    const text = this.input.current.innerText;
    return text.trim().length === 0;
  }

  onSendButtonClick = (event) => {
    if (!this.isEmpty()) {
      this.sendMessage();
      this.clearInput();
      this.focus();
    }
  };

  onKeyDown = (event) => {
    if (this.isJustEnterKey(event)) {
      if (!this.isEmpty()) {
        this.sendMessage();
        this.clearInput();
      }

      // Make sure the line break of pressing enter is ignored
      event.stopPropagation();
      event.preventDefault();
    }
  };

  sendMessage = () => {
    const { onMessageSend } = this.props;
    const message = this.input.current.innerText;

    // Trigger event
    onMessageSend(message);
  };

  render() {
    const { spellCheck } = this.state;

    return (
      <div className="input-mask">
        <div className="input-mask__input-wrapper">
          <div
            className="input-mask__input"
            contentEditable={true}
            spellCheck={spellCheck}
            ref={this.input}
            placeholder="Type a message..."
            onKeyUp={this.onKeyUp}
            onKeyDown={this.onKeyDown}
          />
        </div>
        <Fab color="primary" className="input-mask__button" aria-label="Add" onClick={this.onSendButtonClick}>
          <Icon>send</Icon>
        </Fab>
      </div>
    );
  }
}

function mapDispatchToProps(dispatch) {
  return {
    onMessageSend: (message) => {
      dispatch(addUserMessage(message));
    },
  };
}

export default connect(undefined, mapDispatchToProps)(InputMask);
