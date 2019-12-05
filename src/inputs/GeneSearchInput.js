import React from 'react';
import '../styles/App.scss';

import { Paper, Typography, TextField, Grid } from '@material-ui/core';
import Button from '@material-ui/core/Button';

export const GeneSearchInput = (props) => {
	return(
			<div>
				<Paper className="paper-input" elevation={3}>
					<Typography variant="h5">Query for your genes of interest here:</Typography>
					<Typography variant="body1">{"You can input any number of genes separated by commas or spaces. Genes are case insensitive. Please use Gene Symbols only. Values displayed are in log2(FPKM)"}</Typography>
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
								<div style={{'marginTop': '32px'}}>
						      		<Button className="submit-button" variant="contained" color="primary" onClick={props.handleSubmit}>
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

