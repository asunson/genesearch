import React, {Component} from 'react';
import { BrowserRouter as Router, Redirect, Route, withRouter } from 'react-router-dom';
import './styles/App.css';
import {TopBar} from './layouts/TopBar'

class ScrollToTop extends Component {
  componentDidUpdate(prevProps) {
    if (this.props.location.pathname !== prevProps.location.pathname) {
      window.scrollTo(0, 0);
    }
  }

  render() {
    return (
      <TopBar>
        {this.props.children}
      </TopBar>
    )
  }
}

const ScrollControl = withRouter(ScrollToTop);

function App() {
  return (
    <Router>
      <ScrollControl>
        <main>
            <Route exact path="/search" render={() => (
              <div>
                This is some content
              </div>
            )}/>
            <Route exact path="/" render={() => (
              <Redirect to="/search"/>
            )}/>
        </main>
      </ScrollControl>
    </Router> 
  );
}

export default App;
