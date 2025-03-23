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
                            max_id_int = max(max_id_int)
                        
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
        def get_item
            