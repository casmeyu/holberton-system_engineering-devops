#!/usr/bin/python3
"""Module for taking information out on a json api"""
import csv
import json
import requests
from sys import argv


def get_todos_json():
    """Writes the tasks of all the users into a JSON file"""
    url = 'https://jsonplaceholder.typicode.com/'
    users = json.loads(requests.get('{}users/'.format(url)).text)

    keys = ['id', 'name', 'completed', 'title']
    aux_list = []
    with open('todo_all_employees.json', 'wt') as file:
        for u in users:
            todo_list = requests.get('{}users/{}/todos'.format(url, u['id']))
            todo_list = json.loads(todo_list.text)
            user_dict = {}
            user_dict[u['id']] = []
            for value in todo_list:
                task_dict = {}
                task_dict['task'] = value['title']
                task_dict['completed'] = value['completed']
                task_dict['username'] = u['name']
                user_dict[u['id']].append(task_dict)

            aux_list.append(user_dict)

        json.dump(aux_list, file)


if __name__ == '__main__':
    get_todos_json()
