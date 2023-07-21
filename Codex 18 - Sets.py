# Set
# Collection Unordered, Unindexed, No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()

# utensils.update(dishes)
# dishes.update(utensils)

# for x in utensils:
#     print(x)

# dinner_table = utensils.union(dishes)
#
# for x in dinner_table:
#     print(x)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))
