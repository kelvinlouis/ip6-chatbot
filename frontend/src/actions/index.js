import moment from 'moment';
import { AUTHOR_USER, AUTHOR_BOT } from '../constants';

export const ADD_USER_MESSAGE = 'ADD_USER_MESSAGE';
export const ADD_BOT_MESSAGE = 'ADD_BOT_MESSAGE';
export const ADD_LANGUAGE_ERRORS = 'ADD_LANGUAGE_ERRORS';
export const START_THINKING = 'START_THINKING';
export const STOP_THINKING = 'STOP_THINKING';
export const AUTHENTICATE = 'AUTHENTICATE';

function createMessage(text, type, author) {
  return {
    type,
    text,
    author,
    timestamp: moment(),
    messageId: `${+moment()}`,
    errors: [],
  };
}

export const addUserMessage = (text) => createMessage(text, ADD_USER_MESSAGE, AUTHOR_USER);
export const addBotMessage = (text) => createMessage(text, ADD_BOT_MESSAGE, AUTHOR_BOT);

export const addLanguageErrors = (messageId, errors) => ({
  type: ADD_LANGUAGE_ERRORS,
  messageId,
  errors,
});

export const startThinking = () => ({
  type: START_THINKING,
});

export const stopThinking = () => ({
  type: STOP_THINKING,
});

export const authenticate = (participantId) => ({
  type: AUTHENTICATE,
  participantId,
});
