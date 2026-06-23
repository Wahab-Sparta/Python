import subprocess
import json
run_file = "Python_Scripting/3rd_challenge.py"
order_file = "Python_Scripting/orders.json"
table_number = "3"
order = "Pizza"

def remove_items(table_number):
    with open(order_file, "r") as jsonfile:
        orders = json.load(jsonfile)
    orders.pop(table_number)
    with open(order_file, "w") as jsonfile:
        json.dump(orders, jsonfile)


def test_3rd_challenge():
    subprocess.run(["python", run_file, order_file, table_number, order])
    with open(order_file) as jsonfile:
        contents = json.load(jsonfile)
        assert contents == {
            "1": ["Bar of Chocolate", "Sushi", "Tea", "Coffee"],
            "6": ["Cheeseburger", "Fries", "Mozzarella Sticks", "Coffee", "Salad"],
            "12": ["Garlic Bread", "Pepperoni Pizza", "Coffee"],
            "3" : ["Pizza"]
        }
    remove_items(table_number)


