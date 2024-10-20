# Sample data for dynamic interaction
veg_items = ["Paneer Tikka", "Aloo Gobi", "Veg Biryani", "Chole Bhature", "Veg Burger", "Paneer Butter Masala", 
             "Mixed Veg Curry", "Palak Paneer", "Dal Makhani", "Veg Pulao"]

non_veg_items = ["Chicken Biryani", "Butter Chicken", "Mutton Korma", "Fish Curry", "Prawn Fry", 
                 "Chicken Tikka", "Egg Curry", "Lamb Chops", "Chicken Wings", "Beef Steak"]

orders = [
    {"table": 2, "items": [veg_items[0], non_veg_items[1]], "status": "Pending"}, # Paneer Tikka, Butter Chicken
    {"table": 5, "items": [non_veg_items[4], veg_items[7]], "status": "Pending"} # Prawn Fry, Palak Paneer
]

tables = {
    2: "Assigned",
    5: "Assigned",
    7: "Available"
}

inventory = {
    "Tomatoes": 10,
    "Cheese": 5,
    "Chicken": 7,
    "Paneer": 8
}

shift_schedule = [
    {"day": "Monday", "shift": "9AM - 2PM"},
    {"day": "Tuesday", "shift": "2PM - 7PM"}
]

customer_feedback = []


def main_dashboard():
    while True:
        print("\n==== Main Dashboard ====")
        print("1. Staff Menu")
        print("2. Exit")
        choice = input("Please select an option: ")
        if choice == "1":
            staff_menu()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


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
        if choice == "1":
            staff_dashboard()
        elif choice == "2":
            order_management()
        elif choice == "3":
            table_management()
        elif choice == "4":
            inventory_access()
        elif choice == "5":
            customer_service()
        elif choice == "6":
            shift_management()
        elif choice == "7":
            generate_bill()
        elif choice == "8":
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")


def staff_dashboard():
    print("\n==== Staff Dashboard ====")
    print("Daily Tasks: You have", len([table for table in tables if tables[table] == "Assigned"]), "assigned tables to manage.")
    print("Order Notifications: You have", len([order for order in orders if order['status'] == "Pending"]), "pending orders.")


def order_management():
    while True:
        print("\n==== Order Management ====")
        print("1. View New Orders")
        print("2. Update Order Status")
        print("3. View Order History")
        print("4. Place New Order")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            view_new_orders()
        elif choice == "2":
            update_order_status()
        elif choice == "3":
            print("Order History: Last 5 orders served successfully.")
        elif choice == "4":
            place_new_order()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def view_new_orders():
    print("\nNew Orders:")
    for order in orders:
        print(f"Table {order['table']} - Items: {', '.join(order['items'])} - Status: {order['status']}")


def update_order_status():
    table_no = int(input("Enter table number to update status: "))
    for order in orders:
        if order["table"] == table_no:
            order["status"] = "Served"
            print(f"Order for Table {table_no} marked as served.")
            return
    print(f"No pending order found for Table {table_no}.")


def place_new_order():
    table_no = int(input("Enter table number for new order: "))
    print("\n--- Menu ---")
    print("Veg Items:")
    for i, item in enumerate(veg_items, 1):
        print(f"{i}. {item}")
    
    print("\nNon-Veg Items:")
    for i, item in enumerate(non_veg_items, 1):
        print(f"{i+10}. {item}")
    
    items = []
    while True:
        item_choice = input("Select item by number (0 to finish): ")
        if item_choice == "0":
            break
        item_choice = int(item_choice)
        if 1 <= item_choice <= 10:
            items.append(veg_items[item_choice - 1])
        elif 11 <= item_choice <= 20:
            items.append(non_veg_items[item_choice - 11])
        else:
            print("Invalid item number, try again.")
    
    if items:
        orders.append({"table": table_no, "items": items, "status": "Pending"})
        print(f"Order placed for Table {table_no} with items: {', '.join(items)}.")
    else:
        print("No items selected.")


def table_management():
    while True:
        print("\n==== Table Management ====")
        print("1. Check Assigned Tables")
        print("2. Update Table Status")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            check_assigned_tables()
        elif choice == "2":
            update_table_status()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def check_assigned_tables():
    print("\nAssigned Tables:")
    for table, status in tables.items():
        print(f"Table {table}: {status}")


def update_table_status():
    table_no = int(input("Enter table number to update status: "))
    if table_no in tables:
        tables[table_no] = "Cleaned"
        print(f"Table {table_no} status updated to Cleaned.")
    else:
        print(f"Table {table_no} does not exist.")


def inventory_access():
    while True:
        print("\n==== Inventory Access ====")
        print("1. View Inventory Levels")
        print("2. Report Low Stock Items")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            view_inventory_levels()
        elif choice == "2":
            report_low_stock()
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def view_inventory_levels():
    print("\nInventory Levels:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}kg")


def report_low_stock():
    item = input("Enter item name to report low stock: ")
    if item in inventory:
        print(f"Low stock reported for {item}.")
    else:
        print(f"{item} not found in inventory.")


def customer_service():
    while True:
        print("\n==== Customer Service ====")
        print("1. Access Customer Profiles")
        print("2. Record Customer Feedback")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            print("Customer Profiles: John Doe - Regular, Table 5.")
        elif choice == "2":
            feedback = input("Enter customer feedback: ")
            customer_feedback.append(feedback)
            print("Customer feedback recorded.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def shift_management():
    while True:
        print("\n==== Shift Management ====")
        print("1. View Shift Schedule")
        print("2. Request Shift Changes")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            view_shift_schedule()
        elif choice == "2":
            print("Shift Change Request: Submitted request for shift swap.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def view_shift_schedule():
    print("\nShift Schedule:")
    for shift in shift_schedule:
        print(f"{shift['day']}: {shift['shift']}")


def generate_bill():
    while True:
        print("\n==== Generate Bill ====")
        print("1. Generate Bill for Current Orders")
        print("2. Print/Email Bill to Customer")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            print("Bill generated for Table 2 - $25.")
        elif choice == "2":
            print("Bill printed and emailed to customer.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


# Start the application
main_dashboard()
