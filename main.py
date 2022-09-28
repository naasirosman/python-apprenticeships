

def hello_world():
    return "Hello World!"
# def indicates what is next is a function

print(hello_world())
# print() runs a function




#  booleans are 0 and 1 in form of false and true

# numbers are either integers (follow BIDMAS) 
# or floating point decimals

print(17/3) 

# 5.667 is a float point decimal
# // divides and rounds down
# % 
# += *= etc is the same as JavaScript
# https://www.w3schools.com/python/python_operators.asp




# strings



x = "hello world"

y = """hello 
world""" 

print(x)
print(y)
#  triple "" to do multi-line strings




# combining strings and variables
test = "bye"
print("hello " + test) 

# slicing strings
x = "helloworld"
print(x[0:5])
print(x[0:4])
print(x[1:5])
print(x[2:5])
print(x[3:5])
print(x[5:-1])
print(x[5:-3])



# data-types: Lists, Sets, Dictionaries

# lists - usually used for single dimension (same data type) that is redeclarable

a = [99, "string", True, 2.3]

# fetching from a list
print(a[0])

# slicing a list
print(a[1:3])

# push into list list
a.append("hello")
print(a)

# push into specific position

a.insert(1, "bye")
print(a)

# find length
print(len(a))

# replace
a[1:2] = ["replace1"]
print(a)

# multidimension list (c contains a and b)

a = [0, 1, 2, 3, 4, 5]
b = [0, 10, 20, 20, 40, 50]
c = [a, b]
print(c)

# you can append (isnert) a list to it self to make infinite list
c.append(c)
print(c)
# python is smart enough to use [...]
# fetching itself
print(c[2]) 



# dictionary are sets inside sets that corrospond (in pairs)

x = {}
y = { "a":1, "b": 2, "c": 3 }
print(y["a"])

# adding a new pair to dictionary

y["d"] = 4
print(y)

# checking inside list
print("d" in y)
print("e" in y)
del(y["d"])
print("d" in y)



