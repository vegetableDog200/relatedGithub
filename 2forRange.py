import random
from random import randint

newList = []


for i in range(10):
    x = randint(0, 10)
    newList.append(x)
    print(newList[i])