# Week 1.5, Session 2: Task 3

class Money:
    """
    An amount of money, in British Pounds Sterling.
    """

    def __init__(self, pounds, pence):
        """
        Creates a Money object, given the number of pounds and pence.
        """
        if type(pounds) is not int:
            raise TypeError("Pounds must be an integer.")
        if type(pence) is not int:
            raise TypeError("Pence must be an integer.")
        if pounds < 0:
            raise ValueError("Pounds cannot be negative.")
        if pence < 0 or pence > 99:
            raise ValueError("Pence must be between 0 and 99.")

        self.pounds = pounds
        self.pence = pence

    def __str__(self):
        """
        Returns a string representation of this Money.
        """
        return f"£{self.pounds}.{self.pence:02d}"

    def __add__(self, other):
        """
        Adds this Money to another Money, returning the total.
        """
        if not isinstance(other, Money):
            raise TypeError("You can only add another Money object.")

        total_pence = self.pence + other.pence
        total_pounds = self.pounds + other.pounds + (total_pence // 100)
        total_pence = total_pence % 100

        return Money(total_pounds, total_pence)
