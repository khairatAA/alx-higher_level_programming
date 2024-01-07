#!/usr/bin/node
// 6-completed_tasks.js

// computes the number of tasks completed by user id
const request = require('request');
const processArgv = require('process').argv;

request(processArgv[2], function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const responseData = JSON.parse(body);
    const taskCompleted = {};

    for (let i = 0; i < responseData.length; i++) {
      const task = responseData[i];

      if (task.completed === true) {
        if (task.userId in taskCompleted) {
          taskCompleted[task.userId]++;
        } else {
          taskCompleted[task.userId] = 1;
        }
      }
    }
    console.log(taskCompleted);
  }
});
