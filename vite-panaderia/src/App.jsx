import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './HomePage'; // Asegúrate de que la ruta sea correcta
import LoginPage from './LoginPage'; // Asegúrate de que la ruta sea correcta

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} /> {/* Usar "element" en lugar de "component" */}
        <Route path="/login" element={<LoginPage />} /> {/* Usar "element" en lugar de "component" */}
        {/* Puedes agregar más rutas aquí si es necesario */}
      </Routes>
    </Router>
  );
}

export default App;
