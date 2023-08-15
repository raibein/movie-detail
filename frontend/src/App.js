import React from 'react';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import './App.css';


// import all pages and rounting here
import DefaultContainer from './Containers/DefaultContainer';
import MovieByIdContainer from './Containers/MovieByIdContainer';



function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<DefaultContainer/>}/>
        <Route exact path="/movie/:id" element={<MovieByIdContainer/>}/>
      </Routes>
    </Router>
  );
}

export default App;
