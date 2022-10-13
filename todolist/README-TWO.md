# Assignment 6: Javascript and AJAX

[Link to Site]: https://pbp-web-assignment.herokuapp.com
[site]: https://pbp-web-assignment.herokuapp.com

[Link to Site]

## Asynchronous Programming vs Synchronous Programming

Asynchronous and synchronous programming have different implementations in various languages. But for the context of this assignment, asynchronous typically doesn't block a
thread's execution, in the sense that when a program is executing a heavy process, it will not the block the thread for other segments of the code and they can run
while the heavy process is being executed. If this other segments depends on the heavy process before, then it too will not block the thread and let other parts of the program
to run. Once, the heavy process is done, control of the thread returns to the heavy process and it resumes its way normally. On the other hand, synchronous blocks a thread's
execution if a heavy process is taking place. It will wait until that process is finished before resuming the program.

Asynchronous allows programs independent of each other to run together due to its non-blocking trait. This could be implemented in a single-threaded environment 
or multi-threaded.

## Event-Driven Programming

It's a paradigm in which aspects of the program is run and triggered by events. It's execution focuses on handling the events its designed to handle. These events can be
messages from other servers, user clicks, sensor detection, etc. An example is the `submit` event listener which listens and handles a form submission. This is shown in the
`Add Task` or `Create Task` button.

## Asynchronous Programming in AJAX

1. Typically consists of adding a `<script>` tag to the head of our html document which sources a JavaScript file. This will expose the functions and variables inside of
   the file for use in the HTML document.
2. In modern browsers, we can use the Fetch API to do AJAX requests such as POST, GET, PUT, etc.
3. If we want to implement a form submission which will do an AJAX POST request, we can assign a function as the event handler to the form's `submit` event. We can then
   get the form data in the function and use it as the request body and do an AJAX POST request using the Fetch API.
4. We can show data asynchronously without having to reload the page every time by triggering an event that will re-render the data needed by using a JavaScript function which
   makes an AJAX GET request to fetch the data.
   
## Implementing the checklists

1. Create a new JavaScript file for our functions. (e.g. `static/js/script.js`)
2. Add the script to the head of the base HTML document so it will be exposed to every other HTML document using the base template.
3. Create new view (`todolist_json`) which returns all todolist items in JSON and add it to the urlpatterns for `todolist` (`/todolist/json`).
4. Add a `renderTodolist` handler to fetch the tasks using AJAX GET and render it in the `todolist.html`. Modify the `todolist.html` to accommodate this.
5. Add an `updateTodolistItem` and `deleteTask` function which will use AJAX PUT and DELETE to handle updating the task status and deletion and add it to the task card.
6. Modify the existing `Create Task` button on the `/todolist` page to show a modal for creating a task.
7. Create the HTML form for creating tasks in the modal.
8. Create a view (`add_task`) which will handle the creation of a task and add it to the `todolist` urlpatterns (`/todolist/add`).
9. Add a `createTask` function which will use AJAX POST to send the request to create a task to the `/todolist/add` endpoint.
10. Reset the form on submission, close the modal, and call the `renderTodolist` function to re-render the tasks again after creation without reloading the page.
