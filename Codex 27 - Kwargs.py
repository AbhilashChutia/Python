# **kwargs
# Parameter that will pack all arguments into a dictionary
# Useful so that a fucntion can accept a varying amount of keyword arguments

def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.", first="Abhialsh", middle="Ghost",last="Chutia")