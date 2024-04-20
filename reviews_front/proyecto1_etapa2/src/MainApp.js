import React from 'react';
import { Route, Routes } from 'react-router-dom';
import App from './App';
import ModelView from './ModelView';

function MainApp() {
  return (
    <Routes>
      <Route exact path="/" element={<App />} />
      <Route exact path="/model" element={<ModelView />} />
    </Routes>
  );
}

export default MainApp;
