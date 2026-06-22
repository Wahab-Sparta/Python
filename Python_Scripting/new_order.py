# Python script that accepts a new menu order as an argument, and it appends to orders.txt
# "Bar of Chocolate" - how are spaces handled?
import sys

menu_order = sys.argv
menu_order.pop(0)
file = open("orders.txt", "a+")
for order in menu_order:
    file.write(order+"\n")

file.close()