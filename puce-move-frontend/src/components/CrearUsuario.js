import React, { useState } from 'react';
import axios from 'axios';

function CrearUsuario() {
  const [formData, setFormData] = useState({
    nombre: '',
    correo: '',
    tipo_usuario: ''
  });

  const [mensaje, setMensaje] = useState('');

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/usuarios/', formData)
      .then(res => {
        setMensaje('✅ Usuario registrado correctamente');
        setFormData({ nombre: '', correo: '', tipo_usuario: '' });
      })
      .catch(err => {
        console.error(err);
        setMensaje('❌ Error al registrar usuario');
      });
  };

  return (
    <div>
      <h2>Registrar nuevo usuario</h2>
      {mensaje && <p>{mensaje}</p>}
      <form onSubmit={handleSubmit}>
        <label>Nombre:</label><br />
        <input type="text" name="nombre" value={formData.nombre} onChange={handleChange} required /><br /><br />

        <label>Correo:</label><br />
        <input type="email" name="correo" value={formData.correo} onChange={handleChange} required /><br /><br />

        <label>Tipo de usuario:</label><br />
        <select name="tipo_usuario" value={formData.tipo_usuario} onChange={handleChange} required>
          <option value="">-- Selecciona una opción --</option>
          <option value="estudiante">Estudiante</option>
          <option value="docente">Docente</option>
          <option value="administrativo">Administrativo</option>
        </select><br /><br />

        <button type="submit">Registrar usuario</button>
      </form>
    </div>
  );
}

export default CrearUsuario;
