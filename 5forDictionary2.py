import random

keys = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
characterA = {}
for v in keys:
    characterA[v] = random.randint(1, 20)
print(characterA)




