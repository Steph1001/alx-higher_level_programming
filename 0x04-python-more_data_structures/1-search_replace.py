#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        return [i if i != search else replace for i in my_list]
