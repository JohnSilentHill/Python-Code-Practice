import time
import random
import msvcrt # This is for windows key input detection

def delayed_print(text, delay=0.5): # Default text delay is .5 seconds
    print(text)
    time.sleep(delay)

## GLOBAL VARIABLES -- these can be accessed from all functions and essentially save as you switch 

coolness_factor = 0
money = 25
cigarettes_count = 500
cigarettes_smoked = 0
beers_drank = 0
beers_count = 10

# ----- SMOKING FUNCTION -----

def smoke():
    import random  # Needed for lung failure check

    # Pull variables
    global coolness_factor, cigarettes_count, cigarettes_smoked

    # Coolness dictionary
    cigcoolness_factors = {
        "Newport": 7,
        "Camel": 4,
        "Marlboro Red": 6,
        "Marlboro Gold": 5,
        "American Spirit Blacks": 10,
        "L&B": 2,
        "L&M Blue": 8
    }

    # Cig names
    cig_brands = list(cigcoolness_factors.keys())

    # Lookup tables
    cigbrands = {brand.lower(): brand for brand in cig_brands}
    coolness_lookup = {k.lower(): v for k, v in cigcoolness_factors.items()}

    while True:
        delayed_print("---------------------", 0.5)
        delayed_print(f"Your coolness factor is currently {coolness_factor}!", 1)
        delayed_print(f"You currently have {cigarettes_count} cigarettes.", 1)

        if cigarettes_smoked >= 500:
            if random.random() < 0.5:
                delayed_print("Your lungs imploded and you died.", 1)
                break

        if cigarettes_smoked == 499:
            delayed_print("Just a heads up, you've smoked 499 cigs. Smoking one more will likely kill you.", 1)

        if cigarettes_count <= 0:
            delayed_print("You're out of cigs. Go buy more from the shop.", 1)
            break

        delayed_print("---------------------", 0.5)
        delayed_print("Would you like to smoke one? (Y/N)", 0)
        delayed_print("---------------------", 0.5)
        smoke_input = input("Your choice: ").strip().lower()

        if smoke_input == "y":
            delayed_print("---------------------", 0.5)
            delayed_print(f"Which brand would you like to smoke? Your options are: {', '.join(cig_brands)}", 0)
            brandAsk = input("Your choice: ").strip().lower()

            if brandAsk in cigbrands:
                chosen_brand = cigbrands[brandAsk]
                cigarettes_count -= 1

                # Exceptions
                if chosen_brand.lower() == "american spirit blacks":
                    cigarettes_smoked += 2
                else:
                    cigarettes_smoked += 1

                points = coolness_lookup[brandAsk]
                coolness_factor += points

                delayed_print("---------------------", 0.5)
                delayed_print(f"You smoked a {chosen_brand} cigarette.", 1)
                delayed_print(f"You gained {points} coolness points!", 1)
            else:
                delayed_print("That's not one of the options, dumbass.", 1)

        elif smoke_input == "n":
            delayed_print("---------------------", 0.5)
            delayed_print("Fair enough.", 1)
            break

        else:
            delayed_print("---------------------", 0.5)
            delayed_print("Accepted answers are Y or N.", 1)

# ----- DRINKING FUNCTION -----

def drink():

    # Pull variables
    global coolness_factor, beers_count, beers_drank

    # Coolness dictionary
    beercoolness_factors = {
        "Budweiser": 6,
        "Heineken": 6,
        "Corona": 2,
        "Moretti": 5,
        "Desperados": 3,
        "Guiness": 10,
        "Carling": 2,
        "Coors Light": 1
    }

    # Drink names
    beer_brands = list(beercoolness_factors.keys())

    # Lookup tables
    beerbrands = {brand.lower(): brand for brand in beer_brands}
    coolness_lookup = {k.lower(): v for k, v in beercoolness_factors.items()}

    while True:
        delayed_print("---------------------", 0.5)
        delayed_print(f"Your coolness factor is currently {coolness_factor}!", 1)
        delayed_print(f"You currently have {beers_count} beers.", 1)

        if beers_drank >= 20:
            if random.random() < 0.5:
                delayed_print("Your liver packed in and you died.", 1)
                break

        if beers_drank == 19:
            delayed_print("Just a heads up, you've drank 19 beers. Your liver is crying. Be careful.", 1)

        if beers_count <= 0:
            delayed_print("You're out of beer. Go buy more from the shop.", 1)
            break

        delayed_print("---------------------", 0.5)
        delayed_print("Would you like to drink one? (Y/N)", 0)
        drink_input = input("Your choice: ").strip().lower()

        if drink_input == "y":
            delayed_print("---------------------", 0.5)
            delayed_print(f"Which beer are you cracking open? Your options are: {', '.join(beer_brands)}", 0.5)
            brandAsk = input("Your choice: ").strip().lower()

            if brandAsk in beerbrands:
                brand_proper = beerbrands[brandAsk]
                beers_count -= 1
                
                # Exceptions
                if brand_proper.lower() == "guiness": # Counts for 2
                    beers_drank += 2
                
                elif brand_proper.lower() == "coors light": # Counts for 0, pathetic drink
                    beers_drank -= 0

                else:
                    beers_drank += 1

                points = coolness_lookup[brandAsk]
                coolness_factor += points

                delayed_print("---------------------", 0.5)
                delayed_print(f"You chugged a {brand_proper}.", 1)
                delayed_print(f"You gained {points} coolness points!", 1)
            else:
                delayed_print("That's not one of the options, dumbass.", 1)

        elif drink_input == "n":
            delayed_print("---------------------", 0.5)
            delayed_print("Fair enough.", 1)
            break

        else:
            delayed_print("---------------------", 0.5)
            delayed_print("Accepted answers are Y or N.", 1)

# ----- STORE FUNCTION HERE -----

# This handles the menu

def show_store_menu():
    store_menu = [  # This table compacts the old stupid bulky list
        "---------------------",
        "STORE:",
        "Please select one of the options below by typing in the abbreviation.",
        "---------------------",
        "Buy Beer : $4 : (Type: 'beer')",
        "Buy Cigarettes Pack (10) : $12 : (Type: 'cigs')",
        "Leave Store : (Type: 'exit')",
        f"Current Money: ${money}",
        "---------------------"
    ]
    for line in store_menu:
        delayed_print(line, 0.5)

# This handles the input functions

def store():
    global money, inventory, beers_count, cigarettes_count

    while True:
        show_store_menu()

        buy = input("Your choice: ").strip().lower()

        if buy == "beer":
            if money >= 4:
                beers_count += 1
                money -= 4
                delayed_print("You bought 1 Beer.")
            else:
                delayed_print("Not enough money.")
        
        elif buy == "cigs":
            if money >= 12:
                cigarettes_count += 10
                money -= 12
                delayed_print("You bought 1 pack of Cigarettes (10).")
            else:
                delayed_print("Not enough money. Go earn some.")
        
        elif buy == "exit":
            delayed_print("Leaving store...")
            delayed_print("---------------------", 0.5)
            break
        
        else:
            delayed_print("Invalid option. Try again.")

        delayed_print(f"Money left: ${money}")
            


# ----- STATS FUNCTION -----

def stats():

    # Pull variables
    global cigarettes_smoked, beers_drank

    while True:
        delayed_print("---------------------", 0.5)
        delayed_print("STATS:", 1)
        delayed_print(f"You have smoked {cigarettes_smoked} cigs and drank {beers_drank} beers.", 0.5)
        time.sleep(1) # This is here because the stupid delayed_print below doesn't want to work
        delayed_print("Press any key to return to the menu.", 1)
        delayed_print("---------------------", 0.5)
        msvcrt.getch()
        break

# ----- MENU FUNCTION -----

menu_lines = [ # This table acts the same as the store function and compacts dialogue
    "---------------------",
    "Smoke cigarettes (Smoke)",
    "Drink beer (Drink)",
    "Go to the store (Store)",
    "View your stats (Stats)",
    "Quit the game (Quit)",
    "---------------------"
]

while True:
    delayed_print("---------------------", 0.5)
    print("Welcome to Hell Yeah Simulator.")
    time.sleep(1)
    print("What would you like to do?")
    time.sleep(1)

    for line in menu_lines:
        delayed_print(line)

    do = input("Your choice: ").strip().lower()

    # Disgusting elif statements

    if do == "smoke":
        smoke()

    elif do == "drink":
        drink() 

    elif do == "store":
        store()

    elif do == "stats":
        stats() 

    elif do == "quit":
        print("See you later.")
        break

    else:
        delayed_print("Invalid option. Try again.", 1)
