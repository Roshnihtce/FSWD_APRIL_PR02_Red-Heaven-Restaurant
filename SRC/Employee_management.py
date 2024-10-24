import json
import os
import uuid

class EmployeeManagement:
    def __init__(self, json_file='data/staff_data.json'):
        self.json_file = json_file
        self.staff_list = self.load_data()

    def load_data(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as file:
                return json.load(file)
        return []

    def save_data(self):
        with open(self.json_file, 'w') as file:
            json.dump(self.staff_list, file, indent=4)
    
    def employee_management(self):
        while True:
            print("\n==== Employee Management ====")
            print("1. Add Staff")
            print("2. Edit Staff")
            print("3. Delete Staff")
            print("4. View Staff Schedules")
            print("5. Back")

            choice = input("Please select an option: ")

            if choice == '1':
                self.add_staff()
            elif choice == '2':
                self.edit_staff()
            elif choice == '3':
                self.delete_staff()
            elif choice == '4':
                self.view_staff_schedules()
            elif choice == '5':
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_staff(self):
        first_name = input("Enter staff's first name: ")
        second_name = input("Enter staff's second name: ")
        mobile_number = input("Enter staff's mobile number: ")
        role = input("Enter staff role: ")
        schedule = input("Enter staff schedule: ")
        timing = input("Enter staff timing: ")

        
        username = input("Enter a username for the staff: ")
        
        staff_id = str(uuid.uuid4())[:8]

        password = input("Enter a password for the staff: ")

        staff_member = {
            "id": staff_id,
            "first_name": first_name,
            "second_name": second_name,
            "mobile_number": mobile_number,
            "role": role,
            "schedule": schedule,
            "timing": timing,
            "username": username,
            "password": password
        }

        self.staff_list.append(staff_member)
        self.save_data()
        print(f"Staff {first_name} {second_name} added successfully with ID {staff_id} and username '{username}'.")

    def edit_staff(self):
        self.view_staff()
        staff_id = input("Enter the ID of the staff member to edit: ")

        for staff in self.staff_list:
            if staff['id'] == staff_id:
                print(f"Editing {staff['first_name']} {staff['second_name']}...")
                staff['role'] = input(f"Enter new role (current: {staff['role']}): ") or staff['role']
                staff['schedule'] = input(f"Enter new schedule (current: {staff['schedule']}): ") or staff['schedule']
                staff['timing'] = input(f"Enter new timing (current: {staff['timing']}): ") or staff['timing']
                staff['username'] = input(f"Enter new username (current: {staff['username']}): ") or staff['username']
                self.save_data()
                print(f"Staff {staff['first_name']} {staff['second_name']} updated successfully.")
                return
        print(f"Staff member with ID {staff_id} not found.")

    def delete_staff(self):
        self.view_staff()
        staff_id = input("Enter the ID of the staff member to delete: ")

        for staff in self.staff_list:
            if staff['id'] == staff_id:
                self.staff_list.remove(staff)
                self.save_data()
                print(f"Staff with ID {staff_id} deleted successfully.")
                return
        print(f"Staff member with ID {staff_id} not found.")

    def view_staff_schedules(self):
        if not self.staff_list:
            print("No staff members available.")
        else:
            print("\n==== Staff Schedules ====")
            for staff in self.staff_list:
                print(f"{staff['first_name']} {staff['second_name']} ({staff['role']}): {staff['schedule']} | Timing: {staff['timing']}")

    def view_staff(self):
        if not self.staff_list:
            print("No staff members available.")
        else:
            print("\n==== Staff List ====")
            for staff in self.staff_list:
                print(f"ID: {staff['id']} - {staff['first_name']} {staff['second_name']} - {staff['role']} - Username: {staff['username']}")

if __name__ == "__main__":
    dashboard = EmployeeManagement()
    dashboard.employee_management()
