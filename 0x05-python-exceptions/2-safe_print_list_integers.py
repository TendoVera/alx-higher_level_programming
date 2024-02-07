#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real = 0
    for ist in range(0, x):
        try:
            print("{:d}".format(my_list[ist]), end="")
            real += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (real)
