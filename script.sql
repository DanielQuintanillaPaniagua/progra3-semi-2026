
CREATE DATABASE IF NOT EXISTS db_academica;
USE db_academica;

CREATE TABLE IF NOT EXISTS usuarios_usss022525 (
    idUsuario INT(10) AUTO_INCREMENT PRIMARY KEY,
    usuario CHAR(35) NOT NULL UNIQUE,
    clave CHAR(35) NOT NULL,
    nombre CHAR(85) NOT NULL,
    direccion CHAR(100),
    telefono CHAR(9)
);

CREATE TABLE IF NOT EXISTS clientes (
    idCliente INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(150),
    telefono VARCHAR(20),
    email VARCHAR(100),
    tipo ENUM('particular','empresa') DEFAULT 'particular'
);

CREATE TABLE IF NOT EXISTS productos (
    idProducto INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    descripcion VARCHAR(150) NOT NULL,
    estado ENUM('activo','inactivo') DEFAULT 'activo'
);


INSERT INTO usuarios_usss022525 (usuario, clave, nombre) 
VALUES ('admin', '123', 'Administrador') 
ON DUPLICATE KEY UPDATE nombre='Administrador';
