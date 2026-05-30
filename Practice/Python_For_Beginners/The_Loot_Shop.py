# The Loot Shop

# Function : The player starts with 100 gold coins. Players can open 10 gold coin loot boxes until they choose to stop, or run out of money. If the user pulls a legendary item, they immeditally recieve 20 gold coins. 

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

#User starts with 100 gold coins
current_coins = 100

def main():
    print("Welcome to my mystical look shop. It appears so thought you dont have any money? That is ok, I will give you 100 gold coins to do with your desire. Each box cost 10 coins, so be wise with your decisions!")

    while current_coins != 0:
        currentChoice = makeChoice()

        if (currentChoice) == "y":
            openLoot()
        else :
            finalMessage()



def makeChoice():
    choice = input("Enter y if you would like to open a box, and anything else if you dont want to")

    return choice

def openLoot():
    current_coins -= 10
    print("Opening Loot")


def finalMessage():
    print("Final Message")

main()