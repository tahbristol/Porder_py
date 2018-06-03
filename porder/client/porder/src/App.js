import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Header} from './components/Header'
import {Welcome} from './components/Welcome'

class App extends Component {
	render() {
		return (
      <div className="App">
				<Header />
				<Welcome />
      </div>
    );
	}
}

export default App;
