# def num (a,b):
   
#     # sum = a+b
#     return a+b
#     # print(sum)
# # print(num(10,20))


# result = num(10,30)
# print("result is: ",result)
# result1= num(20,30)
# print("result1 is: ",result1)

# def add(a, b):
   
#     return a +b

# def mod(c , d) :

#     return c % d

# result1=  add(2,6)
# result2 = mod(10,2)

# print("total:",add(2,6) + mod(10,2))


def add(a, b):
    return a + b

d = {
    "e": {
        "f": [2, 10, "owais", {"g": "yes"}],
        "h": add(2, 3)  # result is 5
    }
}

print(d["e"]["f"][3]["g"])   # Output: yes
print(d["e"]["h"])           # Output: 5
print(d["e"]["f"][2])