# Logical Operators
# And | Or | Not
# Used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside? : "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go Outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("stay Inside!")