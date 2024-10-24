from datetime import datetime

class TableManagementSystem:
    def __init__(self):
        # Initialize tables (10 tables in total)
        self.tables = {i: {"status": "Available", "booking_details": None} for i in range(1, 11)}

    def show_tables(self):
        """Displays the current status of all tables."""
        print("\n--- Current Table Status ---")
        for table, info in self.tables.items():
            print(f"Table {table}: {info['status']}")

    def check_availability(self, date, time):
        """Checks and returns the available tables on a specific date and time."""
        available_tables = [t for t, info in self.tables.items() if info['status'] == "Available"]
        if available_tables:
            print(f"Tables available on {date} at {time}: {available_tables}")
            return available_tables
        else:
            print("Sorry, no tables available at that time.")
            return []

    def validate_date(self, date_str):
        """Validates the date format."""
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_time(self, time_str):
        """Validates the time format."""
        try:
            datetime.strptime(time_str, '%H:%M')
            return True
        except ValueError:
            return False

    def book_table(self):
        """Books a table for a user on a specific date and time."""
        name = input("Enter your name: ")
        date = input("Enter date for booking (YYYY-MM-DD): ")

        if not self.validate_date(date):
            print("Invalid date format. Please try again.")
            return

        time = input("Enter time for booking (HH:MM): ")
        if not self.validate_time(time):
            print("Invalid time format. Please try again.")
            return

        available_tables = self.check_availability(date, time)
        if available_tables:
            try:
                table_choice = int(input(f"Choose a table from available tables {available_tables}: "))
                if table_choice in available_tables:
                    self.tables[table_choice]['status'] = "Reserved"
                    self.tables[table_choice]['booking_details'] = {"name": name, "date": date, "time": time}
                    print(f"Table {table_choice} has been successfully booked for {name} on {date} at {time}.")
                else:
                    print("Invalid table choice.")
            except ValueError:
                print("Invalid input. Please enter a valid table number.")
        else:
            print("No tables available for booking.")

    def update_booking(self):
        """Updates an existing booking with a new date and time."""
        name = input("Enter the name for updating the booking: ")
        for table, info in self.tables.items():
            if info['booking_details'] and info['booking_details']['name'] == name:
                print(f"Booking found for {name} on table {table}.")
                new_date = input("Enter new date for booking (YYYY-MM-DD): ")
                if not self.validate_date(new_date):
                    print("Invalid date format. Please try again.")
                    return
                new_time = input("Enter new time for booking (HH:MM): ")
                if not self.validate_time(new_time):
                    print("Invalid time format. Please try again.")
                    return
                self.tables[table]['booking_details']['date'] = new_date
                self.tables[table]['booking_details']['time'] = new_time
                print(f"Booking updated for {name} on table {table} to {new_date} at {new_time}.")
                return
        print("No booking found under this name.")

    def cancel_booking(self):
        """Cancels an existing booking."""
        name = input("Enter the name to cancel booking: ")
        for table, info in self.tables.items():
            if info['booking_details'] and info['booking_details']['name'] == name:
                print(f"Booking found for {name} on table {table}.")
                self.tables[table]['status'] = "Available"
                self.tables[table]['booking_details'] = None
                print(f"Your booking for table {table} has been canceled.")
                return
        print("No booking found under this name.")

    def update_table_status(self):
        """Updates the status of a specific table manually."""
        try:
            table_number = int(input("Enter table number to update status: "))
            if table_number in self.tables:
                status = input("Enter new status (Available/Occupied/Reserved): ")
                if status in ["Available", "Occupied", "Reserved"]:
                    self.tables[table_number]['status'] = status
                    print(f"Table {table_number} status updated to {status}.")
                else:
                    print("Invalid status. Please enter Available, Occupied, or Reserved.")
            else:
                print("Invalid table number.")
        except ValueError:
            print("Invalid input. Please enter a valid table number.")

    def main_menu(self):
        """Displays the main menu and handles user input."""
        while True:
            print("\n--- Table Management System ---")
            print("1. Book a Table")
            print("2. Update Booking")
            print("3. Cancel Booking")
            print("4. Check Table Status")
            print("5. Update Table Status")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.book_table()
            elif choice == "2":
                self.update_booking()
            elif choice == "3":
                self.cancel_booking()
            elif choice == "4":
                self.show_tables()
            elif choice == "5":
                self.update_table_status()
            elif choice == "6":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")

# Run the table management system
if __name__ == "__main__":
    system = TableManagementSystem()
    system.main_menu()
