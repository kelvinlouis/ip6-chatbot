import { combineReducers } from 'redux';
import { conversation } from './conversation';

const appReducers = combineReducers({
  conversation,
});

export default appReducers;
