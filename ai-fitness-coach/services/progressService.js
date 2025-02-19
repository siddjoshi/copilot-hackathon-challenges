// filepath: /ai-fitness-coach/services/progressService.js
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

const getUserData = (userId) => {
  const users = JSON.parse(fs.readFileSync(dataPath, 'utf8')).users;
  return users.find(user => user.id === userId);
};

module.exports = { trackProgress, getUserData };
