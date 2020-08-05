import React from 'react';
import './Home.css';

function Home() {

  return (
    <div className="container sm-margin-top">
        <div className="row text-center lg-margin-bottom">
            <h1>Feeling lucky?</h1>
            <h3 className="text-muted">
                Test your luck against the roll of the dice and win today
            </h3>
        </div>
        <div className="row text-center">
            <div className="col-lg-4">
                <i className="fa fa-fw fa-4x fa-bullhorn text-primary"></i>
                <h2>Place bets</h2>
                <p className="text-muted">Correctly guess the dice's roll.</p>
                <p>
                    <a href="#" className="btn btn-default">Sign up</a>
                </p>
            </div>
            <div className="col-lg-4">
                <i className="fa fa-fw fa-4x fa-database text-primary"></i>
                <h2>Win currency</h2>
                <p className="text-muted">Gain coins if your guess is correct.</p>
                <p>
                    <a href="#" className="btn btn-default">Sign up</a>
                </p>
            </div>
            <div className="col-lg-4">
                <i className="fa fa-fw fa-4x fa-trophy text-primary"></i>
                <h2>Leaderboard</h2>
                <p className="text-muted">Compare your results to others.</p>
                <p>
                    <a href="#" className="btn btn-default">Sign up</a>
                </p>
            </div>
        </div>
    </div>
  );
}

export default Home;
