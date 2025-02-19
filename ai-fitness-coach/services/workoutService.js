// filepath: /ai-fitness-coach/services/workoutService.js
const generateWorkoutPlan = (userPreferences) => {
  const workoutPlan = [
    { day: 'Monday', exercise: 'Push-ups', sets: 3, reps: 15 },
    { day: 'Wednesday', exercise: 'Squats', sets: 3, reps: 20 },
    { day: 'Friday', exercise: 'Plank', duration: '1 minute' }
  ];
  return workoutPlan;
};

module.exports = { generateWorkoutPlan };
