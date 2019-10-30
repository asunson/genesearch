import React, {Component} from 'react';
import { BrowserRouter as Router, Redirect, Route, Switch, withRouter } from 'react-router-dom';
import './styles/App.scss';
import {TopBar} from './layouts/TopBar'
import {GeneSearchInput} from './inputs/GeneSearchInput'

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

const handleTextChange = (e) => {
    var s = e.target.value;
    var list = s.split(/[\s ,\n\t]+/);
    this.setState({ geneList:list });
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      geneList: []
    }
  }

  render() {
    return (
      <Router>
        <ScrollControl>
          <main>
            <Switch>
              <Route exact path="/search" render={() => (
                <div>
                  <GeneSearchInput handleTextChange={this.handleTextChange}/>
                </div>
              )}/>
              <Route exact path="/" render={() => (
                <Redirect to="/search"/>
              )}/>
              <Redirect to="/search"/>
            </Switch>
          </main>
        </ScrollControl>
      </Router> 
    );
  }
}

export default App;
