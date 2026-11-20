import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
num_to_choose = int(input("How many names do you want to choose? "))

if num_to_choose < 0:
    print("Please enter a non-negative integer.")
    exit()
elif num_to_choose > len(names):
    print("Please enter a number less than or equal to the total number of names.")
    exit()

chosen_names = random.sample(names, num_to_choose)
# Display the chosen names, one per line
for name in chosen_names:
    print((name) + "\n")
