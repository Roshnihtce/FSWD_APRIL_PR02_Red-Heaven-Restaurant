# List of daily tasks for the staff
daily_tasks = [
    "Prepare ingredients for lunch menu.",
    "Check table reservations for the day.",
    "Clean the dining area before opening.",
    "Inspect kitchen equipment for maintenance.",
    "Stock up on beverages and snacks.",
    "Review and update the staff shift schedule.",
    "Ensure the restaurant complies with safety standards."
]

# List of notifications for staff to stay updated
notifications = [
    "New customer feedback received.",
    "Inventory levels updated by the kitchen staff.",
    "Maintenance scheduled for the kitchen on Friday.",
    "New menu item added to the dinner selection.",
    "Special discount for today's happy hour."
]

# Function to display the dashboard menu with daily tasks and notifications
def dashboard():
    while True:
        print("\n--- Dashboard ---")
        print("1. View Daily Tasks")
        print("2. View Notifications")
        print("3. Back to Main Menu")

        # Get user's choice from the menu
        choice = input("Choose an option: ")

        # If the user chooses to view daily tasks
        if choice == '1':
            print("\n--- Daily Tasks ---")
            for idx, task in enumerate(daily_tasks, start=1):
                print(f"{idx}. {task}")
        
        # If the user chooses to view notifications
        elif choice == '2':
            print("\n--- Notifications ---")
            for idx, notification in enumerate(notifications, start=1):
                print(f"{idx}. {notification}")
        
        # If the user chooses to go back to the main menu
        elif choice == '3':
            break
        
        # If the user enters an invalid option
        else:
            print("Invalid option, please try again.")

# Add a main block to ensure it runs when executed directly
if __name__ == "__main__":
    dashboard()
