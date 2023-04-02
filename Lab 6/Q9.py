# WAP to enter the recipes ordered by the customer, in a restaurant, prepare the bill in a proper format.
class Restaurant:
    def __init__(self):
        self.menu = {
            "Pizza": 8.99,
            "Burger": 5.99,
            "Pasta": 9.99,
            "Salad": 6.99,
            "Soup": 4.99
        }
    
    def print_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")
    
    def generate_bill(self, items):
        total = sum(self.menu[item] for item in items)
        print("Bill:")
        print(f"{'Item':<10} {'Price':<10}")
        for item in items:
            print(f"{item:<10} ${self.menu[item]:<10.2f}")
        print(f"{'Total':<10} ${total:<10.2f}")

restaurant = Restaurant()
restaurant.print_menu()

print("Enter the items ordered by the customer, one per line. Enter 'done' when finished.")
ordered_items = []
while True:
    item = input().strip()
    if item == "done":
        break
    if item not in restaurant.menu:
        print(f"{item} is not on the menu. Please enter a valid item.")
    else:
        ordered_items.append(item)

restaurant.generate_bill(ordered_items)
