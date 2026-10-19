
def calculate_mean(lst_value): 
    """
    Calculates the average (mean) of a list of numbers.

    Args:
        lst_value: A list of numbers.

    Returns: 
       the total sum of the values divided by the number of values in the list; known as the mean or average. 
    """ 

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
    sum = sum + value 
    return sum/num_of_value 