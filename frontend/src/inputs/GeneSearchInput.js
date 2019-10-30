import React from 'react';
import '../styles/App.scss'

import { Paper, Typography, TextField, Grid } from '@material-ui/core';
import { zIndex } from '@material-ui/system'
import Button from '@material-ui/core/Button';

export const GeneSearchInput = (props) => {
	return(
			<div>
				<Paper className="main-paper" elevation={3}>
					<Typography variant="h5">Query for your genes of interest here:</Typography>
					<Typography variant="p">{"You can input any number of genes separated by commas or spaces. Genes are case insentive. Please use Gene Symbols only."}</Typography>
					<form className="text-center">
						<Grid
				          container
				          spacing={2}
				        >
				        	<Grid item lg={10} md={10} xl={10} xs={12}>
								<TextField
							        id="filled-multiline-static"
							        label="Gene List"
							        multiline
							        rows="2"
							        placeholder="Enter your genes here!"
							        className="text-field vertical-center"
							        margin="normal"
							        variant="outlined"
							        fullWidth={true}
							        onChange={props.handleTextChange}
							      />
							</Grid>
							<Grid item lg={2} md={2} xl={2} xs={12}>
								<div style={{'margin-top': '32px'}}>
						      		<Button className="submit-button" variant="contained" color="primary" onClick={ () => {} }>
					        			Submit
						    		</Button>
					    		</div>
						    </Grid>
					    </Grid>
					</form>
				</Paper>
			</div>
		)
}

