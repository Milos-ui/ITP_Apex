DROP DATABASE IF EXISTS Login;
CREATE DATABASE Login;
USE Login;
-- Erstelle die Tabelle für Benutzer
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password BINARY(60) NOT NULL
);



