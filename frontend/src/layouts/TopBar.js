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
              <MenuIcon />
            	"This is the TopBar header"
			</Toolbar>
			
		</div>
	)
}