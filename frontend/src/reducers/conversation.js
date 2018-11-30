import moment from 'moment';
import {
  ADD_BOT_MESSAGE,
  ADD_USER_MESSAGE,
  START_THINKING,
  STOP_THINKING
} from '../actions';

const initialState = {
  id: moment().unix(),
  messages: [],
  thinking: false,
};

function messages(state = [], action) {
  switch (action.type) {
    case ADD_USER_MESSAGE:
    case ADD_BOT_MESSAGE:
      return [
        ...state,
        {
          author: action.author,
          text: action.text,
          timestamp: action.timestamp,
        }
      ];
    default:
      return state;
  }
}

export function conversation(state = initialState, action) {
  switch (action.type) {
    case ADD_USER_MESSAGE:
    case ADD_BOT_MESSAGE:
      return Object.assign({}, state, {
        messages: messages(state.messages, action)
      });
    case START_THINKING:
      return Object.assign({}, state, {
        thinking: true,
      });
    case STOP_THINKING:
      return Object.assign({}, state, {
        thinking: false,
      });
    default:
      return state;
  }
}
