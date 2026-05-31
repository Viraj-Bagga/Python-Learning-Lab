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

#A running list of how many of each items the user recieves. 
perItemTotal = [0,0,0,0,0,0]
totalSum = 0

weights = [.2,.2,.2,.2,.1,.1]

#User starts with 100 gold coins


def main():
    print("Welcome to my mystical loot shop. It appears so thought you dont have any money? That is ok, I will give you 100 gold coins to do with your desire. Each box cost 10 coins, so be wise with your decisions!")

    global current_coins
    global items

    while current_coins >= 10:
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
    global weights
    global loot
    global totalSum
    global item

    item = np.random.choice(list(loot_box), size = 1, p=weights)[0]

    print(item)

    match item:
        case "Sword":
            perItemTotal[0] += 1
        case "Shield":
            perItemTotal[1] += 1
        case "Invisability Potion":
            perItemTotal[2] += 1
        case "Rusty Blade":
            perItemTotal[3] += 1
        case "Armour":
            perItemTotal[4] += 1
        case "Magic Wand":
            perItemTotal[5] += 1

    print(f"You recieved a {item}")
    totalSum += 1
    
    if loot_box[item+""].get("Rarity",0) >= 8:
        current_coins += 20
        print("Congrats! You recieved 20 more coins!")



def finalMessage():
    
    global items
    global current_coins
    global totalSum
    global perItemTotal


    totalItems = totalSum
    swordString = ""
    shieldString = ""
    invisabilityString = ""
    rustyString = ""
    armourString = ""
    magicString = ""


    if perItemTotal[0] > 1:
        swordString = "Swords,"
    elif perItemTotal[0] == 1:
        swordString = "Sword,"
    else :
        swordString = " "
    
    if perItemTotal[1] > 1:
        shieldString = "Shields,"
    elif perItemTotal[1] == 1:
        shieldString = "Shield,"
    else:
        shieldString =  ""
    
    if perItemTotal[2] > 1:
        invisabilityString = "Invisability Potions,"
    elif perItemTotal[2] == 1:
        invisabilityString = "Invisability Potion,"
    else:
        invisabilityString =  ""
    
    if perItemTotal[3] > 1:
        rustyString = "Rusty Blades,"
    elif perItemTotal[3] == 1:
        rustyString = "Rusty Blade,"
    else:
        rustyString =  ""
    
    if perItemTotal[4] > 1:
        armourString = "pieces of Armour,"
    elif perItemTotal[4] == 1:
        armourString = "piece of Armour,"
    else:
        armourString =  ""
    
    if perItemTotal[5] > 1:
        magicString = "and Magic Wands!"
    elif perItemTotal[5] == 1:
        magicString = "and Magic Wand!"
    else:
        magicString =  ""

    print(f"You recieved {totalItems} and have {current_coins} gold coins remaining!")
    print(f"You got {perItemTotal[0]} {swordString} {perItemTotal[1]} {shieldString} {perItemTotal[2]} {invisabilityString} {perItemTotal[3]} {rustyString} {perItemTotal[4]} {armourString} {perItemTotal[5]} {magicString} ")

main()