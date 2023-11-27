class Book:
    def __init__(self, name):
        self.name = name

learning_python = Book("Learning Python in 100 Steps")
print(learning_python.name)

class Planet:
    def __init__(self,name = "Earth"):
        self.name = name

planet1 = Planet()

print(planet1.name)

planet2 = Planet("Jupiter")

print(planet2.name)
