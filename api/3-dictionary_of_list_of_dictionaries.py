#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.

This script fetches the user information and to-do lists for all employees
from the JSONPlaceholder API and exports the data to a JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    data_to_export = {}
    for user in users:
        user_id = user.get("id")
        todos = requests.get(
            url + "todos", params={"userId": user_id}).json()

        data_to_export[str(user_id)] = [
            {
                "username": user.get("username"),
                "task": t.get("title"),
                "completed": t.get("completed")
            }
            for t in todos
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile)
