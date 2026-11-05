# Week 1.3, Session 2: Write User Information to a File


# Prompt the user for their name, age, and favorite colour.
name = input("Please enter your name:")
age = input("Please enter your age:")
favorite_color = input("Please enter your favorite color:")

# Open a file called 'user_info.txt' for writing
with open('user_info.txt', 'w') as f:

# Write each piece of information to the file, each on a new line.
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"Favorite Color: {favorite_color}\n")

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
