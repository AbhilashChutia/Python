# Nested Functions
# Function calls inside other function calls
# Innermost function calls are resolved first
# Returned value is used as arg for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))