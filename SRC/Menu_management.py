import json
import os

class MenuDashboard:
    def __init__(self):
        # Path to the menu.json file in the 'data/' folder
        self.menu_file = os.path.join('data', 'menu.json')
        self.menu = self.load_menu()

    def load_menu(self):
        """Load menu from the JSON file."""
        try:
            with open(self.menu_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"{self.menu_file} not found. Starting with an empty menu.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding {self.menu_file}. Starting with an empty menu.")
            return {}

    def save_menu(self):
        """Save the menu to the JSON file."""
        with open(self.menu_file, 'w') as file:
            json.dump(self.menu, file, indent=4)
        print("Menu saved successfully.")

    def menu_management(self):
        while True:
            print("\n==== Menu Management ====")
            print("1. Add Menu Item")
            print("2. Edit Menu Item")
            print("3. Delete Menu Item")
            print("4. View Special Offers")
            print("5. View Menu Items")
            print("6. Back")
            
            choice = input("Please select an option: ")

            if choice == '1':
                self.add_menu_item()
            elif choice == '2':
                self.edit_menu_item()
            elif choice == '3':
                self.delete_menu_item()
            elif choice == '4':
                self.view_special_offers()
            elif choice == '5':
                self.view_menu()
            elif choice == '6':
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def add_menu_item(self):
        """Add a new item to the menu."""
        category = input("Enter the category (veg, non_veg, soft_drinks, etc.): ").lower()
        if category not in self.menu:
            print(f"Category '{category}' not found. Please select a valid category.")
            return
        
        name = input("Enter menu item name: ")
        price = float(input("Enter menu item price: "))
        ingredients = input("Enter menu item ingredients: ")
        
        new_id = max(item['id'] for item in self.menu[category]) + 1 if self.menu[category] else 1
        
        menu_item = {
            "id": new_id,
            "name": name,
            "price": price,
            "ingredients": ingredients
        }
        
        self.menu[category].append(menu_item)
        self.save_menu()
        print(f"Menu item '{name}' added successfully to category '{category}'.")
    
    def edit_menu_item(self):
        """Edit an existing menu item."""
        self.view_menu()
        category = input("Enter the category (veg, non_veg, soft_drinks, etc.): ").lower()
        if category not in self.menu:
            print(f"Category '{category}' not found.")
            return
        
        item_id = int(input("Enter the ID of the menu item to edit: "))
        
        for item in self.menu[category]:
            if item['id'] == item_id:
                print(f"Editing '{item['name']}' (ID: {item_id})...")
                item['price'] = float(input(f"Enter new price for {item['name']} (current: {item['price']}): "))
                item['ingredients'] = input(f"Enter new ingredients for {item['name']} (current: {item['ingredients']}): ")
                self.save_menu()
                print(f"Menu item '{item['name']}' updated successfully.")
                return
        print(f"Menu item with ID '{item_id}' not found in category '{category}'.")
    
    def delete_menu_item(self):
        """Delete a menu item."""
        self.view_menu()
        category = input("Enter the category (veg, non_veg, soft_drinks, etc.): ").lower()
        if category not in self.menu:
            print(f"Category '{category}' not found.")
            return
        
        item_id = int(input("Enter the ID of the menu item to delete: "))
        
        for item in self.menu[category]:
            if item['id'] == item_id:
                self.menu[category].remove(item)
                self.save_menu()
                print(f"Menu item '{item['name']}' (ID: {item_id}) deleted successfully.")
                return
        print(f"Menu item with ID '{item_id}' not found in category '{category}'.")
    
    def view_special_offers(self):
        """Display special offers."""
        print("\n==== Special Offers ====")
        special_offers = [
            {"name": "Buy 1 Get 1 Free Pizza", "valid_till": "31st Oct 2024"},
            {"name": "20% off on Desserts", "valid_till": "25th Dec 2024"}
        ]
        
        if special_offers:
            for offer in special_offers:
                print(f"Offer: {offer['name']}, Valid Till: {offer['valid_till']}")
        else:
            print("No special offers available at the moment.")
    
    def view_menu(self):
        """View the current menu items categorized by type."""
        if not self.menu:
            print("No items in the menu.")
        else:
            print("\n==== Current Menu ====")
            for category, items in self.menu.items():
                print(f"\n-- {category.replace('_', ' ').title()} --")
                print(f"{'ID':<5} {'Name':<25} {'Price':<10} {'Ingredients':<30}")
                print("="*70)
                for item in items:
                    item_id = item.get('id', 'N/A')
                    name = item.get('name', 'N/A')
                    price = item.get('price', 'N/A')
                    ingredients = item.get('ingredients', 'N/A')
                    print(f"{item_id:<5} {name:<25} {price:<10} {ingredients:<30}")
                print("-" * 70)

if __name__ == "__main__":
    dashboard = MenuDashboard()
    dashboard.menu_management()
