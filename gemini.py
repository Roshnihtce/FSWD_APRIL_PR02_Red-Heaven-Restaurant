import datetime

class RestaurantManagementSystem:
    def __init__(self):
        self.veg_items = ["Paneer Tikka", "Aloo Gobi", "Veg Biryani", "Chole Bhature", "Veg Burger", "Paneer Butter Masala",
                          "Mixed Veg Curry", "Palak Paneer", "Dal Makhani", "Veg Pulao"]
        self.non_veg_items = ["Chicken Biryani", "Butter Chicken", "Mutton Korma", "Fish Curry", "Prawn Fry",  
                              "Chicken Tikka", "Egg Curry", "Lamb Chops", "Chicken Wings", "Beef Steak"]
        self.orders = []
        self.tables = {2: "Assigned", 5: "Assigned", 7: "Available"}
        self.inventory = {"Tomatoes": 10, "Cheese": 5, "Chicken": 7, "Paneer": 8}
        self.shift_schedule = [{"day": "Monday", "shift": "9AM - 2PM"}, {"day": "Tuesday", "shift": "2PM - 7PM"}]
        self.customer_feedback = []

    def main_dashboard(self):
        while True:
            print("\n==== Main Dashboard ====")
            print("1. Staff Menu")
            print("2. Customer Menu")
            print("3. Exit")
            choice = input("Please select an option: ")
            if choice == "1":
                self.staff_menu()
            elif choice == "2":
                self.customer_menu()
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

    def staff_menu(self):
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
                self.staff_dashboard()
            elif choice == "2":
                self.order_management()
            elif choice == "3":
                self.table_management()
            elif choice == "4":
                self.inventory_access()
            elif choice == "5":
                self.customer_service()
            elif choice == "6":
                self.shift_management()
            elif choice == "7":
                self.generate_bill()
            elif choice == "8":
                print("Logging out...")
                break
            else:
                print("Invalid option. Please try again.")

    def customer_menu(self):
        while True:
            print("\n--- Customer Menu ---")
            print("1. View Menu")
            print("2. Place Order")
            print("3. Provide Feedback")
            print("4. Back")
            choice = input("Please choose an option (1-4): ")
            if choice == "1":
                self.view_menu()
            elif choice == "2":
                self.place_order()
            elif choice == "3":
                self.record_customer_feedback()
            elif choice == "4":
                break
            else:
                print("Invalid option. Please try again.")

    def staff_dashboard(self):
        print("\n==== Staff Dashboard ====")
        print("Daily Tasks: You have", len([table for table in self.tables if self.tables[table] == "Assigned"]), "assigned tables to manage.")
        print("Order Notifications: You have", len([order for order in self.orders if order['status'] == "Pending"]), "pending orders.")

    def order_management(self):
        while True:
            print("\n==== Order Management ====")
            print("1. View New Orders")
            print("2. Update Order Status")
            print("3. View Order History")
            print("4. Back")
            choice = input("Please select an option: ")
            if choice == "1":
                self.view_new_orders()
            elif choice == "2":
                self.update_order_status()
            elif choice == "3":
                self.view_order_history()
            elif choice == "4":
                break
            else:
                print("Invalid option. Please try again.")

    def view_new_orders(self):
        print("\nNew Orders:")
        for order in self.orders:
            print(f"Table {order['table']} - Items: {', '.join(order['items'])} - Status: {order['status']}")

    def update_order_status(self):
        table_no = int(input("Enter table number to update status: "))
        for order in self.orders:
            if order["table"] == table_no:
                order["status"] = "Served"
                order["served_time"] = datetime.datetime.now()
                print(f"Order for Table {table_no} marked as served.")
                return
        print(f"No pending order found for Table {table_no}.")

    def view_order_history(self):
        print("\nOrder History:")
        for order in self.orders:
            if order["status"] == "Served":
                print(f"Table {order['table']} - Items: {', '.join(order['items'])} - Served at: {order['served_time']}")

    def place_order(self):
        table_no = int(input("Enter table number for new order: "))
        print("\n--- Menu ---")
        print("Veg Items:")
        for i, item in enumerate(self.veg_items, 1):
            print(f"{i}. {item}")

        print("\nNon-Veg Items:")
        for i, item in enumerate(self.non_veg_items, 1):
            print(f"{i+10}. {item}")

        items = []
        while True:
            item_choice = input("Select item by number (0 to finish): ")
            if item_choice == "0":
                break
            item_choice = int(item_choice)
            if 1 <= item_choice <= 10:
                items.append(self.veg_items[item_choice - 1])
            elif 11 <= item_choice <= 20:
                items.append(self.non_veg_items[item_choice - 11])
            else:
                print("Invalid item number, try again.")

        if items:
            self.orders.append({"table": table_no, "items": items, "status": "Pending"})
            print(f"Order placed for Table {table_no} with items: {', '.join(items)}.")
        else:
            print("No items selected.")

    def table_management(self):
        while True:
            print("\n==== Table Management ====")
            print("1. Check Assigned Tables")
            print("2. Update Table Status")
            print("3. Back")
            choice = input("Please select an option: ")
            if choice == "1":
                self.check_assigned_tables()
            elif choice == "2":
                self.update_table_status()
            elif choice == "3":
                break
            else:
                print("Invalid option. Please try again.")

    def check_assigned_tables(self):
        print("\nAssigned Tables:")
        for table, status in self.tables.items():
            print(f"Table {table}: {status}")

    def update_table_status(self):
        table_no = int(input("Enter table number to update status: "))
        if table_no in self.tables:
            self.tables[table_no] = "Cleaned"
            print(f"Table {table_no} status updated to Cleaned.")
        else:
            print(f"Table {table_no} does not exist.")

    def inventory_access(self):
        while True:
            print("\n==== Inventory Access ====")
            print("1. View Inventory Levels")
            print("2. Report Low Stock Items")
            print("3. Back")
            choice = input("Please select an option: ")
            if choice == "1":
                self.view_inventory_levels()
            elif choice == "2":
                self.report_low_stock()
            elif choice == "3":
                break
            else:
                print("Invalid option. Please try again.")

    def view_inventory_levels(self):
        print("\n==== Inventory Levels ====")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity} units")

    def report_low_stock(self):
        low_stock_item = input("Enter the item name to report low stock: ")
        if low_stock_item in self.inventory:
            print(f"Low stock reported for {low_stock_item}.")
        else:
            print(f"{low_stock_item} is not found in the inventory.")

    def customer_service(self):
        while True:
            print("\n==== Customer Service ====")
            print("1. Access Customer Profiles")
            print("2. Record Customer Feedback")
            print("3. Back")
            choice = input("Please select an option: ")
            if choice == "1":
                self.access_customer_profiles()
            elif choice == "2":
                self.record_customer_feedback()
            elif choice == "3":
                break
            else:
                print("Invalid option. Please try again.")

    def access_customer_profiles(self):
        print("Customer Profiles: John Doe - Regular, Table 5.")

    def record_customer_feedback(self):
        feedback = input("Enter customer feedback: ")
        self.customer_feedback.append(feedback)
        print("Feedback recorded.")

    def shift_management(self):
        while True:
            print("\n==== Shift Management ====")
            print("1. View Shift Schedule")
            print("2. Request Shift Changes")
            print("3. Back")
            choice = input("Please select an option: ")
            if choice == "1":
                self.view_shift_schedule()
            elif choice == "2":
                self.request_shift_changes()
            elif choice == "3":
                break
            else:
                print("Invalid option. Please try again.")

    def view_shift_schedule(self):
        print("\nShift Schedule:")
        for schedule in self.shift_schedule:
            print(f"{schedule['day']} - {schedule['shift']}")

    def request_shift_changes(self):
        day = input("Enter day for shift change request: ")
        new_shift = input("Enter new shift timings: ")
        for schedule in self.shift_schedule:
            if schedule["day"] == day:
                schedule["shift"] = new_shift
                print(f"Shift for {day} updated to {new_shift}.")
                return
        print(f"No shift found for {day}.")

    def generate_bill(self):
        table_no = int(input("Enter table number to generate bill: "))
        for order in self.orders:
            if order["table"] == table_no and order["status"] == "Served":
                total = len(order["items"]) * 100  # Assume each item costs 100
                print(f"Bill for Table {table_no}: {total} (for {len(order['items'])} items)")
                return
        print(f"No served order found for Table {table_no}.")

# Example of how to start the system
rms = RestaurantManagementSystem()
rms.main_dashboard()
