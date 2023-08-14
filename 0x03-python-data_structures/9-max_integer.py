#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for bigger in range(len(my_list)):
        if my_list[bigger] > biggest:
            biggest = my_list[bigger]
            return (biggest)
