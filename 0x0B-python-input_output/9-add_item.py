#!/usr/bin/python3
import sys
sjson_file = __import__('7-save_to_json_file').save_to_json_file
ljson_file = __import__('8-load_from_json_file').load_from_json_file


def add_item(arguments, filename):
    '''
    Adds arguments to a list and save them into JSON file
    [:param arguments:] the arguments
    [:param filename:] the file
    '''
    try:
        save = ljson_file(filename)
    except:
        save = []

    for arg in arguments:
        save.append(arg)
    sjson_file(save, filename)

if __name__ == "__main__":
    arguments = sys.argv[1:]
    filename = "add_item.json"
    add_item(arguments, filename)
