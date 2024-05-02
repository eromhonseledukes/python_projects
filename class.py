print("This is My first Python class")  # code to print a string
name = "Tom Young"    # code to print a variable 
print(type(name))
print(name)

# A code to add 2 numbers and display result
num1 = 55
print(type(num1))
num2 = 88
sum = num1 + num2
print(sum)

# indentation: Used to indicate the beginning and the ending of a block of code in python
if 5 > 2:  # if/conditional statement
    print("five is greater than two")  # child statement

    # DATA TYPES: Used to indicate the type of value stored in a variable
    # different categories of data
    # 1. text data type
        # 1a string data type --- a collection of characters (must be in quotes)
    # 2. numeric type
         # 2a integer   2b float
    # 3 sequence type
       # 3a list   and 3b tuple: both list and tuple are used for storing collection of values
    # 4. mapping data type
       # 4a dictionary data type uses key and value pairs. Key represent a variable. Eg a product name is key, and the value is type of product



       # A Code to Declare a list Called Items
items = ["tea","sugar","butter"]
print(items)



# PYTHON DATA TYPES

# In python, a data type is determined by value asigned to th variable. A variable can be explicitly or declared defaultly

# Explicitly declare
num1 = int(20)
print(num1)

name = str("Abraham")
print(name)

height = float(5.8)
print(height)

# Default Declaration
num1 = 20
print(num1)

name = "Abraham"
print(name)

height = 1.7
print(height)


# CASTING: Casting is the conversion from one data type to another: There are 2 types of casting: Explicit and implicit casting

# Explicit casting is converting from higher to lower data type
# Implicit casting is converting lower to higher data type. eg
# float is higher in capacity to store moe value than interger

x = 10
y = 5.1

x = float(10)
print(x)

y = int(5.1)
print(y)


# STRINGS: Array of characters surrounded by a single or double quotes
# ARRAY: A collection of variable of the same data type
# Each item in an array is refered to as the element of th array
# Each Element in an array can be referenced using the index which represent the position of the element in the array
# An array starts indexing from zero. that means first elent in the array collection will take the position = zero

name = 'Abraham'
name = "Abraham"

name = "My name is Abraham"
# name = "Rex"

# Passing the string as an aguement to print function
print("my name is Abraham")
print(name)


# Arrays and strings: to print 
print(name[0])
print(name[3])
print(name[2])

# LENGHT FUNCTION: the lenght function returns the lenght or number of characters in a string (count characters including the space)

print(len(name))

# STRING SLICING: Used for returning thev range of characters
# It includes the start index which represent first element in the range and the endindex which represent the last element in the range

greetings = "Hello, World!"
print(greetings[0:6])


# CONVERTING CASES USING PYTHON, CHANGING STRINGS FROM AN UPPER TO LOWER CASE.VICE VERSA

text = "Hello, World!"
print(text.lower())
print(text.upper())
print(text.capitalize())

# FINDING SUB-STRINGS
# Substrings are used for displaying a part of the string
text2 = "python is easy to learn, python is easy to use"

# Count method is used for checking the occureance of a substring in the main string
print(text2.count("python"))

# FIND METHOD. Returns the position where the substring
print(text2.find("is"))

# SPLITING AND JOINING OF STRINGS - Split Methods /Join Method
# SPLIT METHOD
text3 = "laptop, headphone, mobilephone"
product_list = text3.split(",")  # It will return ['laptop', 'Headphone', 'mobilephone']
print(product_list)

# JOIN METHOD. Will join the list element with specified symbol
new_text = "-".join(product_list)
print(new_text)

# REPLACE METHOD:  Replaces a character or string with another
text4 = "Abraham is my Name"
print(text4.replace("Abraham", "Iyiola"))

# STRING CONCATENATOR: It joins or combine 2or more strings together
firstname = "Iyiola"
lastname = "Abraham"
fullname = firstname + " " + lastname
print("My fullname is :" + fullname)

# STRING FORMAT OR FORMATTTING A STRING
# Is a place holder used for combining a string with a number
age = 21
text5 = "My age is {} years old.".format(age)
print(text5)

quantity = 3
itemno = 505
price = 49.50
myorder = "I want {} pieces of item {} for {} naira"
print(myorder.format(quantity,itemno,price))

# PYTHON LISTS: 
# used for storing multiple items in a single variable
sample_list = ["Orange", "Banana", "Apple", "Mango"]
print(sample_list)
print(sample_list[0])
print(sample_list[3])

# LIST LENGHT FUNCTION
# used for displaying number of items in the list

# DIFF BTW ARRAY AND LIST: Array = similar data type of list. But list can contain an array of diferent data types
print(len(sample_list))

# RANGE OF INDEXES IN A LIST: 
# Index has to do with the position of each element in a list
print(sample_list[0:2])
print(sample_list[0:4])

# Excluding some items from a list of collections
print(sample_list[:1])

# PRINT FROM AN INDEX POSITION TO THE END
print(sample_list[1:])

# TO CHECK IF AN ITEM IS PART OF A LIST AND RETURN A MESSAGE
if "Apple" in sample_list:
    print("yes, 'Apple' is in sample list")


    # HOT TO CHANGE OR UPDATE LIST ITEMS
    # TO change an item in the list, you use the position of the item. You reference item to be changed using the position or index
    sample_list[0] = "mango" # change mango to apple
    print(sample_list)

    # CHANGING A RANGE OF ITEMS
    sample_list [1:3] = ["kiwi","pear"]
    print(sample_list)

    # INSERTING ITEMS TO A LIST
    # Two ways to insert an item to a list:  1: The append function 2: The Insert method

    # 1: APPEND: Append function adds an item at the end of list
    sample_list.append(["grapes"]) # grapes will be added
    print(sample_list)

    # 2: INSERT: This allows you to add an element to a position on the list
    sample_list.insert(1, "Cashiew")
    print(sample_list)

    sample_list.append(["Clementine"])
    print(sample_list)

    # EXTENDING A LIST:  = adding another list to the end of a list. Like combining 2 lists

    products = ["laptop", "phone", "Tablet"]
    sample_list.extend(products)
    print(sample_list)

    # REMOVING AN ITEM FROM LIST [REMOVE METHOD AND POP METHOD]
    # 1: REMOVE will remove an iten based on specified item name
    # 2: POP will remove an item based on specified item position

    # REMOVE
    sample_list.remove("phone") 
    print(sample_list)# phone will be removed from the list

    # POP METHOD
    sample_list.pop(2) # item in3rd position will remove
    print(sample_list)

    # CLEAR METHOD:    Used To Empty A List
    #  sample_list.clear()
    # print(sample_list)

    # DELETE METHOD: TO Delete Entire List From THe System Memory
    # del sample_list

    # ITERATING OR LOOPING THROUGH A LIST
    # Enables you print all items in a list one by one
    for i in sample_list : # i represent each/every item in list
        print(i)     # loop through

        # SORTING A LIST: Arranging items in a list in ascending or decending order
    newlist = ["Yam", "Garri", "Rice"]
    newlist.sort() # sort in ascending order by default
    print(newlist)

    # DESCENDING ORDER
    newlist.sort(reverse=True)
    print(newlist)


    # 12 - 04 - 2024
    #  LIST DICTIONARY: Is a collection for removing items using he key and value pairs. The key in a dictionary is a type of variable that stores its value
    # A dictionary is efficient in storing both single/multiple item values in a single variable

    this_dict = {
        'brand' : 'Ford',
        'model' : 'Fiesta',
        'year' : '2005',
        'courses' : ['Maths', 'Physics', 'Chemistry'],
    }
    print(this_dict)

    # INVENTARY APPLICATION USING DICTIONARY
    inventory = {
        'apple' : 50,
        'banana' : 75,
        'orange' : 60,
        'watermelon' : 40,
    }
    # To UPdate the dictionary collection
    inventory['banana'] += 20
    inventory['orange'] += 30
    # To print updated inventory
    print("display updated inventory")

    for item, quantity in inventory.items():
        print(f"{item.capitalize()} : {quantity} ")
        # The f is for formatted to enable us capitalize output
        print(f"{item} : {quantity} ")



        # 16 - 04 - 2024

        #CONDITIONAL STATEMENTS: Used in python for decision making and for changing the normal flow of programme based on the condition 
        # If statements are used to execute a block of code if the condition is true
        #Elif  and else : used to add additional condition or privide a default action if the condition in an if statement is false
        # Elif is for stisfying multiple conditions

    # EXAMPLE of a Grading System that prompt user to enter the grade number
    grade = int(input("Enter your grade: "))
    if grade >= 90:
        print("Your Grade is A+")
    elif grade >= 85:
        print("Your Grade is A")
    elif grade >= 80:
        print("Your Grade is B+")
    elif grade >= 70:
        print("Your Grade is B")
    elif grade >= 60:
        print("Your Grade is C+")
    elif grade >= 50:
        print("Your Grade is C")
    elif grade >= 45:
        print("Your Grade is D+")
    elif grade >= 40:
        print("Your Grade is D")
    else:
        print("Your Grade is F")


        # EXAMPLE 2 : A Voting system that determines user Eligibility to vote
    age = int(input("Enter your age: "))
    in_prison = input("Are You Currently in Prison? yes/no :",).lower()
    if age >= 18 and in_prison!="yes":
        print("You are  eligible to vote")
    elif age < 18 and in_prison == "no":
        print("You are not eligible to vote")
    elif age >= 18 and in_prison =="yes":
        print("You Must be Out of Prison Before You can Vote")

    else:
        print("You are not eligible to vote")


        # FUNCTIONS IN PYTHON

        # Functions in python are independent and reusableblock of codes which performs a specific task. 
        # Function makes the programme more organised and easier to manage.
        # Each unit or section of your programme or application can refer to a function

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            return num1 / num2
    else:
        print("Invalid operation")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose Operation(+, -, *, /): ")

result = calculator(num1, num2, operation)
print("Result:", result)


#        17/04/2024
#   CLASSES AND OBJECTS IN PYTHON

# A BANK APPLICATION USING CLASSES AND OBJECTS
# A CLASS = a blueprints for creating an object
# OBJECT = A real world entity with attributes and methods
# In python, we create an object with attributes and methods.using the class. The attributes are reffered to as the variables

class BankAccount:
    # Constructors used for initializing the variables to be used in the class.

    def __init__(self, customer_name, bank_name, account_number, initial_deposit, initial_balance=0.0) :
        # initializing the variables using a constructor
        self.customer_name = customer_name
        self.account_number = account_number
        self.initial_balance = initial_balance
        self.bank_name = bank_name
        self.initial_deposit = initial_deposit


        # Declaring Methods which means actions to be performed by customers.
        # DEPOSITS
    def deposit(self, amount):
        self.initial_balance += amount
        print(f"Deposited {amount}. Current balance: {self.initial_balance}")

        # WITHDRAWALS
    def withdraw(self, amount):
        if amount <= self.initial_balance:
            self.initial_balance -= amount
        else:
            print("Insufficient Funds")

    # TO CHECK BALANCE OF ACCOUNT
    def check_balance(self):
        print(f"Current balance: {self.initial_balance}")        

    # TO DECLARE variable for TRANSFER FUNDS
    def transfer_funds(self, recipient_account, amount):
        if self.initial_balance >= amount:
            self.withdraw(amount)
            recipient_account.deposit(amount)
            print(f"transfered {amount} from {self.customer_name} at{self.bank_name} to{recipient_account.customer_name} at {recipient_bank_name}. ")
        else:
            print("Insufficient Funds for transfer")

    
        
        # To PROMPT USER TO ENTER THIER ACCOUNT DETAILS
customer_name = input("Enter your name: ")
bank_name = input("Enter your bank name: ")
account_number = int(input("Enter your account number: "))


        # CREATING AN OBJECT TO INVOKE/CALL ALL THE THE METHOD
account1 = BankAccount(customer_name, account_number, initial_deposit)

# TO DISPLAY ACCOUNT INFORMATION
account1.display_info()

# TO CREATE THE BANK ACCOUNT OBJECT OR INSTANCE
account1 = BankAccount(customer_name, bank_name, account_number)

# TO PROMPT CUSTOMERS TO DEPOSIT AN AMOUNT
deposit_amount = float(input("Enter how much you want to deposit: "))
account1.deposit(deposit_amount)

# TO PROMPT CUSTOMERS TO WITHDRAW AN AMOUNT
withdrawal_amount = float(input("Enter how much you want to withdraw: "))
account1.withdraw(withdrawal_amount)

# PROMPT CUSTOMER TO TRANSFER TO TRANSFER FUNDS
recipient_bank_name = input("Enter recipient bank name: ")
recipient_account_number = input("Enter recipient account number: ")
recipient_customer_name = input("Enter recipient customer name: ")
transfer_amount = float(input("Enter how much you want to transfer: "))

# TO CREATE RECIPIENT BANK ACCOUNT OBJECT OR INSTANCE
recipient_account = BankAccount(recipient_customer_name, recipient_account_number, recipient_bank_name)

# TO TRANSFER FUNDS TO RECIPIENT ACCOUNT
account1.transfer_funds(recipient_account, transfer_amount)

# TO DISPLAY UPDATED ACCOUNT INFORMATION
account1.display_info()

# TO DISPLAY UPDATED BALANCES FOR BOTH SENDER AND RECIPIENT
print("\nSender's balance and details :")

account1.display_info()

print(f"Sender Name : {account1.customer_name}")
print(f"Sender Account Number : (account1.account_number)")
print(f"Sender Bank Name : (account1.bank_name)")  

print("\nRecipient's balance and details :")
recipient_account.check_balance()
print(f"Recipient Name : {recipient_account.customer_name}")
print(f"Recipient Account Number : (recipient_account.account_number)")
print(f"Recipient Bank Name : (recipient_account.bank_name)")


    






        
        

    















