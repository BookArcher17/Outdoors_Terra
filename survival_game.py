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
    animal_encounter(health, hydration, inventory)

def animal_encounter(health, hydration, inventory):
    display_status(health, hydration, inventory)
    type_text("A pair of glowing eyes stares at you from the brush.")
    type_text("As you watch, a wolf emerges from the shadows, snarling fiercely")
    print("1. Stand your groud and fight.")
    print("2. Turn and run.")

    choice = input("\nEnter 1 or 2: ").strip()

    if choice == "1":
        if "Pocket Knife" in inventory:
            type_text("As the wolf approaches, you grab your pocket knife. It lunges at you and you stab at it.")
            type_text("The wolf gouges your arm, but as you stab it, it yelps and runs away")

            health -= 40
            print(f"Health decreased by 40! Current health: {health}%")

        else:
            type_text("\nYou have nothing to defend yourself with. The wolf attacks!")
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
        type_text("You drink eagerly.")
        hydration += 20
        print(f"Hydration increased by 20! Current Hydration: {hydration}%")
        type_text("After you have drank your fill, you must decide what to do next.")
        print("1. Go back to the plane to see if you can salvage anything from the wreck.")
        print("2. Search for a cave to spend the night in.")
        print("3. Stay by the water for the night")

        choice = input("\nEnter 1, 2 or 3:").strip()
        if choice == "1":
           type_text("You carefully climb back up the embankment and make your way back to the plane.")
           return_to_plane_path(health, hydration, inventory) 

        elif choice == "2":
            type_text("You decide to head upstream in search of a cave to sleep in")
            find_a_cave_path(health, hydration, inventory)

        elif choice == "3":
            type_text("You decide to spend the night by the river")

        else:
            type_text("You panic.")

def return_to_plane_path(health, hydration, inventory):
    print("-----------------------------------------------------------------")
    type_text("Upon reaching the plane, you realise how late it is. Do you decide to take stock now or wait until morning?")

#DO THE OPTIONS HERE!!!!


def find_a_cave_path(health, hydration, inventory):
    print("----------------------------------------------------------------------")
    type_text("After walking for a while, you stumble across a cave opening at ground level.")
    type_text("What do you want to do?")
    print("1. Sleep here")
    print("2. Search for a cave higher up away from the water")
    print("3. Decide that this was a bad idea and return to the plane")

    choice = input("\nEnter 1, 2 or 3")
    if choice == "1":
        type_text("You decide to sleep in this cave")
        lower_cave_path(health, hydration, inventory)

    elif choice == "2":
        type_text("Deciding that the risk of running into predators is too high, you continue searching.")

    elif choice =="3":
        type_text("You decide to return to the plane")
        return_to_plane_path(health, hydration, inventory)

def lower_cave_path(health, hydration, inventory):
    print("---------------------------------------------------------------")
    type_text("You enter the cave, and a wave of exhaustion washes over you. It's been a long day.")
    type_text("You curl up on the floor against one of the walls and fall into a deep sleep.")
    
        
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