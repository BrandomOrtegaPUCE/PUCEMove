import React, { useState } from 'react';
import './App.css';
import Login from './components/Login';
import CrearUsuario from './components/Registro';
import Home from './components/Home';

function App() {
  const [isLogin, setIsLogin] = useState(true); // alterna entre login y registro
  const [token, setToken] = useState(localStorage.getItem('token') || '');

  const handleLogin = (token) => {
    setToken(token);
    localStorage.setItem('token', token);
  };

  const handleLogout = () => {
    setToken('');
    localStorage.removeItem('token');
  };

  if (!token) {
    return (
      <div className="auth-container">
        <h1>PUCE Move</h1>
        {isLogin ? (
          <>
            <Login onLogin={handleLogin} />
            <p>¿No tienes cuenta? <button onClick={() => setIsLogin(false)}>Regístrate</button></p>
          </>
        ) : (
          <>
            <CrearUsuario onRegister={() => setIsLogin(true)} />
            <p>¿Ya tienes cuenta? <button onClick={() => setIsLogin(true)}>Inicia sesión</button></p>
          </>
        )}
      </div>
    );
  } else {
    return (
      <Home token={token} onLogout={handleLogout} />
    );
  }
}

export default App;
