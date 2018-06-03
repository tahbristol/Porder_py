import React from 'react'

export const Welcome = () => {
	return(
		<div className="container welcome">
			<div className="row">
				<div className="col-sm-12" id="flashMessageContainer">
					
				</div>
				<div className="col-sm-12">
					<div className="container landing">
						<h1>Welcome to pOrder</h1>
						<h6>The tool to keep your orders in check</h6>
						<a href="" className="btn btn-primary">Create Account</a>
						<p>
							<small>Have an account?</small>
							<a href="">
								<strong>Login</strong>
							</a>
						</p>
					</div>
				</div>
			</div>
		</div>
	)
}