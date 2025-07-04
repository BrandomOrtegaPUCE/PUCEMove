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
        {viajes.map(v => (
          <li key={v.id}>
            {v.origen} → {v.destino} | {v.fecha} {v.hora} | Cupos: {v.cupos_disponibles}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ViajesList;
