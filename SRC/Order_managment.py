import datetime

# Expanded Menu Data with 10 items in each category
menu_items = {
    'veg': [
        {'id': 1, 'name': 'Paneer Butter Masala', 'price': 250, 'ingredients': 'Paneer, Butter, Cream, Spices'},
        {'id': 2, 'name': 'Veg Biryani', 'price': 180, 'ingredients': 'Rice, Mixed Vegetables, Spices'},
        {'id': 3, 'name': 'Palak Paneer', 'price': 230, 'ingredients': 'Spinach, Paneer, Spices'},
        {'id': 4, 'name': 'Dal Makhani', 'price': 200, 'ingredients': 'Black Lentils, Kidney Beans, Butter, Cream'},
        {'id': 5, 'name': 'Vegetable Korma', 'price': 220, 'ingredients': 'Mixed Vegetables, Cashew Paste, Cream'},
        {'id': 6, 'name': 'Aloo Gobi', 'price': 180, 'ingredients': 'Potato, Cauliflower, Spices'},
        {'id': 7, 'name': 'Malai Kofta', 'price': 240, 'ingredients': 'Potato Dumplings, Tomato Gravy, Cream'},
        {'id': 8, 'name': 'Chana Masala', 'price': 190, 'ingredients': 'Chickpeas, Onion, Tomato, Spices'},
        {'id': 9, 'name': 'Vegetable Jalfrezi', 'price': 210, 'ingredients': 'Mixed Vegetables, Bell Peppers, Spices'},
        {'id': 10, 'name': 'Baingan Bharta', 'price': 200, 'ingredients': 'Roasted Eggplant, Onion, Tomato, Spices'},
    ],
    'non_veg': [
        {'id': 11, 'name': 'Chicken Curry', 'price': 300, 'ingredients': 'Chicken, Spices, Coconut Milk'},
        {'id': 12, 'name': 'Mutton Rogan Josh', 'price': 450, 'ingredients': 'Mutton, Spices, Yogurt'},
        {'id': 13, 'name': 'Fish Fry', 'price': 350, 'ingredients': 'Fish, Spices, Oil'},
        {'id': 14, 'name': 'Butter Chicken', 'price': 320, 'ingredients': 'Chicken, Butter, Cream, Tomato'},
        {'id': 15, 'name': 'Prawn Masala', 'price': 400, 'ingredients': 'Prawns, Onion, Tomato, Spices'},
        {'id': 16, 'name': 'Chicken Biryani', 'price': 280, 'ingredients': 'Chicken, Rice, Spices, Saffron'},
        {'id': 17, 'name': 'Tandoori Chicken', 'price': 300, 'ingredients': 'Chicken, Yogurt, Spices'},
        {'id': 18, 'name': 'Fish Curry', 'price': 330, 'ingredients': 'Fish, Coconut Milk, Spices'},
        {'id': 19, 'name': 'Mutton Korma', 'price': 420, 'ingredients': 'Mutton, Yogurt, Cashew Paste, Spices'},
        {'id': 20, 'name': 'Chicken 65', 'price': 280, 'ingredients': 'Chicken, Flour, Spices, Curry Leaves'},
    ],
    'soft_drinks': [
        {'id': 21, 'name': 'Coke', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Caffeine'},
        {'id': 22, 'name': 'Sprite', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Citric Acid'},
        {'id': 23, 'name': 'Fanta', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Orange Flavor'},
        {'id': 24, 'name': 'Pepsi', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Caramel Color'},
        {'id': 25, 'name': 'Mountain Dew', 'price': 55, 'ingredients': 'Carbonated Water, Sugar, Citrus Flavor'},
        {'id': 26, 'name': 'Mirinda', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Orange Flavor'},
        {'id': 27, 'name': 'Limca', 'price': 45, 'ingredients': 'Carbonated Water, Sugar, Lemon-Lime Flavor'},
        {'id': 28, 'name': 'Thumbs Up', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Spice Blend'},
        {'id': 29, 'name': 'Frooti', 'price': 40, 'ingredients': 'Mango Pulp, Water, Sugar'},
        {'id': 30, 'name': 'Appy Fizz', 'price': 45, 'ingredients': 'Carbonated Water, Apple Juice, Sugar'},
    ],
}

# Order Management
orders = []
order_history = []

def create_order(item_name, price, table_number):
    order = {
        'item_name': item_name,
        'price': price,
        'table_number': table_number,
        'status': 'New',
        'timestamp': datetime.datetime.now()
    }
    orders.append(order)
    print(f"{item_name} added to the order for Table {table_number}!")

def view_orders():
    print("\n--- Current Orders ---")
    if orders:
        for idx, order in enumerate(orders, start=1):
            print(f"{idx}. Table: {order['table_number']}, Item: {order['item_name']}, "
                  f"Price: ₹{order['price']}, Status: {order['status']}, "
                  f"Time: {order['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("No active orders!")

def update_order_status(order_index, new_status):
    if 0 <= order_index < len(orders):
        orders[order_index]['status'] = new_status
        print(f"Order status updated to {new_status}")
        if new_status == 'Completed':
            completed_order = orders.pop(order_index)
            order_history.append(completed_order)
    else:
        print("Invalid order index!")

def view_order_history():
    print("\n--- Order History ---")
    if order_history:
        for idx, order in enumerate(order_history, start=1):
            print(f"{idx}. Table: {order['table_number']}, Item: {order['item_name']}, "
                  f"Price: ₹{order['price']}, Status: {order['status']}, "
                  f"Time: {order['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("No order history!")

def display_menu(category):
    print(f"\n--- {category.capitalize()} Menu ---")
    for item in menu_items[category]:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ₹{item['price']}, Ingredients: {item['ingredients']}")
    print("\n")

def order_management():
    while True:
        print("\n--- Order Management ---")
        print("1. View Menu")
        print("2. Create Order")
        print("3. View Current Orders")
        print("4. Update Order Status")
        print("5. View Order History")
        print("6. Back to Staff Menu")
        
        choice = input("Please choose an option (1-6): ")

        if choice == '1':
            category = input("Enter category (veg/non_veg/soft_drinks): ")
            if category in menu_items:
                display_menu(category)
            else:
                print("Invalid category!")
        elif choice == '2':
            item_id = int(input("Enter the item ID to add to order: "))
            table_number = int(input("Enter the table number: "))
            item_found = None
            for category in menu_items:
                for item in menu_items[category]:
                    if item['id'] == item_id:
                        item_found = item
                        break
                if item_found:
                    break
            if item_found:
                create_order(item_found['name'], item_found['price'], table_number)
            else:
                print("Invalid item ID. Please try again.")
        elif choice == '3':
            view_orders()
        elif choice == '4':
            view_orders()
            order_index = int(input("Enter the order index to update: ")) - 1
            new_status = input("Enter new status (Preparing/Ready/Completed): ")
            update_order_status(order_index, new_status)
        elif choice == '5':
            view_order_history()
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

def staff_menu():
    while True:
        print("\n--- Staff Menu ---")
        print("1. Order Management")
        print("2. Logout")
        
        choice = input("Please choose an option (1-2): ")

        if choice == '1':
            order_management()
        elif choice == '2':
            print("Logging out... Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    staff_menu()




