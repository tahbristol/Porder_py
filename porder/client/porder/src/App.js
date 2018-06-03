import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Header} from './components/Header'
import {Welcome} from './components/Welcome'
import {SignupForm} from './components/SignupForm'

class App extends Component {
	state = {
			name: '',
			email: '',
			password: '',
			password: ''
	}
	
	handleSignupInput = (evt) => {
		this.setState({
			[evt.target.name]: evt.target.value
		})
	}
	
	handleSignup = (evt) => {
	}
	render() {
		return (
      <div className="App">
				<Header />
				<SignupForm signupForm={this.state.handleSignupInput}
					handleSignup={this.handleSignup}
					handleSignupInput={this.handleSignupInput} />
      </div>
    );
	}
}

export default App;
