import React from 'react';

function LoginPage() {
    return (
        <div className="login-box">
            <img className="avatar" src="/images/logo_bañico.png" alt="logo panaderia BAÑICO'S" />
            <h1>Acceda aquí</h1>
            <form>
                <label htmlFor="Nombre de usuario">Nombre de Usuario</label>
                <input type="text" placeholder="Ingrese el nombre de usuario" />
                <label htmlFor="Contraseña">Contraseña</label>
                <input type="password" placeholder="Introduzca la Contraseña" />
                <input type="submit" value="Iniciar Sesión" />
                <a href="#">Olvidaste tu contraseña</a><br />
                <a href="#">No tienes cuenta? Regístrate</a>
            </form>
        </div>
    );
}

export default LoginPage;
