#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        if (completed[userId] === undefined) {
          completed[userId] = 1;
        } else {
          completed[userId] += 1;
        }
      }
    });

    console.log(completed);
  }
});
