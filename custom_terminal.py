# Boring crap to make shit work
import sys
import time
import string
import random

string.ascii_letters
string.digits
string.punctuation

# Generic text delay function
def delayed_print(text, delay=0.5):
    print(text)
    time.sleep(delay)

# Command functions

# ---------

def help():

    print("For more information on a specific command, just figure it out because I'm not adding all that.")
    print("")
    print("HELP                Displays the list of commands, duh") 
    print("EXIT                Exits the terminal")
    print("")
    print("HELLO               Prints 'hello world'")
    print("PWORDGEN            Starts a password generator")
    print("")

# ---------

def exit_terminal():
    
    exitconfirm = input("Do you want to exit the terminal? (Y/N) > ").strip().lower()
    if exitconfirm == "y":
        print("Exiting terminal...")
        sys.exit()  # Exits without causing a stack overflow, whoops
    else:
        print("Returning to terminal.")
        delayed_print("")

# ---------

def hello():

    print("Hello World!")
    delayed_print("")

# ---------

def generate_password():
    while True:
        delayed_print("PASSWORD GENERATOR", 0.5)
        delayed_print("Usage: 'generate password [length]", 0.5)
        delayed_print("-----------------")
        generate = input("> ").strip().lower()
        parts = generate.split()

        if len(parts) == 3 and parts[0] == "generate" and parts[1] == "password":
            if parts[2].isdigit():
                length = int(parts[2])
                if length < 5:
                    delayed_print("Minimum length of 5 characters.")
                else:
                    # Create pool of characters to choose from
                    characters = string.ascii_letters + string.digits

                    # Generate password
                    password_random = random.choices(characters, k=length)
                    password = ''.join(password_random)

                    delayed_print("-----------------")
                    if length > 20:
                        delayed_print("Are you really going to remember this?")
                        delayed_print("\n")
                    delayed_print("Your password:")
                    delayed_print(password)
                    print("")
                    break
            else:
                delayed_print("Not a valid password length.")
        else:
            delayed_print("Unrecognised command.")


# Dictionary
commands = {
    "help": help,
    "exit": exit_terminal,
    "hello": hello,
    "pwordgen": generate_password
}

def repeaterror():
    print("Bro please just type 'help' already.")
    print("")

error_count = 0

# Pre user input terminal banner
print("")
delayed_print("JohnSilentHill's Terminal [Version 1.0.0]", 0.2)
delayed_print("Copyright: None, feel free to copy.", 0.2)
print("")

# Main command input
while True:
    user_input = input("C:\\Users\\John>").strip().lower()

    if user_input in commands:
        commands[user_input]()  # () is important. It actually calls the function here.
    else:
        print(f"'{user_input}' is not recognized as an internal or external command,\noperable program or batch file.\n")
        error_count += 1
        if error_count >= 10:
            repeaterror()
