import time
import random
import msvcrt # This is for windows key input detection

def delayed_print(text, delay=0.5): # Default text delay is .5 seconds
    print(text)
    time.sleep(delay)

## GLOBAL VARIABLES -- these can be accessed from all functions and essentially save as you switch 
## You can edit money or cigarettes starting values as you please

coolness_factor = 0
money = 25
cigarettes_count = 500
cigarettes_smoked = 0
beers_drank = 0
beers_count = 10

# ----- SMOKING FUNCTION -----

def smoke():
    
    # Pull variables
    global coolness_factor
    global cigarettes_count
    global cigarettes_smoked
   
    # Brands list
    cig_brands = ["Newport", "Camel", "Marlboro Red", "Marlboro Gold"]

    # Dictionary
    cigbrands = {cigbrand.lower(): cigbrand for cigbrand in cig_brands}

    while True:
        delayed_print(f"Your coolness factor is currently {coolness_factor}!", 1)
        delayed_print(f"You currently have {cigarettes_count} cigarettes.", 1)

        if cigarettes_smoked >= 10:
            if random.random() < 0.5:
                delayed_print("Your lungs imploded and you died.", 1)
                break

        if cigarettes_smoked == 9:
            delayed_print("Just a heads up, you've smoked 9 cigs. Smoking one more will likely kill you.", 1)

        if cigarettes_count <= 0:
            delayed_print("You're out of cigs. Go buy more from the shop.", 1)
            break

        delayed_print("Would you like to smoke one? (Y/N)", 0)
        smoke_input = input().strip().lower()

        if smoke_input == "y":
            delayed_print(f"Which brand would you like to smoke? Your options are: {', '.join(cig_brands)}", 0)
            brandAsk = input().strip().lower()

            if brandAsk in cigbrands:
                chosen_brand = cigbrands[brandAsk]
                delayed_print(f"You smoked a {chosen_brand} cigarette.", 1)
                coolness_factor += 1
                cigarettes_smoked += 1
                cigarettes_count -= 1
            else:
                delayed_print("That's not one of the options, dumbass.", 1)

        elif smoke_input == "n":
            delayed_print("Fair enough.", 1)
            break

        else:
            delayed_print("Accepted answers are Y or N.", 1)

# ----- DRINKING FUNCTION -----

def drink():

    # Pull variables
    global coolness_factor
    global beers_count
    global beers_drank

    # Brands list
    beer_brands = ["Budweiser", "Heineken", "Corona", "Moretti"]

    # Dictionary
    beerbrands = {brand.lower(): brand for brand in beer_brands}

    while True:
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

        delayed_print("Would you like to drink one? (Y/N)", 0)
        drink_input = input().strip().lower()

        if drink_input == "y":
            delayed_print(f"Which beer are you cracking open? Your options are: {', '.join(beer_brands)}", 0)
            brandAsk = input().strip().lower()

            if brandAsk in beerbrands:
                chosen_brand = beerbrands[brandAsk]
                delayed_print(f"You chugged a {chosen_brand}.", 1)
                coolness_factor += 1
                beers_drank += 1
                beers_count -= 1
            else:
                delayed_print("That's not one of the options, dumbass.", 1)

        elif drink_input == "n":
            delayed_print("Fair enough.", 1)
            break

        else:
            delayed_print("Accepted answers are Y or N.", 1)

# S----- STORE FUNCTION HERE -----



# ----- STATS FUNCTION -----

def stats():

    # Pull variables
    global cigarettes_smoked
    global beers_drank

    while True:
        delayed_print("---------------------", 0.5)
        delayed_print("STATS:", 1)
        delayed_print(f"You have smoked {cigarettes_smoked} cigs and drank {beers_drank} beers.", 0.5)
        time.sleep(1) # This is here because the stupid delayed_print below doesn't want to work
        delayed_print("Press any key to return to the menu.", 1)
        msvcrt.getch()
        break

# ----- MENU FUNCTION -----

menu_lines = [
    "---------------------",
    "Smoke cigarettes (Smoke)",
    "Drink beer (Drink)",
    "Go to the store (Store)",
    "View your stats (Stats)",
    "Quit the game (Quit)"
]

while True:
    print("Welcome to Hell Yeah Simulator.")
    time.sleep(1)
    print("What would you like to do? Your options are the following:")
    time.sleep(1)

    for line in menu_lines:
        delayed_print(line)

    do = input().strip().lower()

    if do == "smoke":
        smoke()  # Calls the smoking function

    elif do == "drink":
        drink() # Calls the drinking function

    elif do == "stats":
        stats() # You guessed it, calls the stats function

    elif do == "quit":
        print("See you later.")
        break

    else:
        delayed_print("Invalid option. Try again.", 1)
