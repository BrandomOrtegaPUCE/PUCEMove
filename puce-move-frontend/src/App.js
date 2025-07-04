import React from 'react';
import CrearUsuario from './components/CrearUsuario';
import CrearViaje from './components/CrearViaje';
import ViajesList from './components/ViajesList';
import CrearSolicitud from './components/CrearSolicitud';
import SolicitudesPorViaje from './components/SolicitudesPorViaje';

function App() {
  return (
    <div>
      <h1>PUCE Move - Plataforma de Viajes Compartidos</h1>
      <CrearUsuario />
      <hr />
      <CrearViaje />
      <hr />
      <ViajesList />
      <hr />
      <CrearSolicitud />
      <hr />
      <SolicitudesPorViaje />
    </div>
  );
}

export default App;
