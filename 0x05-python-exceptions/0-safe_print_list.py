#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elementcount = 0    # Counter to count the number of elements printed

    for elements in range(x):
        try:
            print(my_list[elements], end='')
            elementcount += 1

        except IndexError:
                break
    print()

    return elementcount  # Return the number of elements successfully parsed
