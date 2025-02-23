// filepath: /ai-fitness-coach/app.js
const express = require('express');
const bodyParser = require('body-parser');
const workoutRoutes = require('./routes/workoutRoutes');
const nutritionRoutes = require('./routes/nutritionRoutes');
const progressRoutes = require('./routes/progressRoutes');

const app = express();
app.use(bodyParser.json());

app.use('/api', workoutRoutes);
app.use('/api', nutritionRoutes);
app.use('/api', progressRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log();
});
