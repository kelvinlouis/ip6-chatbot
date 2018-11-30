import React, { Component } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import './App.scss';
import Conversation from './components/Conversation/Conversation';
import InputMask from './components/InputMask/InputMask';

class App extends Component {
  render() {
    return (
      <div className="app">
        <CssBaseline />
        <div className="app__main">
          <Conversation />
          <InputMask />
        </div>
        <div className="app__bg">
          <div className="app__bg-gradient" />
          <div className="app__bg-color" />
        </div>
      </div>
    );
  }
}

export default App;
