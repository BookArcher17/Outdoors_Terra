import sys
import time

def type_text(text):
    """Print text nice and slow for effect i reckon"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def start_game():
    print("===============================================")
    print("        WELCOME TO WILDERNESS SURVIVAL         ")
    print("===============================================")
    type_text("You wake up alone in a dense forest, with no memory of how you got there")
    type_text("All you know is that you need to survive")
    type_text("The sun is setting and the temperature is dropping.\n")

    #Health and Stuff
    health = 100
    inventory = []

    first_choice(health, inventory)

def first_choice(health, inventory):
    print("---THE CRASH SITE---")
    type_text("What is your first move?")
    print("1. Stay with the plane wreckage and build a signal fire.")
    print("2. Head into the woods and search for water")
    choice = input ("\nEnter 1 or 2:").strip()

    if choice == "1":
        signal_fire_path(health, inventory)
    elif choice == "2":
        woods_path(health, inventory)

    else:
        print("\Invalid choice. The panic sets in. Try again.")   
