#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    for element in my_list:
        unique_set.add(element)
        result_sum = sum(unique_set)

    return result_sum
