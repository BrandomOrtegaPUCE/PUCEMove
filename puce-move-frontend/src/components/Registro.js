import React, { useState } from 'react';
import axios from 'axios';

function Registro() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  });
  const [mensaje, setMensaje] = useState('');
  const [tipoUsuario, setTipoUsuario] = useState('');

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('http://127.0.0.1:8000/api/registro/', { 
        ...formData, 
        tipo_usuario: tipoUsuario // <-- usa el nombre correcto
      })
      .then(res => {
        setMensaje('✅ Usuario creado correctamente');
        setFormData({ username: '', email: '', password: '' });
        setTipoUsuario('');
      })
      .catch(err => {
        console.error(err);
        if (err.response && err.response.data) {
          setMensaje('❌ ' + (err.response.data.error || 'Error al crear usuario'));
        } else {
          setMensaje('❌ Error de red. Asegúrate de que el servidor esté encendido.');
        }
      });
  };

  return (
    <div>
      <h2>Registro de Usuario</h2>
      {mensaje && <p>{mensaje}</p>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Nombre de usuario"
          value={formData.username}
          onChange={handleChange}
          required
        /><br /><br />
        <input
          type="email"
          name="email"
          placeholder="Correo electrónico"
          value={formData.email}
          onChange={handleChange}
          required
        /><br /><br />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          value={formData.password}
          onChange={handleChange}
          required
        /><br /><br />
        <select value={tipoUsuario} onChange={e => setTipoUsuario(e.target.value)} required>
          <option value="">Selecciona tipo de usuario</option>
          <option value="docente">Docente</option>
          <option value="estudiante">Estudiante</option>
        </select><br /><br />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
}

export default Registro;
