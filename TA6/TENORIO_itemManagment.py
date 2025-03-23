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
        return f"ID: {self.id}, \nName: {self.name}, \nDescription: {self.description}, \nPrice: $ {self.price:2f}"

class ItemManager:
    def __init__(self):
        self.items = {}
        self.existing_ids = []
        
    def generate_unique_id(self):
        
        def generate_unique_id_internal(existing_ids=None):
            if existing_ids is None:
                next_id_int = 1
            else:
                if not existing_ids:
                    next_id_int = 1
                else:
                    try: 
                        max_id_int = 0
                        for id_str in existing_ids:
                            max_id_int = max(max_id_int, int(id_str))
                        next_id_int = max_id_int + 1
                    except ValueError:
                        raise ValueError("Existing IDs must be valid integers convertible to string.")
                return f"{next_id_int:03d}" 
            unique_id = generate_unique_id_internal(self.existing_ids)
            self.existing_ids.append(unique_id)
            return unique_id
        
    def add_item(self, name, description, price):
            try:
                item_id = self.generate_unique_id()
                item = Item(name, description, price, item_id)
                self.items[item.id] = item
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
                        if not name:
                            raise ValueError("Name cannot be empty.")
                        item.name = name
                    if description: 
                        if not description:
                            raise ValueError("Description cannot be empty.")
                        item.description = description
                    if price:
                            if not isinstance(price, (int, float)) or price <= 0:
                                    raise ValueError("Price must be a positive number.")
                            item.price = price
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
                if item_id in self.existing_ids:
                    self.existing_ids.remove(item_id)
        
    def list_items(self): 
            for item in self.items.values():
                print(item)
        
    def update_price_by_id(self, item_id, new_price):
            item = self.get_item(item_id)
            if item:
                try:
                    if not isinstance(new_price, (int, float)) or new_price <=0:
                        raise ValueError("Price must be a positive number.")
                    item.price = new_price
                    print(f"Error: Price of Item ID {item_id} updated to ${new_price:.2f}")
                except ValueError as e:
                    print(f"Error updating price: {e}")
            else:
                print(f"Error: Item ID '{item_id}' not found. Please enter a valid ID from the list.")
                print("Available Item IDs: ")
                for item_key in self.items.keys():
                    print(item_key)
                return False 
            return True
        
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
        print("\nOptions")
        print("1. Add Item")
        print("2. List Items")
        print("3. Update")
        print("4. Exit")
        
        choice = input ("Enter your choice: ") 
        
        if choice == "1":
            name, description, price = get_item_input() 
            manager.add_item(name, description, price)
        elif choice == "2":
            manager.list_items()
        elif choice == "3":
            while True:
                item_id = input("Enter item ID to update price: ")
                while True:
                    try:
                        new_price = float(input("Enter new price: "))
                        if new_price <=0:
                            print("Price must be a positive number.")
                        else:
                            break
                    except ValueError:
                        print("Invalid price. Please enter a number.")
                if manager.update_price_by_id (item_id, new_price):
                    break 
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")             