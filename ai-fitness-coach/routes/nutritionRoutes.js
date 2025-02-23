// filepath: /ai-fitness-coach/routes/nutritionRoutes.js
const express = require('express');
const { getMealPlan } = require('../controllers/nutritionController');
const router = express.Router();

router.post('/meal-plan', getMealPlan);

module.exports = router;
