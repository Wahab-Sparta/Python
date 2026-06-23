#OPTIONAL BONUS: Can you update the files above so that we can track the orders submitted by a particular table
# e.g. Table #12? You might want to use a different filetype instead of txt!

import sys
import json

filename = sys.argv[1]
table_number = str(sys.argv[2])
new_order = sys.argv[3]

with open(filename, "r") as jsonfile:
    orders = json.load(jsonfile)

with open(filename, "w") as jsonfile:
    if table_number in orders:
        orders[table_number].append(new_order)
    else:
        orders[table_number] = [new_order]
    json.dump(orders, jsonfile)



