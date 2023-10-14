import os

source = "C:\\Users\\Abhilash\\Desktop\\test.txt"
destination = "C:\\Users\\Abhilash\\Desktop\\MCA\\testmoved.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")