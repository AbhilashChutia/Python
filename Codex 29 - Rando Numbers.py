import random

x = random.randint(1,6)
y = random.random()

mylist = ['rock','paper','scisors']
z = random.choice(mylist)

print(x)
print(y)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)