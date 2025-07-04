import React, { useState, useEffect } from 'react';
import axios from 'axios';

function CrearSolicitud() {
  const [usuarios, setUsuarios] = useState([]);
  const [viajes, setViajes] = useState([]);
  const [formData, setFormData] = useState({
    usuario_id: '',
    viaje_id: '',
    mensaje: ''
  });
  const [mensaje, setMensaje] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/usuarios/')
      .then(res => setUsuarios(res.data));
    axios.get('http://127.0.0.1:8000/api/viajes/')
      .then(res => setViajes(res.data));
  }, []);

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/solicitudes/', formData)
      .then(res => {
        setMensaje('✅ Solicitud enviada correctamente');
        setFormData({ usuario_id: '', viaje_id: '', mensaje: '' });
      })
      .catch(err => {
        console.error(err);
        setMensaje('❌ Error al enviar solicitud');
      });
  };

  return (
    <div>
      <h2>Solicitar unirse a un viaje</h2>
      {mensaje && <p>{mensaje}</p>}
      <form onSubmit={handleSubmit}>
        <label>Usuario:</label><br />
        <select name="usuario_id" value={formData.usuario_id} onChange={handleChange} required>
          <option value="">-- Selecciona tu usuario --</option>
          {usuarios.map(usuario => (
            <option key={usuario.id} value={usuario.id}>
              {usuario.nombre} ({usuario.tipo_usuario_display})
            </option>
          ))}
        </select><br /><br />

        <label>Viaje:</label><br />
        <select name="viaje_id" value={formData.viaje_id} onChange={handleChange} required>
          <option value="">-- Selecciona un viaje --</option>
          {viajes.map(viaje => (
            <option key={viaje.id} value={viaje.id}>
              {viaje.origen} → {viaje.destino} ({viaje.fecha} {viaje.hora})
            </option>
          ))}
        </select><br /><br />

        <label>Mensaje:</label><br />
        <textarea name="mensaje" value={formData.mensaje} onChange={handleChange} /><br /><br />

        <button type="submit">Enviar solicitud</button>
      </form>
    </div>
  );
}

export default CrearSolicitud;
