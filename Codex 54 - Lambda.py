# lambda
# One line
# Uses lambda keyword
# Throw away function

# lambda parameters:expression

# def double(x):
#     return x * 2

# print(double(2))

double = lambda x:x * 2
multiply = lambda x, y:x * y
add = lambda x, y, z:x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False
print(double(5))
print(multiply(4,5))
print(add(10, 20, 30))
print(full_name("Abhilash", "Chutia"))
print(age_check(24))