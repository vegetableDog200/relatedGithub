characterA = {'strength':1,
              'dexterity':2,
              'constitution':3,
              'intelligence':4,
              'wisdom':5,
              'charisma':6}
print(characterA)
for key in characterA.items():
    print(key)

if(characterA.get('strength')==None):
    print("that isn't a character stat.")
else: print(characterA.get('strength'))

if(characterA.get('speed')==None):
    print("that isn't a character stat.")
else: print(characterA.get('speed'))