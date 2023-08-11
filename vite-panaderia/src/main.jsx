import React from 'react';
import { createRoot } from 'react-dom/client'; // Corregir la importación aquí
import App from './App.jsx';
import './global.css'; // Importar la hoja de estilos global
import 'bootstrap/dist/css/bootstrap.min.css'; // Importar los estilos CSS de Bootstrap

const container = document.getElementById('root');
const root = createRoot(container);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
