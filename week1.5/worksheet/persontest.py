from person import Person
from datetime import date

x = Person("Alan John Smith", date(1990, 8, 17))
print(x.initials()) # Should be AJS
print(x.is_birthday()) # Should be false unless today is Aug 17

person = Person("John Lawrence", date.today())
print(person.is_birthday()) # Should be true always, since we set the birthday to today