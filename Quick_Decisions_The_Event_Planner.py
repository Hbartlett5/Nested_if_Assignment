# Question 2: Quick Decisions: The Event Planner

# Task 1: Code Correction

attendees = input("Enter number of attendees: ")
attendees = int(attendees)
venue = "large hall" 
print(venue) if attendees > 100 else print("conference room")

# Task 2: Venue Selection

attendees = input("Enter number of attendees: ")
attendees = int(attendees)
venue = "large hall"

if attendees > 100:
    if attendees > 200:
        print(venue + ", audio system, and projector")
    elif attendees > 150:
        print(venue + ", and audio system")
    else:
        print(venue)
else:
    if attendees == 100:
        print("conference room, audio system, and projector")
    elif attendees > 75:
        print("conference room, and audio system")
    else:
        print("conference room")

# Task 3: Catering Choices

catering_options = input("vegetarian or non-vegetarian?")

print("We recommend Veggie Delight Caterers!") if catering_options == "vegetarian" else print("We recommend Gourmet Meals Caterers!")