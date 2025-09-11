import random
import time

bullets = 6

def delayed_print(text, delay=0.5): # Default text delay is .5 seconds
    print(text)
    time.sleep(delay)

def dead():
    delayed_print("You died. Exiting...")
    quit()

def value():
    return random.randint(1, bullets) # Apparently you need to put in 'return' because fuck me I guess

while True:
    if value() == 1:
        dead()
        break
    else:
        print("The gun didn't go off.")
        delayed_print(f"{bullets} bullets in the chamber. Continue? (y/n)")
        ask = input("> ").strip().lower()
        if ask == "y":
            bullets -= 1
            continue
        else:
            print("Exiting...")
            break
