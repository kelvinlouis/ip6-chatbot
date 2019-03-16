import io from 'socket.io-client';
import {
  ADD_USER_MESSAGE,
  addBotMessage, addLanguageErrors,
  startThinking,
  stopThinking
} from './actions';
import { secondsByLength } from './utils';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
let socket = null;

/**
 * This functions as a redux middleware.
 * Whenever a message is composed by the user it is emitted to the backend.
 * @param store
 * @returns {function(*): Function}
 */
export const socketConnectorMiddleware = store => next => action => {
  // Continue
  next(action);

  if (action.type === ADD_USER_MESSAGE) {
    if (socket === null) {
      throw new Error('Socket connection has not been initialized yet');
    }

    socket.emit('user_uttered', {
      message: action.text,
      message_id: action.messageId,
      participant_id: store.getState().conversation.participantId,
    });
  }
};

/**
 * Creates a socket connection to the backend.
 * @param store
 */
export function initSocketConnector(store) {
  socket = io(BACKEND_URL);

  socket.on('connect', () => {
    console.log(`connect:${socket.id}`);
  });

  socket.on('connect_error', (error) => {
    console.log(error);
  });

  socket.on('error', (error) => {
    console.log(error);
  });

  socket.on('disconnect', (reason) => {
    console.log(reason);
  });

  // This queue creates a artificial delay
  // so the user isn't bombarded with responses
  const delayedQueue = [];

  // Invoked whenever the bot sends a text message
  socket.on('bot_uttered', (data) => {
    // Marks the response as scheduled
    delayedQueue.push({
      ...data,
      scheduled: false,
    });
  });

  // Invoked whenever the bot found errors in a message of a user
  socket.on('bot_found_errors', (data) => {
    store.dispatch(addLanguageErrors(data.messageId, data.errors));
  });

  // Polls and checks if there are any responses to display.
  setInterval(() => {
    if (delayedQueue.length > 0) {
      // Only handle response, if it isn't scheduled yet.
      if (!delayedQueue[0].scheduled) {
        const { text, errors } = delayedQueue[0];
        delayedQueue[0].scheduled = true;

        store.dispatch(startThinking());

        // Artificial delay based on string length
        setTimeout(() => {
          store.dispatch(stopThinking());
          store.dispatch(addBotMessage(text, errors));

          // Removes item from the queue
          delayedQueue.splice(0, 1);
        }, secondsByLength(text));
      }
    }
  }, 100);
}
