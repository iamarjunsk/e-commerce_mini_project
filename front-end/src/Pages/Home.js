import React from 'react'
import Navbar from '../components/Navbar/Navbar';
import Header from '../components/Header/Head';
import Rowpost from '../components/Rowpost/Rowpost';
import Footer from '../components/Footer/Footer';



function Home(props) {
    return (
        
            <div className="homeParentDiv">
          <Navbar/>
          <Header/>
          <Rowpost/>
          <Footer/>
    </div>
        
    )
}

export default Home
