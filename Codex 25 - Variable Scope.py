# Scope
# The region that a variable is recognized
# Var is only available inside the region it is cresated in.
# Globally / Locally scoped variable can be created

name = "Ghost"

def display_name():
    name = "Abhilash"
    print(name)

display_name()
print(name)

# Local
# Enclosing
# Global
# Built-in