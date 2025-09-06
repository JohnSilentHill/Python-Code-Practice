import time
import random # For % chances

def delayed_print(text, delay=0.5): # Default text delay is .5 seconds
    print(text)
    time.sleep(delay)

# ----- SMOKING FUNCTION -----

def smoke():
    # Variables
    cigarettes_count = 500
    cigarettes_smoked = 0
    coolness_factor = 0
    brand1 = "Marlboro"
    brand2 = "Newport"

    # Dictionary table (expandable for more brands which will each have different coolness factors)
    brands = {
        brand1.lower(): brand1,
        brand2.lower(): brand2
    }

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
            delayed_print(f"Which would you like to smoke? Your options are {brand1} or {brand2}", 0)
            brandAsk = input().strip().lower()

            if brandAsk in brands:
                chosen_brand = brands[brandAsk]
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



# ----- STORE FUNCTION -----



# ----- MENU FUNCTION -----

menu_lines = [
    "---------------------",
    "Smoke cigarettes (Smoke)",
    "Drink beer (Drink)",
    "Go to the store (Store)",
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
    elif do == "quit":
        print("See you later.")
        break
    else:
        delayed_print("Invalid option. Try again.", 1)
