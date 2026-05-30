# The Loot Shop

# Function : The player starts with 100 gold coins. Players can open 10 gold coin loot boxes until they choose to stop, or run out of money. If the user pulls a legendary item, they immeditally recieve 20 gold coins. 

import random

loot_box = {
    "Sword" : {
        "Rarity" : 2,
        "Cost" : 5,
        "Chance" : .1
    },
    "Shield" : {
        "Rarity" : 3,
        "Cost" : 5,
        "Chance" : .2
    },
    "Invisability Potion" : {
        "Rarity" : 4,
        "Cost" : 5,
        "Chance" : .2
    },
    "Rusty Blade" : {
        "Rarity" : 6,
        "Cost" : 5,
        "Chance" : .2
    },
    "Armour" : {
        "Rarity" : 7,
        "Cost" : 5,
        "Chance" : .1
    },
    "Magic Wand" : {
        "Rarity" : 9,
        "Cost" : 5,
        "Chance" : .1
    }
}

current_coins = 100


#User starts with 100 gold coins


def main():
    print("Welcome to my mystical loot shop. It appears so thought you dont have any money? That is ok, I will give you 100 gold coins to do with your desire. Each box cost 10 coins, so be wise with your decisions!")

    global current_coins

    while current_coins != 0:
        currentChoice = makeChoice()

        if (currentChoice) == "y":
            current_coins -= 10
            openLoot()
        else :
            break

    print("That loop was broken")

    



def makeChoice():
    choice = input("Enter y if you would like to open a box : ")

    return choice

def openLoot():

    print("Opening Loot")
    global loot_box
    global current_coins
    item = random.choice(list(loot_box))
    print(item)

    if (loot_box.get(item,{}).get("Rarity",{}) >= 8):
        current_coins += 20
        print("Congrats! You recieved 20 more coins!")


def finalMessage():
    print("Final Message")

main()