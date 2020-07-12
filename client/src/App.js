import React, {useState, useEffect} from 'react';
import './App.css';

function App() {

  useEffect(() => {
      fetch('http://localhost:5000/').then(res => res.json()).then( data => {
        console.log('data', data)
      }) 
  })

  return (
    <div className="App">
        Test
    </div>
  );
}

export default App;
