import React from 'react';
import ReactDOM from 'react-dom';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
// import { createMuiTheme, MuiThemeProvider } from '@material-ui/core/styles';
import App from './App';
import * as serviceWorker from './serviceWorker';
import { socketConnectorMiddleware, initSocketConnector } from './socketConnector';
import appReducers from './reducers';

// Creates the Redux Store and applies the socket middleware,
// to intercept actions and emit them to the backend
const store = createStore(
  appReducers,
  applyMiddleware(socketConnectorMiddleware)
);

// Creates the socket connection for the middleware
initSocketConnector(store);

// const theme = createMuiTheme({
//   palette: {
//     primary: {
//       main: '#80C0A1',
//     },
//     secondary: {
//       main: '#73ACB7',
//     },
//   },
// });

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
