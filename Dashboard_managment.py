def main_dashboard():
    while True:
        print("==== Main Dashboard ====")
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
    while True:
        print("\n==== Staff Dashboard ====")
        print("1. View Daily Tasks")
        print("2. View Notifications")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            print("Daily Tasks: You have 3 tables to manage today and 2 new orders.")
        elif choice == "2":
            print("Notifications: Shift change request approved.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

def order_management():
    while True:
        print("\n==== Order Management ====")
        print("1. View New Orders")
        print("2. Update Order Status")
        print("3. View Order History")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            print("New Orders: Table 2 - Burger, Table 5 - Pizza.")
        elif choice == "2":
            print("Order Status: Order for Table 2 marked as served.")
        elif choice == "3":
            print("Order History: Last 5 orders served successfully.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

def table_management():
    while True:
        print("\n==== Table Management ====")
        print("1. Check Assigned Tables")
        print("2. Update Table Status")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            print("Assigned Tables: Table 2, Table 5, Table 7.")
        elif choice == "2":
            print("Table Status: Table 2 marked as cleaned.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

def inventory_access():
    while True:
        print("\n==== Inventory Access ====")
        print("1. View Inventory Levels")
        print("2. Report Low Stock Items")
        print("0. Back")
        choice = input("Please select an option: ")
        if choice == "1":
            print("Inventory Levels: Tomatoes - 10kg, Cheese - 5kg.")
        elif choice == "2":
            print("Low Stock: Reported low stock for tomatoes.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

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
            print("Customer Feedback: Recorded feedback - 'Great service!'")
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
            print("Shift Schedule: Morning - 9AM to 2PM.")
        elif choice == "2":
            print("Shift Change Request: Submitted request for shift swap.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")

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

if __name__ == "__main__":
    main_dashboard()
