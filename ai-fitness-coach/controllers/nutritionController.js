// filepath: /ai-fitness-coach/controllers/nutritionController.js
const { generateMealPlan } = require('../services/nutritionService');

const getMealPlan = (req, res) => {
  const dietaryPreferences = req.body;
  const mealPlan = generateMealPlan(dietaryPreferences);
  res.json(mealPlan);
};

module.exports = { getMealPlan };
