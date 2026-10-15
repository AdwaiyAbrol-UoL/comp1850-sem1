# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog', 'cat', 'hamster', 'goldfish']

not_fish = []
for item in animals:
    if item != 'goldfish':
        not_fish.append(item)

print(not_fish)

# I made not_fish into a for loop sequence from the list comprehension that was previously given. 