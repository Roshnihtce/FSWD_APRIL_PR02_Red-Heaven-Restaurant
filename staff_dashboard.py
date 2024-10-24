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
    'soft_drinks': [
        {'id': 13, 'name': 'Coke', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Caffeine'},
        {'id': 14, 'name': 'Sprite', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Citric Acid'},
        {'id': 15, 'name': 'Pepsi', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Caffeine'},
        {'id': 16, 'name': 'Fanta', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Orange Flavor'},
        {'id': 17, 'name': 'Limca', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Lime Flavor'},
        {'id': 18, 'name': '7Up', 'price': 50, 'ingredients': 'Carbonated Water, Sugar, Citric Acid'},
    ],
    'salad': [
        {'id': 19, 'name': 'Greek Salad', 'price': 120, 'ingredients': 'Tomatoes, Cucumber, Olives, Feta Cheese'},
        {'id': 20, 'name': 'Caesar Salad', 'price': 130, 'ingredients': 'Lettuce, Croutons, Parmesan, Caesar Dressing'},
        {'id': 21, 'name': 'Garden Salad', 'price': 100, 'ingredients': 'Lettuce, Carrots, Cucumbers, Dressing'},
        {'id': 22, 'name': 'Cucumber Salad', 'price': 80, 'ingredients': 'Cucumbers, Vinegar, Herbs'},
        {'id': 23, 'name': 'Tomato Salad', 'price': 70, 'ingredients': 'Tomatoes, Onion, Dressing'},
        {'id': 24, 'name': 'Fruit Salad', 'price': 150, 'ingredients': 'Mixed Fruits, Honey, Mint'},
    ],
    'indian_bread': [
        {'id': 25, 'name': 'Naan', 'price': 40, 'ingredients': 'Flour, Yeast, Water, Yogurt'},
        {'id': 26, 'name': 'Roti', 'price': 20, 'ingredients': 'Whole Wheat Flour, Water'},
        {'id': 27, 'name': 'Paratha', 'price': 50, 'ingredients': 'Flour, Ghee, Water'},
        {'id': 28, 'name': 'Butter Naan', 'price': 50, 'ingredients': 'Flour, Butter, Yeast'},
        {'id': 29, 'name': 'Garlic Naan', 'price': 60, 'ingredients': 'Flour, Garlic, Butter'},
        {'id': 30, 'name': 'Tandoori Roti', 'price': 30, 'ingredients': 'Whole Wheat Flour, Water'},
    ],
    'rice': [
        {'id': 31, 'name': 'Steamed Rice', 'price': 100, 'ingredients': 'Rice, Water'},
        {'id': 32, 'name': 'Jeera Rice', 'price': 120, 'ingredients': 'Rice, Cumin, Spices'},
        {'id': 33, 'name': 'Fried Rice', 'price': 150, 'ingredients': 'Rice, Vegetables, Spices'},
        {'id': 34, 'name': 'Veg Pulao', 'price': 180, 'ingredients': 'Rice, Mixed Vegetables, Spices'},
        {'id': 35, 'name': 'Chicken Pulao', 'price': 220, 'ingredients': 'Rice, Chicken, Spices'},
        {'id': 36, 'name': 'Paneer Pulao', 'price': 190, 'ingredients': 'Rice, Paneer, Spices'},
    ]
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
            # Dashboard code could go here
        elif choice == '2':
            order_management()
        elif choice == '3':
            print("Table Management: Functionality for managing tables.")
            # Table Management code could go here
        elif choice == '4':
            print("Inventory Access: Functionality for inventory management.")
            # Inventory Access code could go here
        elif choice == '5':
            print("Customer Service: Handling customer inquiries.")
            # Customer Service code could go here
        elif choice == '6':
            print("Shift Management: Managing staff shifts.")
            # Shift Management code could go here
        elif choice == '7':
            print("Generate Bill: Functionality for generating bills.")
            # Bill Generation code could go here
        elif choice == '8':
            print("Logging out... Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

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

        elif choice == '8':
            view_orders()

        elif choice == '9':
            break

        else:
            print("Invalid option, please try again.")

# Start the Staff Menu
staff_menu()