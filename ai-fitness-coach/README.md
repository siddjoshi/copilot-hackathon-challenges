// filepath: /ai-fitness-coach/README.md
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
2. Install dependencies: `npm install`
3. Start the server: `npm start`
4. Use Postman or any API client to interact with the endpoints

## Endpoints
- `POST /api/workout-plan`: Generate a personalized workout plan
- `POST /api/meal-plan`: Generate a personalized meal plan
- `POST /api/progress`: Track user progress
- `GET /api/user/:userId`: Get user data if exists

## Example Requests
### Generate Workout Plan
```json
POST /api/workout-plan
{
  "fitnessLevel": "beginner",
  "goals": ["strength", "endurance"]
}
```

### Generate Meal Plan
```json
POST /api/meal-plan
{
  "dietaryPreferences": ["vegetarian"]
}
```

### Track Progress
```json
POST /api/progress
{
  "userId": "123",
  "progressData": {
    "date": "2025-02-19",
    "weight": 70,
    "bodyFatPercentage": 20
  }
}
```

### Get User Data
```json
GET /api/user/123
```

## Running the Project
1. Ensure you have Node.js installed.
2. Navigate to the project directory and install dependencies:
   ```bash
   npm install
   ```
3. Start the server:
   ```bash
   npm start
   ```
4. Use an API client like Postman to interact with the endpoints.
