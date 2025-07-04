import React from 'react';
import CrearUsuario from './components/CrearUsuario';
import CrearViaje from './components/CrearViaje';
import ViajesList from './components/ViajesList';

function App() {
  return (
    <div>
      <h1>PUCE Move - Plataforma de Viajes Compartidos</h1>
      <CrearUsuario />
      <hr />
      <CrearViaje />
      <hr />
      <ViajesList />
    </div>
  );
}

export default App;
