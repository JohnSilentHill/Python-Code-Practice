import random
import time

def delayed_print(text, delay=0.5): # Default text delay is .5 seconds
    print(text)
    time.sleep(delay)

def dead():
    delayed_print("You pull the trigger...", 1)
    delayed_print("You died. Exiting...")
    quit()

def vsComputer():
    delayed_print("Hello I'm a computer. I haven't made this yet loser.", 1)
    quit()

def solo():
    bullets = 6
    while True:
        shot = random.randint(1, bullets)
        if shot == 1:
            dead()
        else:
            delayed_print("You pull the trigger...", 1)
            delayed_print("Blank.", 1)
            bullets -= 1
            delayed_print(f"{bullets} bullets in the chamber. Continue? (y/n)")
            continueAsk = input("> ").strip().lower()
            if continueAsk == "y":
                continue
            elif continueAsk == "n":
                if bullets == 1:
                    delayed_print("Smart move.", 1)
                    print("Exiting...", 1)
                else:
                    print("Exiting...", 1)
                break
            else:
                print("That wasn't Y or N, exiting regardless...", 1)
                break
    
# Asks if you want to play solo or vs computer

print("Do you want to play against the computer? (Y/N)")
playerChoice = input("> ")
if playerChoice == "y":
    vsComputer()

elif playerChoice == "n":
    solo()

else:
    delayed_print("Please select Y or N.")
