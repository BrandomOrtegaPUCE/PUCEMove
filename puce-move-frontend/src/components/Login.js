import React, { useState } from 'react';

function Login({ onLogin }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    const res = await fetch('http://127.0.0.1:8000/api/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    console.log("Respuesta del backend:", data);
    if (res.ok && data.token) {
      onLogin(data.token);
    } else {
      setError('Usuario o contraseña incorrectos');
    }
  };

  return (
    <form className="form" onSubmit={handleSubmit}>
      <h2>Iniciar sesión</h2>
      {error && <div className="error">{error}</div>}
      <input type="text" placeholder="Usuario" value={username} onChange={e => setUsername(e.target.value)} required />
      <input type="password" placeholder="Contraseña" value={password} onChange={e => setPassword(e.target.value)} required />
      <button type="submit">Entrar</button>
    </form>
  );
}

export default Login;