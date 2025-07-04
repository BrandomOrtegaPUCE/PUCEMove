import React from 'react';
import ViajesList from './components/ViajesList';
import CrearViaje from './components/CrearViaje';

function App() {
  return (
    <div>
      <h1>PUCE Move - Plataforma de Viajes Compartidos</h1>
      <CrearViaje />
      <hr />
      <ViajesList />
    </div>
  );
}

export default App;
