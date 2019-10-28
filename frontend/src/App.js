import React, {Component} from 'react';
import { BrowserRouter as Router, Redirect, Route, Switch, withRouter } from 'react-router-dom';
import './styles/App.scss';
import {TopBar} from './layouts/TopBar'

class ScrollToTop extends Component {
  componentDidUpdate(prevProps) {
    if (this.props.location.pathname !== prevProps.location.pathname) {
      window.scrollTo(0, 0);
    }
  }

  render() {
    return (
        <div>
          <TopBar/>
          {this.props.children}
        </div>
        
    )
  }
}

const ScrollControl = withRouter(ScrollToTop);

function App() {
  return (
    <Router>
      <ScrollControl>
        <main>
          <Switch>
            <Route exact path="/search" render={() => (
              <div>
                This is some content
              </div>
            )}/>
            <Route exact path="/" render={() => (
              <Redirect to="/search"/>
            )}/>
          </Switch>
        </main>
      </ScrollControl>
    </Router> 
  );
}

export default App;
