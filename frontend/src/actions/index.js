import moment from 'moment';
import { AUTHOR_USER, AUTHOR_BOT } from '../constants';

export const ADD_USER_MESSAGE = 'ADD_USER_MESSAGE';
export const ADD_BOT_MESSAGE = 'ADD_BOT_MESSAGE';
export const START_THINKING = 'START_THINKING';
export const STOP_THINKING = 'STOP_THINKING';

function createMessage(text, type, author) {
  return {
    type,
    text,
    author,
    timestamp: moment(),
  };
}

export function addUserMessage(text) {
  return createMessage(text, ADD_USER_MESSAGE, AUTHOR_USER);
}

export function addBotMessage(text) {
  return createMessage(text, ADD_BOT_MESSAGE, AUTHOR_BOT);
}

export function startThinking() {
  return {
    type: START_THINKING,
  };
}

export function stopThinking() {
  return {
    type: STOP_THINKING,
  };
}
