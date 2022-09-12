import express from 'express';
import hello from './api/hello.js';

const app = express();

app.use(express.json({ extended: false }));

app.use('/api/hello', hello);

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server is running in port ${PORT}`));