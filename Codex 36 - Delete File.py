import os
import shutil

path = "C:\\Users\\Abhilash\\Desktop\\test.txt"

try:
    # os.remove(path)       # Delete File
    # os.remove(path)       # Delete Empty Directory
    # shutil.rmtree(path)   # Delete a Dir containing Files
    os.remove(path)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have the permission to delete that!")
else:
    print(path+" was deleted!!")