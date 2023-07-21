# Slicing
# indexing[] or slice()
# [start:stop:step]

# name = "Abhilash Chutia"
#
# first_name = name[0:4:1]
# last_name = name[9:15:1]
# funky_name = name[0:8:2]
#
# reversed_name = name[::-1]
#
# print(first_name)
# print(last_name)
# print(funky_name)
#
# print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4,1)

print(website1[slice])
print(website2[slice])