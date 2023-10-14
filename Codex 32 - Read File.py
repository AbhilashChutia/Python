try:
    with open('C:\\Users\\Abhilash\\Desktop\\Hello.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")