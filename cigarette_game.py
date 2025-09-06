import time # This is for the time.sleep
import random # This is for the % chance functions

# Variables
cigarettes_count = 500
cigarettes_smoked = 0
coolness_factor = 0
brand1 = "Marlboro"
brand2 = "Newport"


# Dictionary
brands = {
    brand1.lower(): brand1,
    brand2.lower(): brand2
}

# General smoking loop
while True:
    time.sleep(1)
    print(f"Your coolness factor is currently {coolness_factor}!")
    time.sleep(1)
    print(f"You currently have {cigarettes_count} cigarettes.")
    time.sleep(1)

    if cigarettes_smoked >= 2:
        if random.random() < 0.5:
            print("Your lungs imploded and you died.")
            break
    else:
        pass 

    if cigarettes_smoked == 1:
        print("Just a heads up, you've smoked 9 cigs. Smoking one more will likely kill you.")

    if cigarettes_count <= 0:
        time.sleep(1)
        print("You're out of cigs. Go buy more from the shop.")
        break # Ends loop, add a shop function later!
    
    time.sleep(1)
    print("Would you like to smoke one? (Y/N)")
    smoke = input().strip().lower() # This sanitises the input so ignores case/whitespace

    # Smoking action
    if smoke == "y":
        time.sleep(1)
        print(f"Which would you like to smoke? Your options are {brand1} or {brand2}")
        brandAsk = input().strip().lower() # So for things like this, define the user input after the question!

        if brandAsk in brands:
            chosen_brand = brands[brandAsk]
            time.sleep(1)
            print(f"You smoked a {chosen_brand} cigarette.")
            coolness_factor += 1
            cigarettes_smoked += 1
            cigarettes_count -= 1
        else:
            time.sleep(1)
            print("That's not one of the options, dumbass.")
            
    elif smoke == "n":
        time.sleep(2)
        print("Fair enough.")
        break

    else:
        time.sleep(1)
        print("Accepted answers are Y or N.")

