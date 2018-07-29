inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory["pocket"] = ["seashell", "strange berry", "lint"]
inventory["backpack"].remove('dagger')
g = inventory["gold"]
g =g +50
inventory["gold"] = g
for i,n in inventory.items():
    print(i, n)