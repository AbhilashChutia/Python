# Nested Loops
# Inner loop wil finish all of it's iterations first.
# Then Outer loop will start

rows = int(input("How many rows? : "))
columns = int(input("How many columns ? : "))
symbol = input("Enter a symbol to be used : ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()