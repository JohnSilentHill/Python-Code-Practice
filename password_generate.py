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

delayed_print("Usage: 'generate password [length]", 0.5)

# The command:
while True:
    generate = input("> ").strip().lower() # The user input starts with "> "
    parts = generate.split()

    # This handles what the user types
    if len(parts) == 3 and parts [0] == "generate" and parts[1] == "password": 
    # if amount of parts = 3, and the first part [0] is "generate", and the second part [1] is "password":
   
        if parts[2].isdigit():

            length = int(parts[2]) # This sets up for defining the length of the password by the integer used in part [2], or the 1-10 input.
        
            # Actual password generation function
            def generate_password(length):
                # 1. Create pool of characters to choose from
                characters = string.ascii_letters + string.digits + string.punctuation

                # 2. Randomly pick characters
                password_list = random.choices(characters, k=length) # Generates characters, 'k' = how many times it pulls from 'characters'

                # 3. Create password
                password = ''.join(password_list)

                # 4. Finally print it as an output
                print(password)
            break
    
        else:
            delayed_print("Not a valid password length.") # User didn't input 1-10 after "generate password"
    else:
        delayed_print("Unrecognised command.")












