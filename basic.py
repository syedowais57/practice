# # name =  "syed owais "
# # print(name)
# # age =20
# # print(age)

# # height_m = int (input ("Enter the number of meters: "))

# # height_cm = height_m * 100
# # print("height in cm is: " + str(height_cm))


# # age = int(input("Enter your age: "))
# # if age > 18:
# #     print("you are an adult")
# # elif age >= 13:
# #     print("you are a teenager")
# # else:
# #     print("you are a child")


# # temp = int(input("Enter the temprature celsius: "))
# # temp_f = (temp * 9/5) + 32
# # print(f"temprature in fahrenheit is: {temp_f}")

# # year = int(input("Enter the year :"))
# # if (year % 4 == 0 and year % 100 != 0 )or (year % 400 == 0) :
# #     print(f"{year} is leap yaer")
# # else :
# #   print(f"{year }is not a leap year")



# # students = {
# #     "101": {"name": "Alice", "age": 20, "grade": "A"},
# #     "102": {"name": "Bob", "age": 22, "grade": "B"},
# #     "103": {"name": "Charlie", "age": 19, "grade": "A"}
    
# # }

# # # Accessing nested data
# # print(students["101"]["name"])   
# # print (students["103"]["age"])

# # s = "PythonRocks"
# # print(s[2:8])

# # num = [1 ,2,3 ,4,5,6]
# # sqr =[]

# # for i in num :
# #     if i % 2 == 0:
# #      sqr.append(i**2)
     
# # print(sqr[::-1])
# # def reverse(arr):
# #    return arr[::-1] 

# # print(reverse([1,2,3]))

# # def count_even_numbers (num):
# #        count= 0
# #        for i in num :
         
# #          if i % 2 == 0:
# #              count= count + 1
       
# #        return count
# # l = []
# # print(count_even_numbers(l))
       
# # l =        

# # for i in range(1 ,100):
# #     print("owais")
 


# # l = [2,7,5,6,3,9]
# # # e = []
# # # o =[]
# # def evn(x):
# #       return x %2==0
# # def odd(x):
# #       return x % 2!= 0
      
# # # print(e)
# # # print(o)
# # even = list (filter(evn , l))
# # oddd = list(filter(odd , l))
# # # evn=list(filter(lambda x : x % 2 == 0,l))
# # print(even)
# # print(oddd)




# # from functools import reduce
# # l = [2,7,5,6,3,9]
# # sqr = reduce(lambda a,b : a + b , l)
# # print(sqr)

# # classes

# # class Car_company:
# #     def alto(self):
# #         print("alto")
# #     def swift(self):
# #         print("swift")
# #     def both(self):
# #            self.alto()
# #            self.swift()
           
        



        
# # obj_company = Car_company()
# # # obj_company.swift()
# # # obj_company.alto()
# # obj_company.both()

# # arr = list(int(input("enter the list")))
# # valueToMatch =input("enter the value to match")

# # def valueTomatch( arr, valueToMatch):
# #     arr= [1,2,3,4,5,6]
# #     valueTo= input("enter the number to match")
# #     for i in arr :
# #       if i == valueTomatch :
# #         print(i)   

# # print(valueTomatch())
# # arr = [1, 2, 3, 4, 5, 6]

# # def func(arr, valueToMatch):
# #     for i in range(len(arr)):  
# #         if arr[i] == valueToMatch:
# #             return i  

# #     print("No match found")
# #     return None

# # result = func(arr, 1)
# # print("Index:", result)

# # def sum ():
# #     total=0
# #     for i in range(1,101):
# #            total=total+i
# #     return total
# # result = sum()
# # print(result)



# # def rvs():
# #        arr = [1, 2, 3, 4, 5]
# #        reversed_arr = []

# #        for i in range(len(arr) -1 , -1, -1): 
# #         reversed_arr.append(arr[i])
      
# #        return reversed_arr

# # reslt = rvs()
# # print(reslt)
# # # print("Original:", arr)
# # # print("Reversed:", reversed_arr)


# def fizzBuzz(n):
#      if n % 3==0 and n % 5 ==0 :
#            print("FizzBUzz")
#      elif n % 3 ==0 :
#            print("Fizz")
#      elif n % 5 == 0 :
#          print("Buzz")

# fizzBuzz(15)   
         

     


# def push(lst, value):
#     lst  += [value]  
#     return lst


# # def pop(lst):
# #     if len(lst) == 0:
# #         raise IndexError("pop from empty list")
# #     last = lst[-1]
# #     del lst[-1]
# #     return last


# def insert(lst, value):
#     lst[:] = [value] + lst  
#     return lst



# def shift(lst):
#     if len(lst) == 0:
#         raise IndexError("shift from empty list")
#     first = lst[0]
#     lst[:] = lst[1:]
#     return first



# my_list = [1, 2, 3]

# push(my_list, 4)
# print("After push:", my_list)     

# shift(my_list)       
# print("after shift" , my_list)

# # pop(my_list)
# # print("After unshift:", my_list)   

# # shift_val = (my_list)
# # print("After shift:", my_list)     
# # print("Shifted value:", shift_val) 
# insert(my_list , 0)
# print("after insert" , my_list)

# def tables(numbers):
    
#     for num in numbers:
#         print(f"\nMultiplication table for {num}:")
#         for i in range(1, 11):
#             print(f"{num} x {i} = {num * i}")


# my_list = [2, 3, 5]
def simpleexp(exp):
    num1 = ''
    num2 = ''
    operator = ''
    found_operator = False

    for ch in exp:
        if ch in "+-*/%":
            operator = ch
            found_operator = True
        elif not found_operator:
            num1 += ch
        else:
            num2 += ch

    num1 = int(num1)
    num2 = int(num2)

   
    print("num1 =", num1)
    print("num2 =", num2)
    print("operator =", operator)

    return num1, num2, operator

# Example
exp = "654+5623"
simpleexp(exp)
