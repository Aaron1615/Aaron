'''

Exercise 5

Compare two lists, returning a list which only contains
the common elements between the two lists (without duplicates).

Extra Credit:
1. Use randomly generated lists



'''

from random import randrange


def list_random(x):
    return ([randrange(0, 50, 1) for i in range(x)])


a1 = list_random(50)
b1 = list_random(50)


def list_compare(l1,l2):
    final_list = []
    for x in l1:
        for y in l2:
            if y in l1 and y not in final_list:
                final_list.append(y)
    return (final_list)

print(list_compare(a1, b1))
    