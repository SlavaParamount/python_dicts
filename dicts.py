d1 = {'d': 1, 'c': 1000, 'b': 111, }


#sort dictionary
ds1 = sorted(d1) #growing by key
ds2 = sorted(d1, reverse= True) ##decrease by key

ds3 = sorted(d1, key=d1.get) #growing by definition
ds4 = sorted(d1, key=d1.get, reverse=True) #decrease by definition


print(ds1)
print(ds2)
print(ds3)
print(ds4)

#addition of dicts

d2 = {'x': 500, 49: 'asdasd'}

c = {**d1, **d2}

print(c)

# extract values with * operator

print(*d1)

d3 = {'d': '1', 'a': 5, 'c': '3'}

def printPetNames(owner, **pets):
   print(f"Owner Name: {owner}")
   for pet,name in pets.items():
      print(f"{pet}: {name}")
printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")