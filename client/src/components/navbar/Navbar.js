import React from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom'

const Navbar = props => {
    return (
        <div>
            <nav className="navbar navbar-default navbar-fixed-top">
                <div className="container">
                    <p><Link to="/">Home</Link></p>
                    <div className="navbar-header">
                        <button type="button" className="navbar-toggle collapsed"
                                data-toggle="collapse" data-target="#navbar"
                                aria-expanded="false" aria-controls="navbar">
                            <span className="sr-only">Toggle navigation</span>
                            <span className="icon-bar"></span>
                            <span className="icon-bar"></span>
                            <span className="icon-bar"></span>
                        </button>
                    </div>
                </div>
            </nav>
        </div>
    )
}

Navbar.propTypes = {

}

export default Navbar
