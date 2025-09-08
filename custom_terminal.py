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

# --------- HELP ---------

def help():

    lines=[
    "For more information on a specific command, just figure it out because I'm not adding all that.",
    "",
    "HELP                Displays the list of commands, duh",
    "EXIT                Exits the terminal",
    "",
    "INFO   [Invalid]    Relays terminal info",
    "GOTOP  [Invalid]    Displays GOTOP",
    "NEOFETCH            Displays NEOFETCH",
    "",
    "HELLO               Prints 'hello world'",
    "PWORDGEN            Starts a password generator",
    ""
    ]

    print("\n" + "\n".join(lines) + "\n")

# --------- EXIT ---------

def exit_terminal():
    
    exitconfirm = input("Do you want to exit the terminal? (Y/N) > ").strip().lower()
    if exitconfirm == "y":
        print("Exiting terminal...")
        sys.exit()  # Exits without causing a stack overflow, whoops
    else:
        print("Returning to terminal.")
        delayed_print("")

# --------- HELLO ---------

def hello():

    print("Hello World!")
    delayed_print("")

# --------- PASSWORD ---------

def generate_password():
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
        else:
            delayed_print("Not a valid password length.")
    else:
            delayed_print("Unrecognised command.")

# --------- INFO ---------

def info():
    print("")

# --------- GOTOP ---------

def gotop():
    print("")

# --------- NEOFETCH ---------

def neofetch():

    lines = [
    "JohnSilentHill@DESKTOP-1",
    "-------------------",
    "Uptime: 21 hours 17 minutes",
    "OS: JohnOS [64-bit]",
    "Packages: 5 [scoop]",
    "-------------------",
    "Motherboard: No motherboard found",
    "Memory: No memory found",
    "CPU: No CPU found",
    "GPU: No GPU found",
    "Disk (C:): 0.01 TiB / 1.8 TiB"
    ]

    time.sleep(1)
    print("\n" + "\n".join(lines) + "\n")
    
# Dictionary
commands = {
    "help": help,
    "exit": exit_terminal,
    "hello": hello,
    "info": info,
    "gotop": gotop,
    "neofetch": neofetch,
    "pwordgen": generate_password
}

def repeaterror():
    print("Bro please just type 'help' already.")
    print("")
    error_count = 0

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

