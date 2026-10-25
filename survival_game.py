from secrets import choice
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
    if health <=0:
     end_game(success=False)
    if hydration <=0:
     end_game(success=False)
    if health >=100:
        health = 100
    if hydration >=100:
        hydration = 100

def start_game():
    print("===============================================")
    print("        WELCOME TO WILDERNESS SURVIVAL         ")
    print("===============================================")
    type_text("You wake up in the cockpit of a plane. The pilot is dead. You are in the middle of the forest.")
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
    type_text("You gather dry brush and metal scrapped from the plane")
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
            river_sleep_path(health, hydration, inventory)

        else:
            type_text("You panic.")
            woods_path(health, hydration, inventory)

def return_to_plane_path(health, hydration, inventory):
    print("-----------------------------------------------------------------")
    type_text("Upon reaching the plane, you realise how late it is. Do you decide to take stock now or wait until morning?")
    print("1. Take stock now")
    print("2. Wait until morning")

    choice = input("\nEnter 1 or 2: ").strip()
    if choice == "1":
        type_text("You decide to take stock of your supplies.")
        type_text("You find a few useful items, including a first aid kit and some food rations.")
        inventory.append("First Aid Kit")
        inventory.append("Food Rations")
        print(f"\nInventory updated: {inventory}")


    elif choice == "2":
        type_text("You decide to wait until morning.")
        type_text("You curl up under the wing of the plane and try to get some rest, eventually falling into a fitful sleep.")
        type_text("You wake up to the sound of birds chirping and the sun rising. You feel a sense of relief, having survived the night.")
        type_text("You now decide to take stock of the plane")
        type_text("You find a few useful items, including a first aid kit and some food rations.")
        inventory.append("First Aid Kit")
        inventory.append("Food Rations")
        print(f"\nInventory updated: {inventory}")
    
    else:
        type_text("You hesitate.")
        return_to_plane_path(health, hydration, inventory)

def find_a_cave_path(health, hydration, inventory):
    print("----------------------------------------------------------------------")
    type_text("After walking for a while, you stumble across a cave opening at ground level.")
    type_text("What do you want to do?")
    print("1. Sleep here")
    print("2. Search for a cave higher up away from the water")
    print("3. Decide that this was a bad idea and return to the plane")

    choice = input("\nEnter 1, 2 or 3: ").strip()
    if choice == "1":
        type_text("You decide to sleep in this cave")
        lower_cave_path(health, hydration, inventory)

    elif choice == "2":
        type_text("Deciding that the risk of running into predators is too high, you continue searching.")

    elif choice =="3":
        type_text("You decide to return to the plane")
        return_to_plane_path(health, hydration, inventory)
    else:
        ("Your indecision is clear")
        find_a_cave_path(health, hydration, inventory)

def lower_cave_path(health, hydration, inventory):
    print("---------------------------------------------------------------")
    type_text("You enter the cave, and a wave of exhaustion washes over you. It's been a long day.")
    type_text("You curl up on the floor against one of the walls and fall into a deep sleep.")
    type_text("As you doze off, you wonder if you will ever make it home. Rain starts to fall outside, and you hear the sound of water dripping from the cave ceiling.")
    flooding_cave_path(health, hydration, inventory)

def flooding_cave_path(health, hydration, inventory):
    print("---------------------------------------------------------------")
    type_text("You wake up to the sound of rushing water. The cave is flooding rapidly, and you are trapped inside.")
    type_text("You can either swim for the entrance or try to find a higher point in the cave to wait out the flood.")
    print("1. Swim for the entrance.")
    print("2. Try to find a higher point in the cave.") 

    choice = input("\nEnter 1 or 2:").strip()
    if choice == "1":
        type_text("You decide to swim for the entrance, but the current is too strong. You are swept away and drown.")
        end_game(success=False)
    elif choice == "2":
        type_text("You decide to find a higher point in the cave. You manage to climb onto a ledge and wait out the flood.")
        type_text("After a while, the water recedes, and you are able to make your way out of the cave.")
        type_text("You are cold and wet, but alive. You must now decide what to do next.")
        print("1. Head back to the plane to see if you can salvage anything from the wreck.")
        print("2. Head off in search of a food source.")

        choice = input("\nEnter 1 or 2:").strip()
        if choice == "1":
            type_text("You decide to head back to the plane.")
            return_to_plane_path_morning(health, hydration, inventory)

        elif choice == "2":
            type_text("You decide to head off in search of a food source.")
            search_for_food_path(health, hydration, inventory)

        else:
            type_text("You decide that instead of doing either of these things, you will wait here to die. You get your wish.")
            end_game(success=False)
    
def river_sleep_path(health, hydration, inventory):
    print("---------------------------------------------------------------")
    type_text("You decide to sleep by the river, hoping that the sound of the water will lull you to sleep.")
    type_text("As you drift off, you hear the rustling of leaves and the snapping of twigs. Something is approaching.")
    type_text("You wake up to find a brown bear staring at you. It looks hungry.")
    print("1. Try to scare the bear away.")
    print("2. Stay still and hope it goes away.")

    choice = input("\nEnter 1 or 2:")
    if choice == "1":
        type_text("You make yourself big and clap loudly at the bear. Instead of running away, it stares at you for a moment.")
        type_text("Suddenly, it lunges forward and swipes its claws along your stomach. You scream in pain and the bear leans over you. Everything goes black.")
        end_game(succes=False)

    elif choice == "2":
        print("-------------------------------------------------------")
        type_text("Deciding to stay still, you freeze as the bear sniffs you. After a long moment, it snorts and walks away.")
        night_after_river_path(health, hydration, inventory)

def night_after_river_path(health, hydration, inventory):
    print("-------------------------------------------------------")
    type_text("You wake up to the sound of birds chirping. The sun is rising and you feel a sense of relief. You survived the night by the river.")
    type_text("Congratulations! You have survived your first night in the wilderness.")
    type_text("Now you must decide what to do next.")
    print("1. Head back to the plane to see if you can salvage anything from the wreck.")
    print("2. Head off in search of a food source.")

    choice = input("\nEnter 1 or 2:").strip()
    if choice == "1":
        type_text("You decide to head back to the plane.")
        return_to_plane_path_morning(health, hydration, inventory)

    elif choice == "2":
        type_text("You decide to head off in search of a food source.")
        search_for_food_path(health, hydration, inventory)

    else:
        type_text("You hesitate, unsure of what to do next.")

def return_to_plane_path_morning(health, hydration, inventory):
    print("-------------------------------------------------------")
    type_text("You make your way back to the plane, hoping to find some useful supplies") 
    type_text("You find a few useful items, including a first aid kit and some food rations.")
    inventory.append("First Aid Kit")
    inventory.append("Food Rations")
    print(f"\nInventory updated: {inventory}")
    type_text("You decide you need to set up a base camp somewhere")
    type_text("Where do you want to go")
    print("1. Stay and set up near the plane")
    print("2. Head north")
    print("3. Head south")
    print("4. Head east")
    print("5. Head west")

    choice = input("\n Enter 1, 2, 3, 4 or 5")
    if choice == "1":
        type_text("You decide that rescuers have the best hope of locating you near the plane, so staying put is the best option")
        stay_at_plane_path(health, hydration, inventory)

    elif choice == "2":
        head_north_path(health, hydration, inventory)

    elif choice == "3":
        head_south_path(health, hydration, inventory)

    elif choice == "4":
        head_east_path(health, hydration, inventory)

    elif choice == "5":
        head_west_path(health, hydration, inventory)

    else:
        type_text("You decide dying out here doesn't sound so bad")
        end_game(success=False)

def head_north_path(health, hydration, inventory):
    type_text("You are drawn to the north, where you see mountains rising against the skyline. Perhaps you can build a life there.")
    type_text("The rescuers surely will see you from up there. Right?")
    type_text("You begin your long trek towards the mountain.")
    welcome_to_the_north_path(health, hydration, inventory)

def head_south_path(health, hydration, inventory):
    type_text("You are drawn south. South is downhill, where rivers go. If you follow the water, it will eventually lead to people. You hope.")
    type_text("Deciding there is no time like the present, you decide to get moving.")
    welcome_to_the_south_path(health, hydration, inventory)

def head_east_path(health, hydration, inventory):
    type_text("The eastern skyline, where the sun rises early in the morning calls to you. If you keep going far enough, you know the ocean is out there somewhere.")
    type_text("Maybe there, you will find salvation.")
    type_text("With one last glance at the plane that carried you here, you set off eastward.")
    welcome_to_the_east_path(health, hydration, inventory)

def head_west_path(health, hydration, inventory):
    type_text("The west calls to you. The sun sets there, casting its final rays. Perhaps there you will be happy.")
    type_text("You carefully begin to pick a path through the thick brush.")
    welcome_to_the_west_path(health, hydration, inventory)

def welcome_to_the_north_path(health, hydration, inventory):
    print("----------------------------------------------------------------------")
    type_text("After a long day of hiking, you are tired and sore.")

    health -= 10
    hydration -= 20
    print(f"Health decreased by 10! Current Health: {health}%")
    print(f"Hydration decreased by 20! Current Hydration: {hydration}%")
    
    if health <= 0:
        end_game(success=False)
    if hydration <= 0:
        end_game(success=False)
    type_text("Stopping to catch your breath, you turn back to see how far you've come.")
    type_text("You stare in awe at the landscape.")
    type_text("From your vantage point up on this mountain, you can see for miles. The little red plane that landed you in this situation is a small dot in the distance.")
    type_text("To the east, the ocean sparkles with the fading light. You cannot see any boats or traces of people there.")
    type_text("To the south, you catch glimpses of the river between trees as it winds downwards for as far as the eye can see.")
    type_text("To the west, you watch as the sun paints the sky a beautiful shade of gold, illuminating the treetops.")
    type_text("As you watch the sun fade, you decide to find a suitable place to sleep. Fortunately, there is a conveniently located bush next to you.")
    type_text("Morning arrives in scattered birdsong and glaring beams of light. You sit up, and that's when you notice the waterfall. It's far away enough that you cannot hear it, but it looks big.")
    type_text("The running water will undoubtedly be clean enough for you to drink, and where there's water there's food and life.")
    type_text("You spend a few hours hiking across the peaks until you reach the waterfall. It's beautiful")
    print("Would you like to set us base here?")
    choice = input("\nEnter 1 or 2")
    print("1. Yes 2. No")

    if choice == "1":
        type_text("Welcome to your new home")
        waterfall_home_path(health, hydration, inventory)

    elif choice == "2":
        type_text("You decide to continue searching for a better home.")

    else:
        type_text("You are indecisive, but decide to stay")
        waterfall_home_path(health, hydration, inventory)

def waterfall_home_path(health, hydration, inventory):
    print("-------------------------------------------------")
    type_text("Welcome to your new home!")

def welcome_to_the_south_path(health, hydration, inventory):
    print("----------------------------------------------------------------------")
    type_text("After tumbling and weaving your way down, you are ready for the day to be over.")
    
    health -= 10
    print(f"Health decreased by 10! Current Health: {health}%")
    type_text("You are glad that you followed the river, so you always had something to drink.")
    type_text("As the sun dips lower in the sky, you trudge on, searching for a suitable sleeping place.")
    type_text("Eventually, you find a bush that doesn't look too offensive and curl up in it.")
    
    if health <= 0:
        end_game(success=False)
    if hydration <= 0:
        end_game(success=False)

def welcome_to_the_east_path(health, hydration, inventory):
        print("----------------------------------------------------------------------")
        type_text("As the sun sets, you catch your first glimpse of the ocean in the distance, and finally realise how tired you are.")
    
        health -= 10
        hydration -= 20
        print(f"Health decreased by 10! Current Health: {health}%")
        print(f"Hydration decreased by 20! Current Hydration: {hydration}%")
        
        if health <= 0:
            end_game(success=False)
        if hydration <= 0:
            end_game(success=False)
        type_text("The plants here are starting to change, and you find a tree with low hanging branches.")
        type_text("You climb up and decide to belt yourself to a branch in a comfortable fork like you'd read about a girl doing in a book.")

def welcome_to_the_west_path(health, hydration, inventory):
        print("----------------------------------------------------------------------")
        type_text("After walking for hours, you are tired and sore.")
    
        health -= 10
        hydration -= 20
        print(f"Health decreased by 10! Current Health: {health}%")
        print(f"Hydration decreased by 20! Current Hydration: {hydration}%")
        
        if health <= 0:
            end_game(success=False)
        if hydration <= 0:
            end_game(success=False)
        type_text("Deciding that you have travelled far enough today, you find a tree with several exposed roots and curl up underneath one, hoping to catch a peaceful night's rest.")
        type_text("When the first rays of sun reach you in the morning, you continue walking. The brush is thick and difficult to pass through, but you endure it.")
        type_text("Eventually, you reach a ravine. You are about to despair when you see a rope bridge.")
        type_text("You are about to complain about how stereotypical it is, when you realise that it looks new")
        print("What do you want to do?")
        print("1. Throw yourself into the ravine and die.")
        print("2. Cross the bridge.")

        choice = input("\nEnter 1 or 2")

        if choice == "1":
            type_text("Welp. You throw yourself into the ravine.")
            end_game(success=False) 

        elif choice =="2":
            type_text("You do what any rational person would do in this situation and head to the bridge. As you cross, you realise that this can only mean one thing.")
            type_text("People have been here recently.")
            the_bridge_and_the_cabin_path(health, hydration, inventory)

        else:
            type_text("You try to decide what to do, but fate decides for you. You slip and plummet off the edge of the ravine.")
            end_game(success=False)
         
def the_bridge_and_the_cabin_path(health, hydration, inventory):
    type_text("After drawing the conslusion that people have been here recently, you hurry across the bridge. On the other side, you see a small clearing through the trees.")
    type_text("There, you discover a cabin.")
    print("Do you go inside or not?")
    print("1. Go inside")
    print("2. Decide it's too risky.")

    choice = input("\nEnter 1 or 2")

    if choice == "1":
        type_text("You decide to enter the cabin. Inside, you find a group of men playing cards. They are surprised to see you.")
        type_text("They tell you that they have been searching for you and the pilot since you didn't land on time.")
        type_text("You share the news about the pilot's passing, and describe where you landed.")

        end_game(success=True)

def search_for_food_path(health, hydration, inventory):
    print("-------------------------------------------------------")
    type_text("You venture into the forest, searching for any signs of edible plants or animals.")
    type_text("After a while, you come across a small clearing with some berry bushes and a few small animals scurrying about.")
    type_text("You recognise the berries and immediately begin picking them, filling your bag.")

    inventory.append("Berries")
    print(f"\nInventory updated: {inventory}")
    type_text("You then decide to return to the plane")
    return_to_plane_path_morning(health, hydration, inventory)

def stay_at_plane_path(health, hydration, inventory):
   type_text("Deciding that the best port of call is staying with the plane, which is probably traceable in some way, at least to your general area, you survey the area.")
   type_text("You've read the book Hatchet, where the main character ends up in a imilar situation.")
   type_text("You are torn between looking for food or creating a better shelter.")
   print("1. Gather food")
   print("2. Create a better shelter")

   choice = input("\nEnter 1 or 2")

   if choice == "1":
       type_text("You decide to go and gather food. There were some trees bearing fruit not too far down the river. It probably won't kill you. Probably.")
       type_text("You pick the fruit. Fortunately, you recognise it as safe. You snack as you work")
       if health <100:
           health +=20
           print("Health increased by 20! Health now {health}%!")
       type_text("After you have gathered the majority of the fruit, you decide to head back to the plane.")
       type_text("As you reach the plane, you become aware of the sound of engines in the distance.")
       rescue_plane_path(health, hydration, inventory)

   elif choice == "2":
       type_text("You set about gathering scrap metals from the plane and nearby branches. A few hours of hard work go by, and the end product is a small, ramshackle thing that resembles a box.")
       type_text("It's a hut. Duh.")
       type_text("Now that you have a shelter, you realise you are hungry.")
       if "Berries" in inventory:
           type_text("You pull out the berries you harvested earlier and snack on them.")
           type_text("The sound of engines distracts you from your peaceful meal.")
           rescue_plane_path(health, hydration, inventory)
       else:
           health -=10
           print("Health depleted by 10! Current health:{health}%!")
           type_text("As your stomach growls, you realise that you can also hear an engine.")
           rescue_plane_path(health, hydration, inventory)


   else:
       type_text("A wave of misery washes over you, and you no longer have any will to live. You drop a rock on your head.")
       end_game(success=False)
       
def rescue_plane_path(health, hydration, inventory):
       type_text("A small plane, barely larger than the one that landed you in this situation, circles overhead. They haven't yet spotted you, but it won't be long until they do.")
       type_text("You thank your lucky stars that you haven't been out here for too long and that this nightmare will finally end.")
       type_text("Eventually, they spot you and use a megaphone to let you know that rescuers will be here soon")
       end_game(success=True)   
   
def end_game(success):
    print("\n=========================================================")
    if success:
        print("CONGRATULATIONS! You have survived the wilderness.")
    else:
        print("GAME OVER: The wilderness has claimed yet another soul.")
    print("===========================================================")

if __name__ == "__main__":
    start_game()