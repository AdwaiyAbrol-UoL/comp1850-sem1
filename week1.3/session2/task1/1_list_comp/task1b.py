# Week 1.3, Session 1: Task 6b

values = [1, 4, 2, 6, 3, 7]

print(values)

newval = [2 * i if i % 2 == 0 else i for i in values]

print(newval)

# I made newval into a list comprehension sequence from the for loop that was previously given.