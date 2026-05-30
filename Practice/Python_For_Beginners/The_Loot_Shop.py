# The Loot Shop

# Function : The player starts with 100 gold coins. Players can open 10 gold coin loot boxes until they choose to stop, or run out of money. If the user pulls a legendary item, they immeditally recieve 20 gold coins. 

import random
import numpy as np

loot_box = {
    "Sword" : {
        "Rarity" : 2,
        "Cost" : 5,
        "Chance" : .2
    },
    "Shield" : {
        "Rarity" : 3,
        "Cost" : 5,
        "Chance" : .4
    },
    "Invisability Potion" : {
        "Rarity" : 4,
        "Cost" : 5,
        "Chance" : .6
    },
    "Rusty Blade" : {
        "Rarity" : 6,
        "Cost" : 5,
        "Chance" : .8
    },
    "Armour" : {
        "Rarity" : 7,
        "Cost" : 5,
        "Chance" : .9
    },
    "Magic Wand" : {
        "Rarity" : 9,
        "Cost" : 5,
        "Chance" : 1.0
    }
}

#Numpy cant pick random value with weights on a dested dictionary so I need to flaten it first
loot = ["Sword", "Shield", "Invisability Potion", "Rusty Blade", "Armour", "Magic Wand"]

#Keeps track of the players coin count at any given moment
current_coins = 100

items = []

weights = [.2,.2,.2,.2,.1,.1]

#User starts with 100 gold coins


def main():
    print("Welcome to my mystical loot shop. It appears so thought you dont have any money? That is ok, I will give you 100 gold coins to do with your desire. Each box cost 10 coins, so be wise with your decisions!")

    global current_coins
    global items

    while current_coins != 0:
        currentChoice = makeChoice()

        if (currentChoice) == "y":
            current_coins -= 10
            openLoot()
        else :
            break

    finalMessage()


def makeChoice():
    choice = input("Enter y if you would like to open a box : ")

    return choice

def openLoot():

    
    global loot_box
    global current_coins
    global items
    global weights

    item = np.random.choice(list(loot_box), size = 1, p=weights)[0]

    print(f"You recieved a {item}")
    items.append(item)
    
    if loot_box[item+""].get("Rarity",0) >= 8:
        current_coins += 20
        print("Congrats! You recieved 20 more coins!")


    


def finalMessage():
    
    global items
    global current_coins

    totalItems = len(items)

    print(f"You recieved {totalItems} and have {current_coins} gold coins remaining!")

main()