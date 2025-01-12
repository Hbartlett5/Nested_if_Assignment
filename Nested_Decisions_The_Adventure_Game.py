# Question 1: Nested Decisions: The Adventure Game

# Task 1: Code Correction
#place = input("Choose a place: forest or cave? ")

#if place == "forest":
    #action = input("climb a tree or cross a river?")
    #if action == "climb a tree":
        #print("You found a bird's nest!")
    #elif action == "cross a river":
        #print("You found a boat!")
#elif place == "cave":
    #print("You find a hidden treasure!")

# Task 2: Setting the Scene

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found hidden treasure!")
    elif action == "proceed in the dark":
        print("You couldn't find anything and left.")

# Task 3: Default Path

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found hidden treasure!")
    elif action == "proceed in the dark":
        print("You couldn't find anything and left.")
    else:
        pass
else:
    pass