
grocery_list = {}

def add_item(name, quantity):
    grocery_list[name] = quantity
    print(f"Added: {name} - {quantity}")

def remove_item(name):
    if name in grocery_list:
        del grocery_list[name]
        print(f"Removed: {name}")
    else:
        print(f"{name} not found.")

def update_item(name, quantity):
    if name in grocery_list:
        grocery_list[name] = quantity
        print(f"Updated: {name} to {quantity}")
    else:
        print(f"{name} not found.")

def display_sorted_list():
    print("\nSorted Grocery List:")
    for item in sorted(grocery_list):
        print(f"{item} - {grocery_list[item]}")

def display_total_items():
    total = sum(grocery_list.values())
    print(f"\nTotal items: {total}")

# Main loop with match-case
while True:
    print("\nOptions: add, remove, update, display, total, exit")
    action = input("").strip().lower()

    match action:
        case "add":
            name = input("Enter item name: ").strip().lower()
            quantity = int(input("Enter quantity: "))
            add_item(name, quantity)

        case "remove":
            name = input("Enter item name to remove: ").strip().lower()
            remove_item(name)

        case "update":
            name = input("Enter item name to update: ").strip().lower()
            quantity = int(input("Enter new quantity: "))
            update_item(name, quantity)

        case "display":
            display_sorted_list()

        case "total":
            display_total_items()

        case "exit":
            print("Thank You !")
            break

        case _:
            print("Invalid option. Please try again.")
