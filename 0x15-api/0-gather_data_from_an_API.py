#!/usr/bin/python3
"""
Python script that uses a REST API for a given employee ID and
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    # Validate to make sure that an argument is passed
    if len(argv) != 2:
        print("Usage: python <filename> id")
    else:
        employee_id = argv[1]

    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    url2 = "https://jsonplaceholder.typicode.com/todos?user_Id={}"\
        .format(employee_id)

    # Send get requests to the urls
    response1 = requests.get(url1)
    response2 = requests.get(url2)

    # Check that your requests were successful then process further
    if response1.status_code == 200 and response2.status_code == 200:
        # Extract the employee name
        data1 = response1.json()
        employee_name = data1.get('name')

        # Convert todos data to json format for easy processing
        data2 = response2.json()

        # Process the data to get the total number of todos
        total = len(data2)
        count = 0

        # Loop through the employee todo to count the completed tasks only
        for i in data2:
            if i.get('completed') == True:
                count += 1

        # Print a message with the retrieved values
        print(f"Employee {employee_name} is done with tasks({count}/{total}:")

        # Print the titles of completed tasks
        for i in data2:
            if i.get('completed') == True:
                print(f"\t {i.get('title')}")

    else:
        print("Failed to fetch data for employee_id:", employee_id)
