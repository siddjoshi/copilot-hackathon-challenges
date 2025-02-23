// filepath: /ai-fitness-coach/controllers/workoutController.js
const { generateWorkoutPlan } = require('../services/workoutService');

const getWorkoutPlan = (req, res) => {
  const userPreferences = req.body;
  const workoutPlan = generateWorkoutPlan(userPreferences);
  res.json(workoutPlan);
};

module.exports = { getWorkoutPlan };
