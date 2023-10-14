# str.format() = Optional Method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format("cow","moon"))

# Variables
print("The {} jumped over the {}".format(animal,item))

# Positional
print("The {1} jumped over the {0}".format(animal,item))

# Keyword
print("The {animal} jumped over the {item}".format(animal="hare",item="house"))