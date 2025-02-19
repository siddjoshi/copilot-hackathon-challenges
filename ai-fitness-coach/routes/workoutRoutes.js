// filepath: /ai-fitness-coach/routes/workoutRoutes.js
const express = require('express');
const { getWorkoutPlan } = require('../controllers/workoutController');
const router = express.Router();

router.post('/workout-plan', getWorkoutPlan);

module.exports = router;
