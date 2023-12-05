#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    def get_element(t, index):
        return t[index] if len(t) > index else 0

    new_tuple = (get_element(tuple_a, 0) + get_element(tuple_b, 0),
                 get_element(tuple_a, 1) + get_element(tuple_b, 1))
    return new_tuple
