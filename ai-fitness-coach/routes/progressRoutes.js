// filepath: /ai-fitness-coach/routes/progressRoutes.js
const express = require('express');
const { postProgress, getUser } = require('../controllers/progressController');
const router = express.Router();

router.post('/progress', postProgress);
router.get('/user/:userId', getUser);

module.exports = router;
