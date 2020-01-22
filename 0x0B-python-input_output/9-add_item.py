#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def add_item(arguments, filename):
    '''
    Adds arguments to a Python list and then saves them to a JSON file
    [:param arguments:] the arguments to be added
    [:param filename:] the name of the file to save to
    '''
    try:
        to_save = load_from_json_file(filename)
    except:
        to_save = []

    for arg in arguments:
        to_save.append(arg)
    save_to_json_file(to_save, filename)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    filename = "add_item.json"
    add_item(arguments, filename)
