const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Servicio 1 (Backend) funcionando - Listo para integración');
});

app.post('/datos', (req, res) => {
    console.log('Servicio 1 recibió datos:', req.body);
    res.json({ estado: "recibido", servicio: 1 });
});

app.listen(PORT, () => {
    console.log(`Servicio 1 escuchando en el puerto ${PORT}`);
});
