# Dictionary
# Changeable, Unordered Collection
# Unique key:value pairs

capitals = {'Usa':'Washington DC', 'India':'New Delhi', 'China':'Beijing', 'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})

# capitals.pop('China')
# capitals.clear()

# print(capitals['India'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key,value in capitals.items():
    print(key, value)