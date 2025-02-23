// filepath: /ai-fitness-coach/services/nutritionService.js
const generateMealPlan = (dietaryPreferences) => {
  const mealPlan = [
    { day: 'Monday', meal: 'Grilled Chicken Salad' },
    { day: 'Tuesday', meal: 'Quinoa and Veggie Stir-fry' },
    { day: 'Wednesday', meal: 'Salmon with Brown Rice' }
  ];
  return mealPlan;
};

module.exports = { generateMealPlan };
