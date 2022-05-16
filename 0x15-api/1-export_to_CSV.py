#!/usr/bin/python3
"""Module for taking information out on a json api"""
import csv
import json
import requests
from sys import argv


def get_todos_csv(u_id):
    """Writes the task of an employee into a CSV file"""
    url = 'https://jsonplaceholder.typicode.com/'
    user = json.loads(requests.get('{}users/{}'.format(url, u_id)).text)
    data = requests.get('{}users/{}/todos'.format(url, u_id))
    content = json.loads(data.text)

    keys = ['id', 'name', 'completed', 'title']
    with open('2.csv', 'wt') as file:
        for value in content:
            value['id'] = u_id
            value['name'] = user['name']
        dict_writer = csv.DictWriter(file,
                                     keys,
                                     extrasaction='ignore',
                                     quoting=csv.QUOTE_ALL,
                                     lineterminator='\n')
        dict_writer.writerows(content)


if __name__ == '__main__':
    if len(argv) >= 2:
        get_todos_csv(argv[1])
