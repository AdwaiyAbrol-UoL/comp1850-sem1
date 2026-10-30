# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    def __init__(self, name, birth):
        """
        Creates a Person, given values for name and date of birth.
        """
        
        # type and valuechecking
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(birth, date):
            raise TypeError("Date of birth must be a date.")
        if name == "":
            raise ValueError("Name cannot be blank.")
        self.name = name
        self.birth = birth

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """
        Returns the uppercase initials of the person.
        """
        initials = ""
        for part in self.name.split():
            initials += part[0].upper()
        return initials.upper() 

    
    def is_birthday(self):
        """
        Returns True if today is the person's birthday, False otherwise.
        """
        d = date.today()
        if d.day == self.birth.day and d.month == self.birth.month:
            return True
        else:
            return False
