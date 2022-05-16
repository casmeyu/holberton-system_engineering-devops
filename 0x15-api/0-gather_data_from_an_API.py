#!/usr/bin/env python3
"""Module for taking information out on a json api"""
import json
import requests
from sys import argv


def get_todos(u_id):
    """Prints all the task done by the employee"""
    url = 'https://jsonplaceholder.typicode.com/'
    user = json.loads(requests.get('{}users/{}'.format(url, u_id)).text)
    data = requests.get('{}users/{}/todos'.format(url, u_id))
    content = json.loads(data.text)

    n_tasks = 0
    n_finish = 0
    todo = []
    for value in content:
        if value['completed'] is True:
            n_finish += 1
            todo.append(value)
        n_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(user['name'],
                                                          n_finish,
                                                          n_tasks))
    for task in todo:
        print('\t {}'.format(task['title']))


if __name__ == '__main__':
    if len(argv) >= 2:
        get_todos(argv[1])
