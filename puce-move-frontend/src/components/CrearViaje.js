import React, { useState, useEffect } from 'react';
import axios from 'axios';

function CrearViaje() {
  const [usuarios, setUsuarios] = useState([]);
  const [formData, setFormData] = useState({
    conductor_id: '',
    origen: '',
    destino: '',
    fecha: '',
    hora: '',
    cupos_disponibles: ''
  });
  const [mensaje, setMensaje] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/usuarios/')
      .then(res => setUsuarios(res.data))
      .catch(err => console.error('Error cargando usuarios:', err));
  }, []);

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/viajes/', formData)
      .then(res => {
        setMensaje('✅ Viaje creado con éxito');
        setFormData({
          conductor_id: '',
          origen: '',
          destino: '',
          fecha: '',
          hora: '',
          cupos_disponibles: ''
        });
      })
      .catch(err => {
        console.error(err);
        setMensaje('❌ Error al crear el viaje');
      });
  };

  return (
    <div>
      <h2>Crear nuevo viaje</h2>
      {mensaje && <p>{mensaje}</p>}
      <form onSubmit={handleSubmit}>
        <label>Conductor:</label><br />
        <select name="conductor_id" value={formData.conductor_id} onChange={handleChange} required>
          <option value="">-- Selecciona un usuario --</option>
          {usuarios.map(usuario => (
            <option key={usuario.id} value={usuario.id}>
              {usuario.nombre} ({usuario.tipo_usuario_display})
            </option>
          ))}
        </select><br /><br />

        <label>Origen:</label><br />
        <input type="text" name="origen" value={formData.origen} onChange={handleChange} required /><br /><br />

        <label>Destino:</label><br />
        <input type="text" name="destino" value={formData.destino} onChange={handleChange} required /><br /><br />

        <label>Fecha:</label><br />
        <input type="date" name="fecha" value={formData.fecha} onChange={handleChange} required /><br /><br />

        <label>Hora:</label><br />
        <input type="time" name="hora" value={formData.hora} onChange={handleChange} required /><br /><br />

        <label>Cupos disponibles:</label><br />
        <input type="number" name="cupos_disponibles" min="1" value={formData.cupos_disponibles} onChange={handleChange} required /><br /><br />

        <button type="submit">Crear viaje</button>
      </form>
    </div>
  );
}

export default CrearViaje;
