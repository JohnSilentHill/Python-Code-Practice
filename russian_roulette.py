import sys, time, random

def typing(text, delay=0.05):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Adds a newline at the end

# Playerstates

def dead():
    typing("You died. Exiting...")
    quit()

def aiDead():
    typing("Your opponent died. Exiting...")
    quit()

# VS Computer gamemode

def vsComputer():
    bullets = 6
    player_turn = random.choice([True, False])  # Randomly choose who starts

    if player_turn:
        time.sleep(1)
    else:
        typing("Your opponent will begin.")
        time.sleep(1)

    while bullets > 0:
        if player_turn:
            typing("Your turn.")
            time.sleep(1)
            typing(f"{bullets} bullets in the chamber. Pull the trigger? (y/n)")
            choice = input("> ").strip().lower()
            if choice == "y":
                typing("You pull the trigger...")
                time.sleep(1)
                shot = random.randint(1, bullets)
                if shot == 1:
                    dead()
                else:
                    typing("Blank.")
                    time.sleep(1)
                    bullets -= 1
            elif choice == "n":
                typing("Exiting...")
                break
            else:
                typing("That wasn't Y or N, exiting regardless...")
                break
        else:
            typing(f"{bullets} bullets in the chamber.")
            time.sleep(1)
            typing("Your opponent pulls the trigger...")
            time.sleep(1)
            shot = random.randint(1, bullets)
            if shot == 1:
                aiDead()
            else:
                typing("Blank.")
                time.sleep(1)
                bullets -= 1

        player_turn = not player_turn

# Solo mode

def solo():
    bullets = 6
    while True:
        shot = random.randint(1, bullets)
        if shot == 1:
            dead()
        else:
            typing("You pull the trigger...")
            time.sleep(1)
            typing("Blank.")
            time.sleep(1)
            bullets -= 1
            typing(f"{bullets} bullets in the chamber. Pull the trigger? (y/n)")
            continueAsk_solo = input("> ").strip().lower()
            if continueAsk_solo == "y":
                continue
            elif continueAsk_solo == "n":
                if bullets == 1:
                    typing("Smart move.")
                    typing("Exiting...")
                else:
                    typing("Exiting...")
                break
            else:
                typing("That wasn't Y or N, exiting regardless...")
                break
    
# Asks if you want to play solo or vs computer

typing("Do you want to play against the computer? (Y/N)")
playerChoice = input("> ")
if playerChoice == "y":
    vsComputer()

elif playerChoice == "n":
    solo()

else:
    typing("Please select Y or N.")
