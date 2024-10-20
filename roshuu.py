import datetime

# Example Menu Data
menu_items = {
    'veg': [
        {'id': 1, 'name': 'Paneer Butter Masala', 'price': 250, 'ingredients': 'Paneer, Butter, Cream, Spices'},
        {'id': 2, 'name': 'Veg Biryani', 'price': 180, 'ingredients': 'Rice, Mixed Vegetables, Spices'},
        {'id': 3, 'name': 'Palak Paneer', 'price': 230, 'ingredients': 'Spinach, Paneer, Spices'},
        {'id': 4, 'name': 'Aloo Gobi', 'price': 150, 'ingredients': 'Potatoes, Cauliflower, Spices'},
        {'id': 5, 'name': 'Matar Paneer', 'price': 200, 'ingredients': 'Peas, Paneer, Spices'},
        {'id': 6, 'name': 'Chana Masala', 'price': 160, 'ingredients': 'Chickpeas, Spices, Tomatoes'},
    ],
    'non_veg': [
        {'id': 7, 'name': 'Chicken Curry', 'price': 300, 'ingredients': 'Chicken, Spices, Coconut Milk'},
        {'id': 8, 'name': 'Mutton Rogan Josh', 'price': 450, 'ingredients': 'Mutton, Spices, Yogurt'},
        {'id': 9, 'name': 'Fish Fry', 'price': 350, 'ingredients': 'Fish, Spices, Oil'},
        {'id': 10, 'name': 'Chicken Biryani', 'price': 280, 'ingredients': 'Chicken, Rice, Spices'},
        {'id': 11, 'name': 'Butter Chicken', 'price': 320, 'ingredients': 'Chicken, Butter, Cream, Spices'},
        {'id': 12, 'name': 'Tandoori Chicken', 'price': 340, 'ingredients': 'Chicken, Yogurt, Spices'},
    ],
    # Add other menu items here
}

# Order Management
orders = []

def create_order(item_name, price):
    order = {
        'item_name': item_name,
        'price': price,
        'timestamp': datetime.datetime.now()
    }
    orders.append(order)
    print(f"{item_name} added to the order!")

def view_orders():
    print("\n--- Current Orders ---")
    if orders:
        for idx, order in enumerate(orders, start=1):
            print(f"{idx}. Item: {order['item_name']}, Price: ₹{order['price']}, Time: {order['timestamp']}")
    else:
        print("No orders yet!")

# Function to Display Menu
def display_menu(category):
    print(f"\n--- {category.capitalize()} Menu ---")
    for item in menu_items[category]:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ₹{item['price']}, Ingredients: {item['ingredients']}")
    print("\n")

# Main Staff Menu
def staff_menu():
    while True:
        print("\n--- Staff Menu ---")
        print("1. Dashboard")
        print("2. Order Management")
        print("3. Table Management")
        print("4. Inventory Access")
        print("5. Customer Service")
        print("6. Shift Management")
        print("7. Generate Bill")
        print("8. Logout")
        
        choice = input("Please choose an option (1-8): ")

        if choice == '1':
            print("Dashboard: All system activities will be monitored here.")
        elif choice == '2':
            order_management()
        elif choice == '3':
            print("Table Management: Functionality for managing tables.")
        elif choice == '4':
            print("Inventory Access: Functionality for inventory management.")
        elif choice == '5':
            print("Customer Service: Handling customer inquiries.")
        elif choice == '6':
            print("Shift Management: Managing staff shifts.")
        elif choice == '7':
            print("Generate Bill: Functionality for generating bills.")
        elif choice == '8':
            print("Logging out... Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

# Order Management
def order_management():
    while True:
        print("\n--- Order Management ---")
        print("1. View Veg Menu")
        print("2. View Non-Veg Menu")
        print("3. View Soft Drinks Menu")
        print("4. View Salad Menu")
        print("5. View Indian Bread Menu")
        print("6. View Rice Menu")
        print("7. Create Order")
        print("8. View Current Orders")
        print("9. Back to Staff Menu")
        
        choice = input("Please choose an option (1-9): ")

        if choice == '1':
            display_menu('veg')
        elif choice == '2':
            display_menu('non_veg')
        elif choice == '3':
            display_menu('soft_drinks')
        elif choice == '4':
            display_menu('salad')
        elif choice == '5':
            display_menu('indian_bread')
        elif choice == '6':
            display_menu('rice')
        elif choice == '7':
            try:
                item_id = int(input("Enter the item ID to add to order: "))
                category_found = None
                item_found = None

                # Search for the item in all categories
                for category in menu_items:
                    for item in menu_items[category]:
                        if item['id'] == item_id:
                            category_found = category
                            item_found = item
                            break
                    if item_found:
                        break

                if item_found:
                    create_order(item_found['name'], item_found['price'])
                else:
                    print("Invalid item ID. Please try again.")
            except ValueError:
                print("Please enter a valid numerical ID.")

        elif choice == '8':
            view_orders()

        elif choice == '9':
            break

        else:
            print("Invalid option, please try again.")

# Start the Staff Menu
staff_menu()
