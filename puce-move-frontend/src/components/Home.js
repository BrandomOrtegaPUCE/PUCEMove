import React from 'react';
import ViajesList from './ViajesList';
import CrearViaje from './CrearViaje';
import CrearSolicitud from './CrearSolicitud';
import SolicitudesPorViaje from './SolicitudesPorViaje';

function Home({ token, onLogout }) {
  return (
    <div className="main-container">
      <header>
        <h2>Bienvenido a PUCE Move</h2>
        <button onClick={onLogout}>Cerrar sesión</button>
      </header>
      <section>
        <ViajesList token={token} />
        <CrearSolicitud token={token} />
        <SolicitudesPorViaje token={token} />
      </section>
    </div>
  );
}

export default Home;