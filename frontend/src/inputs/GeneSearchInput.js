import React from 'react';
import '../styles/App.scss'

import { Paper, Typography, TextField } from '@material-ui/core';
import Button from '@material-ui/core/Button';

export const GeneSearchInput = (props) => {
	return(
			<div>
				<form className="text-center">
					<TextField
				        id="filled-multiline-static"
				        label="Gene List"
				        multiline
				        rows="1"
				        placeholder="Enter your genes here!"
				        className="text-field vertical-center"
				        margin="normal"
				        variant="filled"
				        onChange={props.handleTextChange}
				      />
				      <Button className="vertical-center" variant="contained" color="primary" className="button" onClick={ () => {} }>
			        	Submit
			    	</Button>
				</form>
			</div>
		)
}

