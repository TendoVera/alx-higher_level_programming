#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for ist in my_list:
            if count < x:
                print(ist, end=" ")
                count += 1
        print()
        return count
    except:
        print("An error occurred")
        return count

my_list = [1, 2, 3, 4, 5]
elements_printed = safe_print_list(my_list, 3)
print("Number of elements printed:", elements_printed)
