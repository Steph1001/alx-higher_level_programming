#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        i = list(a_dictionary.values()).index(max(a_dictionary.values()))
        return list(a_dictionary.keys())[i]
