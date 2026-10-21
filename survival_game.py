import sys
import time

def type_text(text):
    """Print text nice and slow for effect i reckon"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def display_status(health, hydration, inventory):
    print("\n" + "="*40)
    print(f"❤️Health: {health}% |💧 Hydration: {hydration}%")
    print(f"🎒 Inventory: {', '.join(inventory) if inventory else 'Empty'}")
    print("="*40 + "\n")




def start_game():
    print("===============================================")
    print("        WELCOME TO WILDERNESS SURVIVAL         ")
    print("===============================================")
    type_text("You wake up alone in a dense forest, with no memory of how you got there")
    type_text("All you know is that you need to survive")
    type_text("The sun is setting and the temperature is dropping.\n")

    #Health and Stuff
    health = 100
    hydration = 100
    inventory = []

    display_status(health, hydration, inventory)
    first_choice(health, hydration, inventory)

def first_choice(health, hydration, inventory):
    print("---THE CRASH SITE---")
    type_text("What is your first move?")
    print("1. Stay with the plane wreckage and build a signal fire.")
    print("2. Head into the woods and search for water")
    choice = input ("\nEnter 1 or 2:").strip()

    if choice == "1":
        signal_fire_path(health, hydration, inventory)
    elif choice == "2":
        woods_path(health, hydration, inventory)

    else:
        print("Invalid choice. The panic sets in. Try again.")   
        first_choice(health, hydration, inventory)

def signal_fire_path(health, hydration, inventory):
    print("\n------------------------------------------------------")
    type_text("You gather dry brush and metal scrapd from the plane")
    type_text("A spark catches! You successfully build a bright signal fire.")
    type_text("You also scavenge a [Pocket Knife] from the cockpit.")
   

    inventory.append("Pocket Knife")
    print(f"\nInventory updated: {inventory}")

    #Transition to next scene
    type_text("\nAs you warm yourself, you hear a deep growl from the shadows...")
    end_game(success=False)

def woods_path(health, hydration, inventory):
    print("\n--------------------------------------------------------------")
    type_text("You stumble blindly through the thick brush into the dark.")
    type_text("You trip over a hidden root and fall down an embankment")

    health -= 30
    hydration -= 20
    print(f"Health decreased by 30! Current Health: {health}%")
    print(f"Hydration decreased by 20! Current Hydration: {hydration}%")

    if health <= 0:
        end_game(success=False)
    else:
        type_text("\nYou are bruised, but you hear the faint sound of rushing water nearby.")
        end_game(success=True)

def end_game(success):
    print("\n=========================================================")
    if success:
        print("CONGRATULATIONS! You survived the first night.")
    else:
        print("GAME OVER: The wilderness has claimed yet another soul.")
    print("===========================================================")

if __name__ == "__main__":
    start_game()