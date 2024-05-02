holidays = ["sunday", "monday", "tuesday"]
# Deleting items in a list
holidays.remove('sunday')
#print(holidays)
# Using del keyword
del holidays[1]
print(holidays)

# Using pop() method  : removes and return the remaining item in a list
holidays = ["sunday", "monday", "tuesday"]

holidays.pop(1)
holidays.pop()  # removes the last item in a list
#holidays.clear()  # removes all the items in a list

# LIST COMPREHENSION IN PYTHON
# List comprehension is an elegant way to define and create lists based on existing
songs = [ "Chioma Jesus,", "Amazing Grace,", "Ngozi Chukwu"]
item1, item2, item3 = songs
print(item1, item2, item3)
print(item1.join(", "), item2, item3)

# USER INPUT IN PYTHON
user_input = input('enter your username') # input always accept strings by default. unless you convert it to other data types
print(user_input)


# IF STATEMENT
holiday = True
if holiday == True:
    print("you are on holiday")
else:
    print("you are not on holiday")


    # BUIDING GUESS MY THOUGHT GAME
    brain = ['Education', 'Maths', 'Science', 'Protein']
    random_thinking = random.choice(brain)
    user_input = input('what is my thinking?')
    if user_input == random_thinking:
        print('you are right')
        print(random_thinking)
        print(brain)
        brain.remove(random_thinking)
        print(brain)    
        
         
        