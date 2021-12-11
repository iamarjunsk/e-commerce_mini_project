import React from 'react'
import './App.css'
import {Search} from "@mui/icons-material"
import {ShoppingCart} from "@mui/icons-material"
import{HorizontalSplit} from "@mui/icons-material"
import{Close} from "@mui/icons-material"
function Navbar() {
    return (
        <div className="navbar">
            <input type="checkbox" id="check" />
            <label htmlFor="checkk">
                <i className="bars"><HorizontalSplit/></i>
                <i className="close"><Close/></i>
            </label>
            <div className="logo">Fashionova</div>
            <div>
                <a className="nav-links" href="">Men</a><a className="nav-links" href="">Woman</a><a className="nav-links" href="">Kids</a>
            </div>
            <div className="searchbar">
            <Search className="searchicon"/>
                <input type="text" placeholder="Search for products brands and more" className="searchbox"
                />
                
            </div>

            <div><button className="btnlogin">Login</button></div>
            <div className="cart">
                <ShoppingCart className="cartlogo"/>
            </div>
            
        </div>
        
        

    )
}

export default Navbar
