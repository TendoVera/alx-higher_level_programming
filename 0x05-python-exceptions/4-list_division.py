#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    the_list = []
    for item in range(0, list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            the_list.append(result)
    return (the_list)
