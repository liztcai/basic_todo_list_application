# basic_todo_list_application
This is a basic To Do List web application created with Python, Django, and TailwindCSS (Frontend)
API reference: https://my-json-server.typicode.com/wsh-startup/mock-api (static endpoints). 

Note:
- static endpoints 


System Requirements: 
1. Python 3.4+
2. Django 3+ 


Instructions:
1. Clone or download this repository into your local directiory
2. Go to the directory where this repository is located
3. Run in your terminal: cd basic_todo_list_application
4. Run in your terminal: python manage.py runserver


The following features are successfully implemented when triggered and logged in the file - app.log
The date and time it was triggered, response status_code, and info message when a feature is triggered is also listed in the app.log 

How to use or test:
1. List down all of the tasks in ascending order.
  ->To implement this, just input in the browser the url of the Development Server Django gave (e.g. http://127.0.0.1:8000/)
  
2. View a specific task given the id. 
  ->To implement this, just click the task that you want to browse the details of. The app will redirect to the page where the details for this task is being shown
  
3. Create a new task to be added to the list 
  ->Tto implement this, just input the task you want to input inside the form with the placeholder "Enter new task", then click the "Add" button

4. Update a task.
  ->To implement this, just click the "Update" button on the right-most side of the task line. The app will redirect to the page where the details for this task is being shown and where you can edit the completed status and name of the task.
  
5. Delete a task.
  ->To implement this, just click the "Delete" button on the right-most side of the task line. 
