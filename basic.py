# --- Variables and Basic I/O ---
name = "syed owais"
print(name)

age = 20
print(age)

# Convert meters to centimeters
height_m = int(input("Enter the number of meters: "))
height_cm = height_m * 100
print("Height in cm is: " + str(height_cm))

# --- Conditional Statements ---
age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")

# Temperature conversion from Celsius to Fahrenheit
temp = int(input("Enter the temperature in Celsius: "))
temp_f = (temp * 9/5) + 32
print(f"Temperature in Fahrenheit is: {temp_f}")

# Leap Year Checker
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# --- Dictionaries and Nested Data ---
students = {
    "101": {"name": "Alice", "age": 20, "grade": "A"},
    "102": {"name": "Bob", "age": 22, "grade": "B"},
    "103": {"name": "Charlie", "age": 19, "grade": "A"}
}
print(students["101"]["name"])
print(students["103"]["age"])

# --- String Slicing ---
s = "PythonRocks"
print(s[2:8])

# --- List Comprehension and Reversing ---
num = [1, 2, 3, 4, 5, 6]
sqr = []
for i in num:
    if i % 2 == 0:
        sqr.append(i**2)
print(sqr[::-1])

# Reverse using function
def reverse(arr):
    return arr[::-1]
print(reverse([1, 2, 3]))

# --- Function to Count Even Numbers ---
def count_even_numbers(num):
    count = 0
    for i in num:
        if i % 2 == 0:
            count += 1
    return count
l = []
print(count_even_numbers(l))

# --- Loop Printing ---
for i in range(1, 100):
    print("owais")

# --- Filter Even and Odd Numbers ---
l = [2, 7, 5, 6, 3, 9]
def evn(x):
    return x % 2 == 0

def odd(x):
    return x % 2 != 0

even = list(filter(evn, l))
oddd = list(filter(odd, l))
print(even)
print(oddd)

# --- Reduce Example (Sum of List) ---
from functools import reduce
l = [2, 7, 5, 6, 3, 9]
sqr = reduce(lambda a, b: a + b, l)
print(sqr)

# --- Classes and Methods ---
class Car_company:
    def alto(self):
        print("alto")
    def swift(self):
        print("swift")
    def both(self):
        self.alto()
        self.swift()

obj_company = Car_company()
obj_company.both()

# --- Search Index of Value in List ---
arr = [1, 2, 3, 4, 5, 6]
def func(arr, valueToMatch):
    for i in range(len(arr)):
        if arr[i] == valueToMatch:
            return i
    print("No match found")
    return None

result = func(arr, 1)
print("Index:", result)

# --- Sum from 1 to 100 ---
def sum():
    total = 0
    for i in range(1, 101):
        total += i
    return total

result = sum()
print(result)

# --- Reverse List using For Loop ---
def rvs():
    arr = [1, 2, 3, 4, 5]
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

reslt = rvs()
print(reslt)

# --- FizzBuzz Example ---
def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")

fizzBuzz(15)

# --- Implementing Array Methods (push, shift, insert) ---
def push(lst, value):
    lst += [value]  # Adds to end
    return lst

def insert(lst, value):
    lst[:] = [value] + lst  # Adds to front
    return lst

def shift(lst):
    if len(lst) == 0:
        raise IndexError("shift from empty list")
    first = lst[0]
    lst[:] = lst[1:]  # Removes first element
    return first

my_list = [1, 2, 3]
push(my_list, 4)
print("After push:", my_list)

shift(my_list)
print("After shift:", my_list)

insert(my_list, 0)
print("After insert:", my_list)
