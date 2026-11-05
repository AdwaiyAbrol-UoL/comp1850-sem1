# Week 1.3, Session 1: Task 4a

sum = 0

for k in range(1,10):
    sum = sum + k ** 2

print(sum)


# modify the code to sum the squares of even numbers up to and including 20
square_sum = 0
for k in range(1,21):
    if k % 2 == 0:
        square_sum += k ** 2
        print(f"The square of {k} is {k ** 2}, current sum is {square_sum}")

# modify the code to print the sum at each iteration