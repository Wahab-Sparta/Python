# A separate script that accepts a filename (e.g. orders.txt)
# Print out how many times each dish has been ordered

import sys

file = open("orders.txt", "r")

order_dict = {}
for line in (file.readlines()):
    line = line[:-1
    ]
    if line in order_dict:
        order_dict[line] += 1
    else:
        order_dict[line] = 1
print(order_dict)
file.close()