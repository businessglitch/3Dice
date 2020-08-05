import React from 'react'
import { Link } from 'react-router-dom'
import PropTypes from 'prop-types'

function Footer(props) {
    return (
        <div className="md-margin-top">
            <footer className="footer text-center">
                <div className="container">
                    <ul className="list-inline">
                    <li className="text-muted">Snake Eyes &copy; 2016</li>
                    <li><Link to="/privacy">Privacy Policy</Link></li>
                    <li><Link to="/terms">Terms of Service</Link></li>
                    </ul>
                </div>
            </footer>
        </div>
    )
}

Footer.propTypes = {

}

export default Footer

