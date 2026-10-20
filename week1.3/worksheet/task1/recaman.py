# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]
for x in range(1,L):
    previous_value = sequence[x-1]
    next_value = previous_value - x
    if next_value > 0 and next_value not in sequence:
        sequence.append(next_value)
    else:
        sequence.append(previous_value + x)

# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence