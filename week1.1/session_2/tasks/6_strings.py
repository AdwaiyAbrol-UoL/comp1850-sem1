# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
# prints the original string entered by the user
print(f"Modified String 1: {user_string.lower()}")
# prints the string in all lowercase letters
print(f"Modified String 2: {user_string.upper()}")
# prints the string in all uppercase letters
print(f"Modified String 3: {user_string.strip()}")
# prints the string with leading and trailing spaces removed
print(f"Modified String 4: {user_string.replace('a', '@')}")
# prints the string with all occurrences of 'a' replaced by '@'
print(f"Modified String 5: {user_string.capitalize()}")
# prints the string with the first character capitalized and the rest lowercase
print(f"Modified String 6: {user_string[::-1]}")
# prints the string in reverse order
print(f"Modified String 7: {user_string.title()}")
# prints the string with the first character of each word capitalized
print(f"Modified String 8: {len(user_string)}")
# prints the length of the string
print(f"Modified String 9: {user_string.find('a')}")
# prints the index of the first occurrence of 'a' in the string, or -1 if not found
print(f"Modified String 10: {user_string.count('a')}")
# prints the number of occurrences of 'a' in the string
print(f"Modified String 11: {user_string.startswith('Hello')}")
# prints True if the string starts with 'Hello', otherwise False
print(f"Modified String 12: {user_string.endswith('!')}")
# prints True if the string ends with '!', otherwise False
print(f"Modified String 13: {user_string.isalnum()}")
# prints True if the string contains only alphanumeric characters, otherwise False
print(f"Modified String 14: {user_string.isalpha()}")
# prints True if the string contains only alphabetic characters, otherwise False
print(f"Modified String 15: {user_string.isdigit()}")
# prints True if the string contains only numeric characters, otherwise False



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!