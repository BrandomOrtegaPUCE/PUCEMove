import React, { useEffect, useState } from 'react';
import axios from 'axios';

function ViajesList() {
  const [viajes, setViajes] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/viajes/')
      .then(res => setViajes(res.data))
      .catch(err => console.error('Error al cargar viajes:', err));
  }, []);

  return (
    <div>
      <h2>Lista de Viajes</h2>
      <ul>
        {viajes.map(viaje => (
          <li key={viaje.id} style={{ marginBottom: '1rem' }}>
            <strong>{viaje.origen} → {viaje.destino}</strong><br />
            Fecha: {viaje.fecha} - Hora: {viaje.hora}<br />
            Cupos disponibles: {viaje.cupos_disponibles}<br />
            <em>Pasajeros:</em>
            <ul>
              {viaje.pasajeros && viaje.pasajeros.length > 0 ? (
                viaje.pasajeros.map(p => (
                  <li key={p.id}>{p.nombre}</li>
                ))
              ) : (
                <li>Sin pasajeros aún</li>
              )}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ViajesList;
