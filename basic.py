# name =  "syed owais "
# print(name)
# age =20
# print(age)

# height_m = int (input ("Enter the number of meters: "))

# height_cm = height_m * 100
# print("height in cm is: " + str(height_cm))


# age = int(input("Enter your age: "))
# if age > 18:
#     print("you are an adult")
# elif age >= 13:
#     print("you are a teenager")
# else:
#     print("you are a child")


# temp = int(input("Enter the temprature celsius: "))
# temp_f = (temp * 9/5) + 32
# print(f"temprature in fahrenheit is: {temp_f}")

# year = int(input("Enter the year :"))
# if (year % 4 == 0 and year % 100 != 0 )or (year % 400 == 0) :
#     print(f"{year} is leap yaer")
# else :
#   print(f"{year }is not a leap year")



# students = {
#     "101": {"name": "Alice", "age": 20, "grade": "A"},
#     "102": {"name": "Bob", "age": 22, "grade": "B"},
#     "103": {"name": "Charlie", "age": 19, "grade": "A"}
    
# }

# # Accessing nested data
# print(students["101"]["name"])   
# print (students["103"]["age"])

# s = "PythonRocks"
# print(s[2:8])

# num = [1 ,2,3 ,4,5,6]
# sqr =[]

# for i in num :
#     if i % 2 == 0:
#      sqr.append(i**2)
     
# print(sqr[::-1])
# def reverse(arr):
#    return arr[::-1] 

# print(reverse([1,2,3]))

# def count_even_numbers (num):
#        count= 0
#        for i in num :
         
#          if i % 2 == 0:
#              count= count + 1
       
#        return count
# l = []
# print(count_even_numbers(l))
       
# l =        

# for i in range(1 ,100):
#     print("owais")
 
l = [2,7,5,6,3,9]
# e = []
# o =[]
def evn(x):
      return x %2==0
def odd(x):
      return x % 2!= 0
      
# print(e)
# print(o)
even = list (filter(evn , l))
oddd = list(filter(odd , l))
# evn=list(filter(lambda x : x % 2 == 0,l))
print(even)
print(oddd)

