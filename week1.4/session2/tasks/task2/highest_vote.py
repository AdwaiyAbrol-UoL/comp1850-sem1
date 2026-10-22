# Week 4, Session 2: Task 2

def most_frequent_string(votes):
    """
    This function identifies the string that appears most frequently
    (highest count) in the votes argument and returns it along with the count
    of its occurrences. It assumes there is a single most frequent string
    (i.e., no ties for the highest count)

    Args:
        votes (list): A list of strings representng votes,
        e.g. ['apples', 'bananas', 'grapes', 'tomatoes']

    Returns:
        - tuple: (str, int) where str is the string with the highest count,
        and int is the count of its occurences
        - None, None: if votes is empty.
    """

    if len(votes) == 0:
        return None, None

    # Store how many times each string appears.
    counts = {}
    for vote in votes:
        if vote in counts:
            counts[vote] = counts[vote] + 1
        else:
            counts[vote] = 1

    # Find the string with the largest count.
    most_frequent = None
    highest_count = 0
    for vote in counts:
        if counts[vote] > highest_count:
            most_frequent = vote
            highest_count = counts[vote]

    return most_frequent, highest_count


fruit = ['date', 'apple', 'cherry', 'date', 'apple', 'apple', 'elderberry',
         'date', 'elderberry', 'elderberry', 'date', 'banana']


# Check if correct output is produced
print(most_frequent_string(fruit))          # ('date', 4)

# If completed, you could update the function to return all items that tie for the
# highest count in a list, e.g  (['apples', 'bananas'], 9). If there is no
# tie, return a single string and a value as usual, e.g ('apples, 9).
