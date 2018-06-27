inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    """
    Prints the inventory items of an inventory with the total number of items
    :param inventory:
    """
    totalItems = 0
    print('Inventory:')
    for item, quantity in inventory.items():
        totalItems += quantity
        print(f'{quantity} {item}')
    print(f'total number of items {totalItems}')


def addToInventory(inventory, itemsToAdd):
    """
    Takes a list of items and add them to an inventory
    :param inventory: map of items
    :param itemsToAdd: list of item names
    """
    for item in itemsToAdd:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1


addToInventory(inventory, dragonLoot)

displayInventory(inventory)
