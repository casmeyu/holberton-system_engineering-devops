#!/usr/bin/python3
"""Module for taking information out on a json api"""
import csv
import json
import requests
from sys import argv


def get_todos_json(u_id):
    """"Writes the tasks of an employee into a JSON file"""
    url = 'https://jsonplaceholder.typicode.com/'
    user = json.loads(requests.get('{}users/{}'.format(url, u_id)).text)
    data = requests.get('{}users/{}/todos'.format(url, u_id))
    content = json.loads(data.text)

    keys = ['id', 'name', 'completed', 'title']
    with open('2.json', 'wt') as file:
        dict_list = []
        aux_dict = {}
        aux_dict[u_id] = []
        for value in content:
            task_dict = {}
            task_dict['task'] = value['title']
            task_dict['completed'] = value['completed']
            task_dict['username'] = user['name']
            aux_dict[u_id].append(task_dict)

        json.dump(aux_dict, file)


if __name__ == '__main__':
    if len(argv) >= 2:
        get_todos_json(2)
