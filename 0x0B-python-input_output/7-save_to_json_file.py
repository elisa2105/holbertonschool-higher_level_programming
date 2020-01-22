#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    '''
    Write a JSON object
    '''
    with open(filename, mode='w') as filet7:
        filet7.write(json.dumps(my_obj))
