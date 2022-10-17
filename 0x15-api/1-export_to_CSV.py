#!/usr/bin/python3
"""Exports data in the CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    name = user.get("username")
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userId, name, task.get("completed"), task.get("title")]
         ) for task in todos]
