import moment from 'moment';
import {
  ADD_BOT_MESSAGE,
  ADD_USER_MESSAGE, SET_PARTICIPANT_ID,
  START_THINKING,
  STOP_THINKING
} from '../actions';

const initialState = {
  participantId: `participant-${moment().unix()}`,
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
  // Curried function for cleaner code to update the state
  const patch = state => parts => Object.assign({}, state, parts);
  const patchState = patch(state);

  switch (action.type) {
    case ADD_USER_MESSAGE:
    case ADD_BOT_MESSAGE:
      return patchState({ messages: messages(state.messages, action) });
    case START_THINKING:
      return patchState({ thinking: true });
    case STOP_THINKING:
      return patchState({ thinking: false });
    case SET_PARTICIPANT_ID:
      return patchState({ participantId: action.participantId });
    default:
      return state;
  }
}
