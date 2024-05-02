# Inheritance in python helps us to define a class that inherits the members of another class.The members of a class  includes the variabls, functions and methods of the class. In inheritance, we use two major types of class. We have superclass which is the topmost class that includes the members to be inherited in other class, then we have the derives or the subclass that inherits the members of the superclass.
 #inheritance is used to promote old reusability

# Implementing inheritance in inventory management system
class products:
    def __init__(self, name, price, quantity):  
        self.name = name
        self.price =price
        self.quantity =quantity

    def calculate_total_cost(self):
        return self.price * self.quantity

class Electronics(products): #creating subclass of products class
    def __init__(self, name, price, quantity, warranty):
        # super is a reference to the superclass and its members
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def display_info(self):
        print(f" Product name: {self.name} price: ${self.price}, quantity: {self.quantity}, warranty: {self.warranty} months")
        print(f"Total: {self.calculate_total_cost()}")

class clothing(products):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def display_info(self):
        print(f"Product name:{self.name} price: ${self.price}, quantity: {self.quantity}, size: {self.size}")
        print(f"Total: {self.calculate_total_cost()}")
def main():
    print("Enter details for Electronics item")
    electronics_name=input("Enter Product's Name: ")
    electronics_price=float(input("Enter Product's Price: "))
    electronics_quantity=int(input("Enter Product's Quantity: "))
    electronics_warranty=int(input("Enter Product's Warranty: "))
    electronics_item = Electronics(electronics_name,electronics_price,electronics_quantity,electronics_warranty)
    
    print("Enter details for clothing item")
    clothing_name=input("Enter Cloth Name: ")
    clothing_price=float(input("Enter Cloth's Price: "))
    clothing_quantity=int(input("Enter Cloth's Quantity: "))
    clothing_size=int(input("Enter Cloth's Size: "))
    clothing_item = clothing(clothing_name,clothing_price,clothing_quantity,clothing_size)

    print("\nDisplaying Product Information")
    print("Electronics item")
    electronics_item.display_info()

    print("clothing item")
    clothing_item.display_info()

if __name__ =="__main__":
     main()
     



    