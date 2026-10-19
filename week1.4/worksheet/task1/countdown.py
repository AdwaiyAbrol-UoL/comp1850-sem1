
def countdown(number): 
    '''  
    This recursive function takes a positive integer number  
    and counts the number down to zero printing each value. 
    ''' 

    print(number)
    if number <=0:
        return
    countdown(number-1)

# testing the function
countdown(11)