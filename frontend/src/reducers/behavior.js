import { AUTHENTICATE } from '../actions';
import { patch } from './helper';

const initialState = {
  authenticationEnabled: Boolean(process.env.REACT_APP_AUTHENTICATION_ENABLED),
  authenticated: false,
};

export function behavior(state = initialState, action) {
  const patchState = patch(state);

  switch (action.type) {
    case AUTHENTICATE:
      if (action.participantId == null) {
        throw new Error(`Authentication has no participant id`);
      }

      return patchState({ authenticated: true });
    default:
      return state;
  }
}
