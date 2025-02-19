#!/bin/bash

# Create directories
mkdir -p ai-fitness-coach/controllers
mkdir -p ai-fitness-coach/services
mkdir -p ai-fitness-coach/routes
mkdir -p ai-fitness-coach/data

# Create files with initial content
echo "// filepath: /ai-fitness-coach/controllers/workoutController.js
const { generateWorkoutPlan } = require('../services/workoutService');

const getWorkoutPlan = (req, res) => {
  const userPreferences = req.body;
  const workoutPlan = generateWorkoutPlan(userPreferences);
  res.json(workoutPlan);
};

module.exports = { getWorkoutPlan };" > ai-fitness-coach/controllers/workoutController.js

echo "// filepath: /ai-fitness-coach/controllers/nutritionController.js
const { generateMealPlan } = require('../services/nutritionService');

const getMealPlan = (req, res) => {
  const dietaryPreferences = req.body;
  const mealPlan = generateMealPlan(dietaryPreferences);
  res.json(mealPlan);
};

module.exports = { getMealPlan };" > ai-fitness-coach/controllers/nutritionController.js

echo "// filepath: /ai-fitness-coach/controllers/progressController.js
const { trackProgress } = require('../services/progressService');

const postProgress = (req, res) => {
  const { userId, progressData } = req.body;
  trackProgress(userId, progressData);
  res.status(200).send('Progress tracked successfully');
};

module.exports = { postProgress };" > ai-fitness-coach/controllers/progressController.js

echo "// filepath: /ai-fitness-coach/services/workoutService.js
const generateWorkoutPlan = (userPreferences) => {
  const workoutPlan = [
    { day: 'Monday', exercise: 'Push-ups', sets: 3, reps: 15 },
    { day: 'Wednesday', exercise: 'Squats', sets: 3, reps: 20 },
    { day: 'Friday', exercise: 'Plank', duration: '1 minute' }
  ];
  return workoutPlan;
};

module.exports = { generateWorkoutPlan };" > ai-fitness-coach/services/workoutService.js

echo "// filepath: /ai-fitness-coach/services/nutritionService.js
const generateMealPlan = (dietaryPreferences) => {
  const mealPlan = [
    { day: 'Monday', meal: 'Grilled Chicken Salad' },
    { day: 'Tuesday', meal: 'Quinoa and Veggie Stir-fry' },
    { day: 'Wednesday', meal: 'Salmon with Brown Rice' }
  ];
  return mealPlan;
};

module.exports = { generateMealPlan };" > ai-fitness-coach/services/nutritionService.js

echo "// filepath: /ai-fitness-coach/services/progressService.js
const fs = require('fs');
const path = require('path');
const dataPath = path.join(__dirname, '../data/users.json');

const trackProgress = (userId, progressData) => {
  const users = JSON.parse(fs.readFileSync(dataPath, 'utf8')).users;
  const user = users.find(user => user.id === userId);
  if (user) {
    user.progress.push(progressData);
    fs.writeFileSync(dataPath, JSON.stringify({ users }, null, 2));
  }
};

module.exports = { trackProgress };" > ai-fitness-coach/services/progressService.js

echo "// filepath: /ai-fitness-coach/routes/workoutRoutes.js
const express = require('express');
const { getWorkoutPlan } = require('../controllers/workoutController');
const router = express.Router();

router.post('/workout-plan', getWorkoutPlan);

module.exports = router;" > ai-fitness-coach/routes/workoutRoutes.js

echo "// filepath: /ai-fitness-coach/routes/nutritionRoutes.js
const express = require('express');
const { getMealPlan } = require('../controllers/nutritionController');
const router = express.Router();

router.post('/meal-plan', getMealPlan);

module.exports = router;" > ai-fitness-coach/routes/nutritionRoutes.js

echo "// filepath: /ai-fitness-coach/routes/progressRoutes.js
const express = require('express');
const { postProgress } = require('../controllers/progressController');
const router = express.Router();

router.post('/progress', postProgress);

module.exports = router;" > ai-fitness-coach/routes/progressRoutes.js

echo "// filepath: /ai-fitness-coach/data/users.json
{
  \"users\": []
}" > ai-fitness-coach/data/users.json

echo "// filepath: /ai-fitness-coach/app.js
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
  console.log(`Server is running on port `);
});" > ai-fitness-coach/app.js

echo "// filepath: /ai-fitness-coach/package.json
{
  \"name\": \"ai-fitness-coach\",
  \"version\": \"1.0.0\",
  \"description\": \"AI-Driven Health and Fitness Coach\",
  \"main\": \"app.js\",
  \"scripts\": {
    \"start\": \"node app.js\"
  },
  \"dependencies\": {
    \"body-parser\": \"^1.19.0\",
    \"express\": \"^4.17.1\",
    \"fs\": \"0.0.1-security\"
  }
}" > ai-fitness-coach/package.json

echo "// filepath: /ai-fitness-coach/README.md
# AI-Driven Health and Fitness Coach

## Overview
This project is an AI-powered health and fitness coach that provides personalized workout plans, nutrition advice, and progress tracking.

## Features
- Personalized workout plans
- Nutrition advice based on dietary preferences
- Progress tracking with visualizations
- Integration with wearable devices (future enhancement)

## Setup
1. Clone the repository
2. Install dependencies: \`npm install\`
3. Start the server: \`npm start\`
4. Use Postman or any API client to interact with the endpoints

## Endpoints
- \`POST /api/workout-plan\`: Generate a personalized workout plan
- \`POST /api/meal-plan\`: Generate a personalized meal plan
- \`POST /api/progress\`: Track user progress

## Example Requests
### Generate Workout Plan
\`\`\`json
POST /api/workout-plan
{
  \"fitnessLevel\": \"beginner\",
  \"goals\": [\"strength\", \"endurance\"]
}
\`\`\`

### Generate Meal Plan
\`\`\`json
POST /api/meal-plan
{
  \"dietaryPreferences\": [\"vegetarian\"]
}
\`\`\`

### Track Progress
\`\`\`json
POST /api/progress
{
  \"userId\": \"123\",
  \"progressData\": {
    \"date\": \"2025-02-19\",
    \"weight\": 70,
    \"bodyFatPercentage\": 20
  }
}
\`\`\`

## Running the Project
1. Ensure you have Node.js installed.
2. Navigate to the project directory and install dependencies:
   \`\`\`bash
   npm install
   \`\`\`
3. Start the server:
   \`\`\`bash
   npm start
   \`\`\`
4. Use an API client like Postman to interact with the endpoints." > ai-fitness-coach/README.md

echo "Project structure and files created successfully."