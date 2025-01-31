'''
#q1
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}! Your age is  {age} years.")
#q2
value = input("Enter your value: ")

if value.isdigit():
    output = int(value)
    print(f"Converted Value: {output} (Type: integer)")
# Check if the input is a float (contains only one decimal point and digits)
elif value.replace(".", "", 1).isdigit() and value.count(".") == 1:
    output = float(value)
    print(f"Converted Value: {output} (Type: float)")
else:
    print(f"DataType of ur input is string")
  
#q3

colorlist = ["red", "blue", "green"]
for color in colorlist:
    print(color.upper())

deletecolor=input("Enter any color from the list u wanna delete: ")  
if deletecolor in colorlist:
  colorlist.remove(deletecolor) 
else: print("color not in list")
    
addcolor=input("Enter any color u want to add in list: ") 
colorlist.append(addcolor)   
for color in colorlist:
    print(color.upper())

 
#q4
my_tuple = ("hey", 20, 30.1, "bye")

first, second, *rest = my_tuple  # *rest stores remaining elements (if any)

# Print the unpacked values
print("First element:", first)
print("Second element:", second)

#q5

students_grades = {}

# Loop to take input for 5 students
for i in range(5):
    name = input("Enter student's name: ")
    grade = input("Enter {name}'s grade: ")
    students_grades[name] = grade

print("\nStudent Grades Dictionary:")
print(students_grades)


#q6 

n1 = int(input("Enter the number of elements for the first list: "))
list1 = []
for i in range(n1):
    element = input(f"Enter element {i+1}: ")
    list1.append(element)

n2 = int(input("\nEnter the number of elements for the second list: "))
list2 = []
for i in range(n2):
    element = input(f"Enter element {i+1}: ")
    list2.append(element)

# Convert the lists to sets
set1 = set(list1)
set2 = set(list2)

# Perform set operations
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

# Display the results
print("\nUnion of the sets:", union)
print("Intersection of the sets:", intersection)
print("Difference of the sets (set1 - set2):", difference)



#q7
num = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print(f"The number {num} is positive")
elif num < 0:
     print(f"The number {num} is negative")
else:
     print("The number zero")

# Check if the number is even or odd
if num % 2 == 0:
    print(f"The number parity is even")
else:
     print(f"The number parit is odd")
 
#q8
# Print numbers from 1 to 50
for i in range(1, 51):
    
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else: 
        print(i)
        
       
#q9
def func(num):
   
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result



num=int(input("Enter a positive number:"))
factorial=func(num)
print(factorial) 
#q10
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n /2) + 1):
        if n % i == 0:
            return False
    return True

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
'''
'''
#q11

def square_numbers(lst):
     new= []
     for x in lst:
        new.append(x * x) 
     return new


n1 = int(input("Enter the number of elements for the  list: "))
list = []
for i in range(n1):
    element = int(input(f"Enter element {i+1}: "))
    list.append(element)


squared_numbers = square_numbers(list)

print("Original list:",list)
print("Squared list:", squared_numbers)
'''
'''
#q12

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

# Merge dict2 into dict1 (dict2's values will overwrite dict1's in case of duplicate keys)
dict1.update(dict2)

print("Merged dictionary:", dict1)
'''

#Remove Duplicates from a List
'''
def remove_duplicates(lst):
    seen = set()  # Set to keep track of already seen elements
    result = []   
    
    for num in lst:
        if num not in seen:  
            result.append(num) 
            seen.add(num)  
    
    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(numbers)
unique = remove_duplicates(numbers)
print("List after removing duplicates:", unique)

'''

#Palindrome Checker
'''
s = input("Enter a string: ")

if s == s[::-1]:
    print( "is a palindrome.")
else:
    print(" is not a palindrome.")
'''
#Fibonacci Sequence Generator
'''
def generate(n):
    sequence = []
    
    # First two Fibonacci numbers
    a, b = 0, 1
    
    for i in range(n):  
        sequence.append(a)  
        a, b = b, a + b  
    
    return sequence


n = int(input("Enter a number: "))  

fibonacci_numbers = generate(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_numbers}")
'''

#Average Calculator with Validation
'''
def average(numbers):
    return sum(numbers) / len(numbers)


def valid(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


n1 = valid("Enter the number of elements for the list: ")
list = []

for i in range(n1):
    element = valid(f"Enter element {i + 1}: ")
    list.append(element)


print(f"The average is: {average(list)}")

'''

#Nested Loops: Multiplication Table
'''
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()  '''
    
    #User Registration System
    
'''
users = {}


def register():
    username = input("Enter a username: ")
    
    if username in users:
        print("Username already exists. Please choose a different one.")
        return
    
    password = input("Enter a password: ")

    users[username] = password
    print(f"User '{username}' registered successfully!")


def login():
    username = input("Enter your username: ")
    
    
    if username not in users:
        print("Username does not exist. Please register first.")
        return
    
    password = input("Enter your password: ")

    if users[username] == password:
        print(f"Welcome, {username}!")
    else:
        print("Incorrect password.")


while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
'''

#Counting Elements with a Dictionary

'''
dictionary = {}


words = input("Enter a list of words separated by spaces: ").split()

for word in words:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
print(dictionary)
'''

#Temperature Converter

'''
choice = input("Enter 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").upper()

if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F.")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C.")
else:
    print("Invalid choice. Please enter 'C' or 'F'."

'''