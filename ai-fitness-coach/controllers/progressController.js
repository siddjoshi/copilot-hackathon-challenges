// filepath: /ai-fitness-coach/controllers/progressController.js
const { trackProgress, getUserData } = require('../services/progressService');

const postProgress = (req, res) => {
  const { userId, progressData } = req.body;
  trackProgress(userId, progressData);
  res.status(200).send('Progress tracked successfully');
};
const getUser = (req, res) => {
  const { userId } = req.params;
  const user = getUserData(userId);
  if (user) {
    res.json(user);
  } else {
    res.status(404).send('User not found');
  }
};

module.exports = { postProgress, getUser };
