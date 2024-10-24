import json

path = r'E:/Red-Heaven-Restaurant/FSWD_APRIL_PR02_Red-Heaven-Restaurant/data/manager_password.json'

def load_manager_credentials():
    try:
        with open(path, 'r') as file:
            credentials = json.load(file)
            return credentials
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        return None

def save_manager_credentials(credentials):
    with open(path, 'w') as file:
        json.dump(credentials, file, indent=4)


class ManagerDashboard:
    def __init__(self):
        self.main_dashboard()
    

    def main_dashboard(self):
        while True:
            print("\n==== Main Dashboard ====")
            print("1. Login")
            print("2. Exit")

            choice = input("Please select an option: ") 

            if choice == '1':
                self.login_dashboard()
            elif choice == '2':
                print("Exiting system... Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


    def login_dashboard(self):
        while True:
            print("\n==== Login Dashboard ====")
            print("1. Manager Login")
            print("2. Staff Login")
            print("3. Customer Login")
            print("4. Exit")
            print("0. Back to Main Dashboard")
            
            choice = input("Please select an option: ")
            
            if choice == '1':
                self.manager_login()
            elif choice == '2':
                print("Staff Login selected. Proceed with Staff Login logic...")
                # Add Staff login logic here
            elif choice == '3':
                print("Customer Login selected. Proceed with Customer Login logic...")
                # Add Customer login logic here
            elif choice == '0':
                print("Returning to Main Dashboard...")
                break  # Return to the main dashboard
            elif choice == '4':
                print("Exiting system... Goodbye!")
                exit()
            else:
                print("Invalid choice. Please try again.")


    def manager_login(self):
        credentials = load_manager_credentials()
        
        if credentials is None:
            return

        username = input("Enter Manager Username: ")
        password = input("Enter Manager Password: ")

        if username == credentials['username'] and password == credentials['password']:
            print("Login Manager successful!")
            self.manager_menu()
        else:
            print("Invalid username or password. Please try again.")


    def manager_menu(self):
        while True:
            print("\n==== Manager Menu ====")
            print("1. Dashboard")
            print("2. Employee Management")
            print("3. Inventory Management")
            print("4. Menu Management")
            print("5. Sales Reports")
            print("6. Reservations Management")
            print("7. Settings")
            print("8. Generate Bill")
            print("9. Logout")
            
            choice = input("Please select an option: ")
            
            if choice == '1':
                self.dashboard()
            elif choice == '2':
                self.employee_management()
            elif choice == '3':
                self.inventory_management()
            elif choice == '4':
                self.menu_management()
            elif choice == '5':
                self.sales_reports()
            elif choice == '6':
                self.reservations_management()
            elif choice == '7':
                self.settings_menu()
            elif choice == '8':
                self.generate_bill()
            elif choice == '9':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")


    def dashboard(self):
        while True:
            print("\n==== Dashboard ====")
            print("1. View Sales Overview")
            print("2. View Reservations Overview")
            print("3. View Staff Performance")
            print("4. Back")
            
            choice = input("Please select an option:")

            if choice == '1':
                print("View Sales Overview... (Logic to be implemented)")
            elif choice == '2':
                print("View Reservations Overview... (Logic to be implemented)")
            elif choice == '3':
                print("View Staff Performance... (Logic to be implemented)")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")


    def employee_management(self):
        while True:
            print("\n==== Employee Management ====")
            print("1. Add Staff")
            print("2. Edit Staff")
            print("3. Delete Staff")
            print("4. View Staff Schedules")
            print("5. Back")
            
            choice = input("Please select an option:")
            
            if choice == '1':
                print("Adding Staff... (Logic to be implemented)")
            elif choice == '2':
                print("Editing Staff... (Logic to be implemented)")
            elif choice == '3':
                print("Deleting Staff... (Logic to be implemented)")
            elif choice == '4':
                print("Viewing Staff Schedules... (Logic to be implemented)")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")


    def inventory_management(self):
        while True:
            print("\n==== Inventory Management ====")
            print("1. View Current Inventory ")
            print("2. Add Inventory Item")
            print("3. Edit Inventory Item")
            print("4. Delete Inventory Item")
            print("5. Low Stock Alerts")
            print("6. Back")
            
            choice = input("Please select an option:")

            if choice == '1':
                print("View Current Inventory... (Logic to be implemented)")
            elif choice == '2':
                print("Add Inventory Item... (Logic to be implemented)")
            elif choice == '3':
                print("Edit Inventory Item... (Logic to be implemented)")
            elif choice == '4':
                print("Delete Inventory Item... (Logic to be implemented)")
            elif choice == '5':
                print("Low Stock Alerts... (Login to implemented)")
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")


    def menu_management(self):
        while True:
            print("\n==== Menu Management ====")
            print("1. Add Menu Item ")
            print("2. Edit Menu Item")
            print("3. Delete Menu Item")
            print("4. View Special Offers")
            print("5. Back")
            
            choice = input("Please select an option:")

            if choice == '1':
                print("Add Menu Item... (Logic to be implemented)")
            elif choice == '2':
                print("Edit Menu Item... (Logic to be implemented)")
            elif choice == '3':
                print("Delete Menu Item... (Logic to be implemented)")
            elif choice == '4':
                print("View Special Offers... (Logic to be implemented)")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.") 


    def sales_reports(self):
        while True:
            print("\n==== Sales Reports ====")
            print("1. Daily Sales Reports")
            print("2. Weekly Sales Reports")
            print("3. Monthly Sales Reports")
            print("4. Back")
            
            choice = input("Please select an option:")

            if choice == '1':
                print("Daily Sales Reports... (Logic to be implemented)")
            elif choice == '2':
                print("Weekly Sales Reports... (Logic to be implemented)")
            elif choice == '3':
                print("Monthly Sales Reports... (Logic to be implemented)")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")    


    def reservations_management(self):
        while True:
            print("\n==== Reservations Management ====")
            print("1. View Reservations")
            print("2. Edit Reservations")
            print("3. Delete Reservations")
            print("4. Back")
            
            choice = input("Please select an option:")

            if choice == '1':
                print("View Reservations... (Logic to be implemented)")
            elif choice == '2':
                print("Edit Reservations... (Logic to be implemented)")
            elif choice == '3':
                print("Delete Reservations... (Logic to be implemented)")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")    


    def settings_menu(self):
        while True:
            print("\n==== Settings Menu ====")
            print("1. Update Business Information")
            print("2. Manage User Permissions")
            print("3. Back")
            
            choice = input("Please select an option:")

            if choice == '1':
                print("Update Business Information... (Logic to be implemented)")
            elif choice == '2':
                print("Manage User Permissions... (Logic to be implemented)")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")


    def generate_bill(self):
        while True:
            print("\n==== Generate Bill ====")
            print("1. View All Bills")
            print("2. Generate New Bill")
            print("3. Edit/Delete Existing Bills")
            print("4. Back")
            
            choice = input("Please select an option:")

            if choice == '1':
                print("View All Bills... (Logic to be implemented)")
            elif choice == '2':
                print("Generate New Bill... (Logic to be implemented)")
            elif choice == '3':
                print("Edit/Delete Existing Bills... (Logic to be implemented)")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")    


if __name__ == '__main__':
    ManagerDashboard()
