import random

# Get user to input how many random numbers they want
count = int(input("How many random numbers do you want? "))

if count < 0:
    print("Please enter a non-negative integer.")
    exit()
# Generate this many random numbers
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as outfile:
    for i in range(count):
        num = random.randint(1, 100)
        outfile.write(str(num) + "\n")
