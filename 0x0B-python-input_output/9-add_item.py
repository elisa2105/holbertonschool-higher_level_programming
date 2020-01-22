#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def add_item(arguments, filename):
    '''
    Adds arguments to a list and save them into JSON file
    [:param arguments:] the arguments
    [:param filename:] the file
    '''
    try:
        save = load_from_json_file(filename)
    except:
        save = []

    for i in arguments:
        save.append(i)
    save_to_json_file(save, filename)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    filename = "add_item.json"
    add_item(arguments, filename)
