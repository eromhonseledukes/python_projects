'''String Manipulation:
a. Create a string variable named "sentence" with the value "The quick brown fox jumps over the lazy dog."
b. Use string methods to convert the sentence to all uppercase.

c. Then, split the sentence into words and store them in a list.
d. Print the list.

List Operations:
a. Create a list named "numbers" with the values [10, 20, 30, 40, 50].
b. Append the number 60 to the list.
c. Insert the number 5 at index 0.
d. Remove the number 30 from the list.
e. Print the modified list.

String Concatenation and List Conversion:
a. Create two lists named "first_names" and "last_names" with at least three elements each.
b. Use string concatenation and a loop to create a new list named "full_names" that contains the full names (first name + last name) of each person.
c. Print the full_names list.

String Formatting and List Indexing:
a. Create a list named "students" with at least three strings representing student names.
b. Use string formatting to print out a message for each student indicating their position in the list (e.g., "Student 1: [Name]").
c. Use list indexing to print out the third student's name.

String Searching and List Filtering:
a. Create a list named "words" with at least five strings.
b. Use a loop to iterate through the list and print only the words that contain the letter 'a'.
c. Use list comprehension to create a new list named "filtered_words" that contains only the words with more than five characters.
d. Print the filtered_words list.

String Slicing and List Slicing:
a. Create a string variable named "text" with a sentence of your choice.
b. Use string slicing to extract the first five characters of the sentence and print them.
c. Create a list named "numbers" with the values [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
d. Use list slicing to extract every third number from the list and print them.'''

# String Manipulation
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence)
print(sentence.upper())

mylist = "the, quick, brown, fox, jumps, over, the, lazy, dog"
list1 = mylist.split(",")
print(list1)

# List operations
numbers =[10, 20, 30, 40, 50]
print(numbers)

numbers.Append([60])
print(numbers)

numbers.insert[0, (5)]
print(numbers)

numbers.remove(30)
print(numbers)

# String concatenation and list conversion
first_name = ["John", "Abel", "June", "Agnes"]
print(first_name)

last_name = ["Boris", "Aggrippa", "Navas", "Ian"]
print(last_name)

fullnames = [first-name[0] + " " + last_name[0], + " " + first_name[1] + " " + last+name[1], + " " + first_name[2] + " " + last_name[2], + first_name[3] + " " + last_name[3]]
print(fullnames)
for i in fullname :
    print(i)

    # String formatting and list indexing
    student = ["Judith", "Caroline", "Elizabeth"]
    print(student)

    height = 1.7
    age = 22
    weight = 58
    text2 = "student[0] is {} meters tall.". format(height)
    print(text2)
    text3 = "student[1] is {} years old.".format(age)
    print(text3)
    text4 = "student[2] weighs about {} kg.".format(weight)
    print(text4)

    print(student[2])

    # String searching and list filtering
    words = ["Came", "Go", "Jump", "shout", "sat"]
    print(words)
    for word in words:
        if 'a' in word:
            print(words)


        # string slicing and list slicing
        text = "I have a good home"
        print(text[0:6])

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(numbers[2], [5], [8])

    



