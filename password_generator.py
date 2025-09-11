# Boring crap to make shit work
import time
import string
import random

string.ascii_letters
string.digits
string.punctuation

# Generic text delay
def delayed_print(text, delay=0.5):
    print(text)
    time.sleep(delay)

delayed_print("-----------------")
delayed_print("Usage: 'generate password [length]", 0.5)
delayed_print("-----------------")

# Actual password generation function

def generate_password(length):

    print("Would you like to include punctuation? (Y/N)")
    userinput = input("> ").strip().lower()
    
    # 1. Create pool of characters to choose from based on user choice
    if userinput == "y":
        characters = string.ascii_letters + string.digits + string.punctuation
    
    else:
        characters = string.ascii_letters + string.digits

    # 2. Randomly pick characters
    password_random = random.choices(characters, k=length) # Generates characters, 'k' = how many times it pulls from 'characters'

    # 3. Create password
    password = ''.join(password_random) # '' Refers to the separator, being no spaces between returned characters. .join makes a string

    # 4. This just returns a generated output
    return password

# The command:
while True:
    generate = input("> ").strip().lower() # The user input starts with "> "
    parts = generate.split()

    # This handles what the user types
    if len(parts) == 3 and parts [0] == "generate" and parts[1] == "password": 
    # if amount of parts = 3, and the first part [0] is "generate", and the second part [1] is "password":
   
        if parts[2].isdigit():
            length = int(parts[2]) # This sets up for defining the length of the password by the integer used in part [2], or the 1-10 input.
            if length < 5:
                delayed_print("Minium length of 5 characters.")
            else:
                password = generate_password(length)
                delayed_print("-----------------")
                if length > 20:
                    delayed_print("Are you really going to remember this?")
                delayed_print("Your password:")
                delayed_print(password)                 
            break
    
        else:
            delayed_print("Not a valid password length.") # User inputted <5 after "generate password"
    else:
        delayed_print("Unrecognised command.")












