#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

new_list = sys.argv[1:]

try:
    old_list = load_from_json_file("add_item.json")
except:
    old_list = []

old_list.extend(new_list)
save_to_json_file(old_list, "add_item.json")
