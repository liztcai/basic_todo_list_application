from django.shortcuts import render, redirect
from django.http import HttpResponse

import requests, json, logging
from datetime import date

logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def index(request):
    r = requests.get('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks')
    tasks = r.json()

    logging.info('Response [%d]: **GET /tasks** successful. Listed all tasks given the specified parameters.', r.status_code)

    data = {'tasks': tasks}
    return render(request, 'tasks/main.html', data)

def show(request, pk):
    r = requests.get('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks?id=' + pk)
    task = r.json()

    logging.info('Response [%d]: Showing details of a task successful.', r.status_code)

    data = {'task': task[0]}
    return render(request, 'tasks/show.html', data)

def store(request):
    re = requests.get('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks')
    tasks = re.json()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        payload = {'title': request.POST['new_task'], 'date': date.today().strftime("%m/%d/%y"), 'completed': False}

        r = requests.post('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks', json=payload)


        logging.info('Response [%d]: **POST /tasks** successful. Created a task given the parameters. Task title - %s', r.status_code, request.POST['new_task'])

        if r.status_code == 201:
            rr = json.loads(r.text)
            res = ' Task - ' + rr['title'] + ' successfully created!'

            data = {'resp': res, 'tasks': tasks}
            return render(request, 'tasks/main.html', data)

def delete(request, pk):
    res = requests.get('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks')
    tasks = res.json()

    re = requests.get('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks?id=' + pk)
    task = re.json()

    r = requests.delete('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks/' + pk)

    logging.info('Response [%d]: **DELETE /tasks/{id}** successful. Deleted a task with the given ID. (Task id - %d, Task title - %s)', r.status_code, task[0]["id"], task[0]["title"])

    if r.status_code == 200:
        res = task[0]["title"] + ' Task - ' + ' successfully deleted!'

        data = {'resp': res, 'tasks': tasks}
        return render(request, 'tasks/main.html', data)

def update(request, pk):
    r = requests.get('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks?id=' + pk)
    task = r.json()

    data = {'task': task[0]}
    return render(request, 'tasks/update.html', data)

def put(request):
    resp = requests.get('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks')
    tasks = resp.json()

    re = requests.get('https://my-json-server.typicode.com/wsh-startup/mock-api/tasks?id=' + request.POST['id'])
    task = re.json()

    if request.method == 'POST':
        payload = {'title': request.POST['updated_task'], 'date': date.today().strftime("%m/%d/%y"), 'completed': request.POST.get('completed', False) }

        url = 'https://my-json-server.typicode.com/wsh-startup/mock-api/tasks/'+request.POST['id']
        r = requests.put(url, json=payload)
        rr = json.loads(r.text)


        logging.info('Response [%d]: **PUT /tasks/{id}** successful. Updated a task details with the given ID. (Task id - %d, Task title - %s)', r.status_code, rr['id'], rr['title'])


        if r.status_code == 200:
            res = 'Task - ' + rr['title'] + ' is successfully updated!'

            data = {'resp': res, 'tasks': tasks}
            return render(request, 'tasks/main.html', data)
