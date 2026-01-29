const express = require('express');
const app = express();
const PORT = 3000;

app.get('/health', (req, res) => {
    res.json({ status: 'UP', message: 'Servicio 1 funcionando' });
});

app.get('/data', (req, res) => {
    res.json({ service: 'Backend', endpoints: ['/health', '/data'] });
});

app.listen(PORT, () => {
    console.log(`Servicio 1 en puerto ${PORT}`);
});
