import { combineReducers } from 'redux';
import { conversation } from './conversation';
import { behavior } from './behavior';

const appReducers = combineReducers({
  conversation,
  behavior,
});

export default appReducers;
