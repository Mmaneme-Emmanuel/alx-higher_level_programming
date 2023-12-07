#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for sor_item in sorted(a_dictionary.keys()):
        print("{}: {}".format(sor_item, a_dictionary[sor_item]))
