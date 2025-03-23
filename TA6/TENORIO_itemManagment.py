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
        return f"ID: {self.id}, \nName: {self.name}, \nDescription: {self.description}, \nPrice: $" 
        