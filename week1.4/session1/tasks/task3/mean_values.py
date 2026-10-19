# function implementation

def mean_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# testing the function

print(f"Mean is {mean_average([3,9,15,27,30])}")
