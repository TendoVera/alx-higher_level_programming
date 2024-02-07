#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    for ist in range(x):
        try:
            print("{}".format(my_list[ist]), end="")
            total += 1
        except IndexError:
            break
    print("")
    return (total)
