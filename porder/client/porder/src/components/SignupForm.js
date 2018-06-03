import React from 'react'

export const SignupForm = (props) => {
		return (
			<div className="container signupPage">
				<h2>Sign Up</h2>
				<form className="form-signin form-signup" onSubmit={props.handleSignup}>
					<label>Name
						<input type="text" name="name" onChange={props.handleSignupInput} value={props.name}/>
					</label>
					<label>Email
						<input type="email" name="email" onChange={props.handleSignupInput} value={props.email}/>
					</label>
					<label>Password
						<input type="password" name="password" onChange={props.handleSignupInput} value={props.password}/>
					</label>
					<label>Password Confirmation
						<input type="password" name="password_confirmation" onChange={props.handleSignupInput} value={props.password_confirmation}/>
					</label>
					<input className="btn btn-success" type="submit" value="Submit"/>
				</form>
				<p>
					<small>Have an account?</small>
					<a href="">
						<strong> Login</strong>
					</a>
				</p>
			</div>
		)
}