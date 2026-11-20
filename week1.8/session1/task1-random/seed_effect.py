# See README.md for instructions on what to do this program

import random

random.seed(10)

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print(num1, num2, num3)

# tried random.seed(39).
# if you set a seed, the sequence of random numbers is predictable and reproducible, which is good for testing and debugging. However, if you don't use a seed, you will get different random numbers each time you run the program. 