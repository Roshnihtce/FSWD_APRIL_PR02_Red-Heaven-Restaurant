class CustomerDashboard:
    def __init__(self):
        self.main_menu()

    def main_menu(self):
        while True:
            print("\n--- Customer Dashboard ---")
            print("1. Home")
            print("2. Menu")
            print("3. Order")
            print("4. Reservations")
            print("5. Account Management")
            print("6. Feedback")
            print("7. Generate Bill")
            print("8. Logout")
            choice = input("Select an option: ")

            if choice == '1':
                self.home_menu()
            elif choice == '2':
                self.menu_menu()
            elif choice == '3':
                self.order_menu()
            elif choice == '4':
                self.reservations_menu()
            elif choice == '5':
                self.account_management_menu()
            elif choice == '6':
                self.feedback_menu()
            elif choice == '7':
                self.generate_bill_menu()
            elif choice == '8':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def home_menu(self):
        while True:
            print("\n--- Home ---")
            print("1. View Restaurant Overview")
            print("2. View Promotions")
            print("3. Back")
            choice = input("Select an option: ")

            if choice == '1':
                print("Showing restaurant overview...")
            elif choice == '2':
                print("Displaying promotions...")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def menu_menu(self):
        while True:
            print("\n--- Menu ---")
            print("1. Browse Menu Items")
            print("2. Search Menu Items")
            print("3. Filter Options (Vegan, Gluten-Free, etc.)")
            print("4. Back")
            choice = input("Select an option: ")

            if choice == '1':
                print("Browsing menu items...")
            elif choice == '2':
                print("Search functionality for menu items...")
            elif choice == '3':
                print("Filter options: Vegan, Gluten-Free, etc.")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def order_menu(self):
        while True:
            print("\n--- Order ---")
            print("1. Place Order (Dine-In, Takeaway, Delivery)")
            print("2. Customize Order")
            print("3. Choose Payment Method")
            print("4. Back")
            choice = input("Select an option: ")

            if choice == '1':
                print("Placing order...")
            elif choice == '2':
                print("Customizing order...")
            elif choice == '3':
                print("Choosing payment method...")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def reservations_menu(self):
        while True:
            print("\n--- Reservations ---")
            print("1. Make Reservation")
            print("2. View Reservations")
            print("3. Edit Reservations")
            print("4. Cancel Reservations")
            print("5. Back")
            choice = input("Select an option: ")

            if choice == '1':
                print("Making reservation...")
            elif choice == '2':
                print("Viewing reservations...")
            elif choice == '3':
                print("Editing reservation...")
            elif choice == '4':
                print("Canceling reservation...")
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def account_management_menu(self):
        while True:
            print("\n--- Account Management ---")
            print("1. Create/View Profile")
            print("2. View Order History")
            print("3. Manage Preferences (Allergies, Favorite Dishes)")
            print("4. Back")
            choice = input("Select an option: ")

            if choice == '1':
                print("Creating or viewing profile...")
            elif choice == '2':
                print("Viewing order history...")
            elif choice == '3':
                print("Managing preferences...")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def feedback_menu(self):
        while True:
            print("\n--- Feedback ---")
            print("1. Rate Experience")
            print("2. Leave Comments")
            print("3. Back")
            choice = input("Select an option: ")

            if choice == '1':
                print("Rating experience...")
            elif choice == '2':
                print("Leaving comments...")
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def generate_bill_menu(self):
        while True:
            print("\n--- Generate Bill ---")
            print("1. View Bill for Current Order")
            print("2. Request Detailed Bill")
            print("3. Pay Bill")
            print("4. Back")
            choice = input("Select an option: ")

            if choice == '1':
                print("Viewing bill for current order...")
            elif choice == '2':
                print("Requesting detailed bill...")
            elif choice == '3':
                print("Paying bill...")
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    CustomerDashboard()
