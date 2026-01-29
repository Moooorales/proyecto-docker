const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const app = express();
app.use(express.json());

// Conectamos a la base de datos (Servicio 2 del proyecto)
const db = new sqlite3.Database('./database.db');

// Creamos la tabla para los mensajes
db.run("CREATE TABLE IF NOT EXISTS mensajes (id INTEGER PRIMARY KEY, autor TEXT, mensaje TEXT)");

// RUTA POST: Para guardar datos enviados por el equipo
app.post('/mensaje', (req, res) => {
    const { autor, mensaje } = req.body;
    db.run("INSERT INTO mensajes (autor, mensaje) VALUES (?, ?)", [autor, mensaje], function(err) {
        if (err) return res.status(500).json({ error: err.message });
        res.status(201).json({ status: "Guardado correctamente", id: this.lastID });
    });
});

// RUTA GET /data: Devuelve el array de registros (Requisito del proyecto)
app.get('/data', (req, res) => {
    db.all("SELECT * FROM mensajes", [], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

// RUTA GET /health: Para verificar que el servicio funciona
app.get('/health', (req, res) => res.send("Servicio 1 (Backend) en línea"));

app.listen(3000, () => console.log('Servicio 1 escuchando en el puerto 3000'));
