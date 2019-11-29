import React from 'react';
import '../styles/App.scss';

import {
  Toolbar,
  Typography
} from '@material-ui/core';

import {
  Menu as MenuIcon,
} from '@material-ui/icons';

export const TopBar = () => {
	return(
		<div className="topbar">
			<Toolbar className="toolbar">
             		<MenuIcon className='text-top pad-left'/>
             		<Typography variant="h5" className="pad-left text-top">GeneSearch</Typography>
			</Toolbar>
			
		</div>
	)
}