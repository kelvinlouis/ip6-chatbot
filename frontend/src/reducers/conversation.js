import moment from 'moment';
import {
  ADD_BOT_MESSAGE,
  ADD_LANGUAGE_ERRORS,
  ADD_USER_MESSAGE,
  AUTHENTICATE,
  START_THINKING,
  STOP_THINKING
} from '../actions';
import { patch } from './helper';

/**
 * The initial state of the store.
 * The participantId is overwritten, if a participant id is
 * provided through a dispatched action.
 */
const initialState = {
  participantId: `participant-${moment().unix()}`,
  messages: [],
  thinking: false,
};

function messages(state = [], action) {
  switch (action.type) {
    case ADD_LANGUAGE_ERRORS:
      // Append errors detected in a message of a user
      // Immutable => creating a new copy of the message
      return state.map(message => {
        if (message.messageId === action.messageId) {
          return {
            ...message,
            errors: action.errors,
          };
        }
        return message;
      });
    case ADD_USER_MESSAGE:
    case ADD_BOT_MESSAGE:
      return [
        ...state,
        {
          author: action.author,
          text: action.text,
          timestamp: action.timestamp,
          messageId: action.messageId,
          errors: action.errors,
        }
      ];
    default:
      return state;
  }
}

export function conversation(state = initialState, action) {
  const patchState = patch(state);
  switch (action.type) {
    case ADD_LANGUAGE_ERRORS:
    case ADD_USER_MESSAGE:
    case ADD_BOT_MESSAGE:
      return patchState({ messages: messages(state.messages, action) });
    case START_THINKING:
      return patchState({ thinking: true });
    case STOP_THINKING:
      return patchState({ thinking: false });
    case AUTHENTICATE:
      return patchState({ participantId: action.participantId });
    default:
      return state;
  }
}
