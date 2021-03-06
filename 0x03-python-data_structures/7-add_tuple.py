#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    a_len = len(tuple_a)
    b_len = len(tuple_b)

    if a_len < 2 or b_len < 2:

        # tuple_a check
        # if a hasn't been assigned by the end
        # tuple_a gets assigned to a variable
        if a_len == 0:
            yeet_a = (0, 0)
        elif a_len == 1:
            yeet_a = (tuple_a[0], 0)
        else:
            yeet_a = tuple_a

        # tuple_b check
        # if b hasn't been assigned by the end
        # tuple_b gets assigned to a variable
        if b_len == 0:
            yeet_b = (0, 0)
        elif b_len == 1:
            yeet_b = (tuple_b[0], 0)
        else:
            yeet_b = tuple_b

        add1 = yeet_a[0] + yeet_b[0]
        add2 = yeet_a[1] + yeet_b[1]
        output = (add1, add2)
        return output

    yeet_a = tuple_a
    yeet_b = tuple_b

    add1 = yeet_a[0] + yeet_b[0]
    add2 = yeet_a[1] + yeet_b[1]
    output = (add1, add2)
    return output
