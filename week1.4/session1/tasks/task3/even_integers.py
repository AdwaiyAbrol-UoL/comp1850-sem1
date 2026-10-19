# function implementation

def even_integers_list(limit):
    result = []
    for number in range(0, limit, 2):
        result.append(number)
    return result

# testing the function

print(f"Even numbers up to 25: {even_integers_list(25)}")