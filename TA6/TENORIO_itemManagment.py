#TENORIO CARL VINCENT IT0011 ITEM MANAGEMENT v1.00

class Item:
    
    def __init__(self, name, description, price, item_id):
        if not name:
            raise ValueError("Name cannot be empty.")
        if not description:
            raise ValueError("Description cannot be empty.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be positive number.")
        
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price
        
    def __str__(self):
        return f"\nID: {self.id} \nName: {self.name} \nDescription: {self.description} \nPrice: $ {self.price:.2f}"

class ItemManager:
    
    def __init__(self):
        self.items = {}
        self.existing_ids = []
        self.next_id = 1
        
    def generate_unique_id(self):
        unique_id = f"{self.next_id:03d}"
        self.next_id += 1
        return unique_id
                
    def add_item(self, name, description, price):
            try:
                item_id = self.generate_unique_id()
                item = Item(name, description, price, item_id)
                self.items[item.id] = item
                print(f"Item added succesfully with ID {item_id}.")
                return item            
            except ValueError as e:
                print(f"Error adding item: {e}")
                return None
            
    def get_item(self, item_id):
            return self.items.get(item_id)
        
    def update_item(self, item_id, name=None, description=None, price=None):
            item = self.get_item(item_id)
            if item:
                try:
                    if name:
                        item.name = name
                    if description: 
                        item.description = description
                    if price is not None:
                        if not isinstance(price, (int, float)) or price <= 0:
                            raise ValueError("Price must be a positive number.")                       
                    print(f"Item {item_id} updated successfully.")
                except ValueError as e:
                    print(f"Error updating item: {e}")
            else:
                print(f"Error: Item ID '{item_id}' not found. Please enter a valid ID from the list.")
                
                print("Available Item IDs:") 
                for item_key in self.items.keys():
                    print(item_key)
                    
    def delete_item(self, item_id):
            if item_id in self.items:
                del self.items[item_id]
                print(f"Item {item_id} deleted successfully.")
            else:
                print(f"Error: Item ID '{item_id}' not found.")   
        
    def list_items(self): 
            if not self.items:
                print("No items available.")
            else:
                for item in self.items.values():
                    print (item)
        
    def update_price_by_id(self, item_id, new_price):
            item = self.get_item(item_id)
            if item:
                try:
                    if not isinstance(new_price, (int, float)) or new_price <=0:
                        raise ValueError("Price must be a positive number.")
                    item.price = new_price
                    print(f"Price of Item ID {item_id} updated to ${new_price:.2f}.")
                    return True
                except ValueError as e:
                    print(f"Error updating price: {e}")
            else:
                print(f"Error: Item ID '{item_id}' not found. Please enter a valid ID from the list.")
                return False 
        
def get_item_input():
            name = input ("Enter item name: ")
            description = input("Enter item description: ")
            while True:
                try:
                    price = float(input("Enter item price: "))
                    if price <=0:
                        print("Price must be a positive number.")
                    else:
                        break
                except ValueError:
                    print("Invalid price. Please enter a number.")
            return name, description, price
        
if __name__ == "__main__":
    manager = ItemManager()
    while True:
        print("\nWelcome to Tenorio's Item Management\n")
        print("1. Add Item")
        print("2. List Items")
        print("3. Update Price")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input ("\nEnter your choice: ") 
        
        if choice == "1":
            name, description, price = get_item_input() 
            manager.add_item(name, description, price)
        elif choice == "2":
            manager.list_items()
        elif choice == "3":
                item_id = input("Enter item ID to update price: ")
                try:
                    new_price = float(input("Enter new price: "))
                    if new_price > 0:
                        manager.update_price_by_id(item_id, new_price)
                    else:
                        print("Price must be a positive number.")
                        
                except ValueError:
                        print("Invalid price. Please enter a number.")
        elif choice == "4":
            item_id = input("Enter item ID to delete: ")
            manager.delete_item(item_id)
        elif choice == "5":
            print("Thank you for using Tenorio's Item Managing System!")
            break
        else:
            print("Invalid choice. Please try again.")             