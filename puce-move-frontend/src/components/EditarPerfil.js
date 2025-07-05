import React, { useEffect, useState } from 'react';
import axios from 'axios';

function EditarPerfil() {
  const [perfil, setPerfil] = useState({ tipo_usuario: '' });
  const token = localStorage.getItem('token');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/perfil/', {
      headers: { Authorization: `Token ${token}` }
    }).then(res => setPerfil(res.data));
  }, [token]);

  const handleChange = (e) => {
    setPerfil({ ...perfil, tipo_usuario: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.patch('http://127.0.0.1:8000/api/perfil/', { tipo_usuario: perfil.tipo_usuario }, {
      headers: { Authorization: `Token ${token}` }
    }).then(() => alert('✅ Perfil actualizado'));
  };

  return (
    <div>
      <h2>Editar Perfil</h2>
      <form onSubmit={handleSubmit}>
        <label>Tipo de Usuario:</label>
        <select value={perfil.tipo_usuario} onChange={handleChange}>
          <option value="estudiante">Estudiante</option>
          <option value="docente">Docente</option>
          <option value="administrativo">Administrativo</option>
        </select>
        <br /><br />
        <button type="submit">Guardar Cambios</button>
      </form>
    </div>
  );
}

export default EditarPerfil;
