import Home from './Pages/Home';
import React from 'react';
import './App.css';
import {BrowserRouter as Router,Route, Routes} from 'react-router-dom'
function App() {
  return (
    <div>
        <Router> 
          <Routes>
        <Route  path='/' element={<Home />}/>
        </Routes>
        </Router>
    </div>
  );
}

export default App;
