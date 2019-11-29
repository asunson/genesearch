import React, {Component} from 'react';
import { BrowserRouter as Router, Redirect, Route, Switch, withRouter } from 'react-router-dom';
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

export class MainRoutes extends Component {
    constructor(props) {
        super(props);
        this.state = {
            samples: null,
            geneList: [],
            geneResults: null
        }
    }

    componentDidMount() {
        fetch("api/samples/", {method: "get"}).then(
            response => {return response.json()}
        ).then(
            data => this.setState({samples: data})
        ).catch(
            (e) => console.log(e)
        );
    }

    handleTextChange = (e) => {
        var s = e.target.value;
        var list = s.split(/[\s ,\n\t]+/);
        list = list.map((s) => s.toUpperCase())
        this.setState({geneList: list});
    }

    queryGenes = () => {
        fetch(
            "api/search/", {
                method: "post",
                body: JSON.stringify({geneList: this.state.geneList}),
                headers: new Headers({"Content-Type": "application/json"})
            }
        ).then(
            response => {return response.json()}
        ).then(
            data => this.setState({geneResults: data})
        ).catch(
            (e) => console.log(e)
        );
    }

    render() {
        return (
            <Router>
                <ScrollControl>
                    <main>
                        <Switch>
                            <Route exact path="/search" render={() => (
                                <div>
                                    <GeneSearchInput 
                                        handleTextChange={this.handleTextChange.bind(this)}
                                        handleSubmit={this.queryGenes.bind(this)}
                                    />
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
        )
    }
}