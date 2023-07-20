# Loop Control Statements
# Changes a loop execution from its normal sequence

# break = used to terminate a loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name : ")
#     if name != "":
#         print("Hello "+name)
#         break

phone = "123-456-7890"

for i in phone:
    if i == "-":
        continue
    print(i, end="")