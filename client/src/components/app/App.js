import React, {useState, useEffect} from 'react';
import { Route, Switch } from 'react-router-dom';
import Home from '../home/Home';
import  Terms from '../terms/Terms';
import Privacy from '../privacy/Privacy';
import Navbar from '../navbar/Navbar';
import Footer from '../footer/Footer';

import './App.css';

function App() {

  useEffect(() => {
      fetch('http://localhost:5000/').then(res => res.json()).then( data => {
        console.log('data', data)
      }) 
  })

  return (
    <main className="container">
		<Navbar />
		<div className="md-margin-top">
			<Switch>
				<Route path="/" component={Home} exact />
				<Route path="/terms" component={Terms} exact />
				<Route path="/privacy" component={Privacy} exact />
			</Switch>
		</div>
		
		<Footer/>
    </main>

  );
}

export default App;
