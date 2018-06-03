import React from 'react'

export const Header = () => {
	return(
		<header>
			<div className="container">
				<div className="row">
					<div className="col-sm-6">
						<a href="/">
							<h1 id="brand">pOrder</h1>
						</a>
					</div>
					<div className="col-sm-6">
						<nav className="navButtons">

								<a href="" className=" text-sm-right">Logout</a>
								<a href="" className="text-sm-right">Profile</a>
							
						</nav>
					</div>
				</div>
			</div>
		</header>
	)
}