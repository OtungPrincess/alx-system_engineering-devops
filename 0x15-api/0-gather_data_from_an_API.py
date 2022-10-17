#!/usr/bin/python3
""" for a given employee ID, returns information about
their TODO list progress"""

import requests
import sys


def get_user_todo_list():
    userId = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/%s' % userId
    url2 = '%s/todos' % url
    todos = requests.get(url2).json()
    user = requests.get(url).json()
    completed_todo = []
    for todo in todos:
        if todo.get('completed') is True:
            completed_todo.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}): "
          .format(user.get('name'), len(completed_todo), len(todos)))
    for todo in completed_todo:
        print("\t {}".format(todo))


if __name__ == '__main__':
    todos = get_user_todo_list()
