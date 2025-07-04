import React, { useEffect, useState } from 'react';
import axios from 'axios';

function SolicitudesPorViaje() {
  const [solicitudes, setSolicitudes] = useState([]);

  const cargarSolicitudes = () => {
    axios.get('http://127.0.0.1:8000/api/solicitudes/')
      .then(res => setSolicitudes(res.data))
      .catch(err => console.error('Error al cargar solicitudes', err));
  };

  useEffect(() => {
    cargarSolicitudes();
  }, []);

  const actualizarEstado = (id, nuevoEstado) => {
    axios.patch(`http://127.0.0.1:8000/api/solicitudes/${id}/`, { estado: nuevoEstado })
      .then(() => cargarSolicitudes())
      .catch(err => console.error('Error al actualizar solicitud', err));
  };

  const solicitudesAgrupadas = solicitudes.reduce((acc, solicitud) => {
    const viajeId = solicitud.viaje.id;
    if (!acc[viajeId]) {
      acc[viajeId] = {
        viaje: solicitud.viaje,
        solicitudes: [],
      };
    }
    acc[viajeId].solicitudes.push(solicitud);
    return acc;
  }, {});

  return (
    <div>
      <h2>Solicitudes por Viaje</h2>
      {Object.values(solicitudesAgrupadas).map(({ viaje, solicitudes }) => (
        <div key={viaje.id} style={{ border: '1px solid #ccc', padding: '1rem', marginBottom: '1rem' }}>
          <h3>{viaje.origen} → {viaje.destino} ({viaje.fecha} {viaje.hora})</h3>
          <ul>
            {solicitudes.map(s => (
              <li key={s.id}>
                <strong>{s.usuario.nombre}</strong> ({s.usuario.tipo_usuario_display}) – <em>{s.estado}</em><br />
                {s.mensaje && <p>📝 {s.mensaje}</p>}
                {s.estado === 'pendiente' && (
                  <>
                    <button onClick={() => actualizarEstado(s.id, 'aceptada')}>✅ Aceptar</button>
                    <button onClick={() => actualizarEstado(s.id, 'rechazada')}>❌ Rechazar</button>
                  </>
                )}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default SolicitudesPorViaje;
