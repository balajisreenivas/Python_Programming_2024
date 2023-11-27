class Book:
    def __init__(self,name,copies=0):
        self.name = name
        self.copies = copies

    def increase_copies(self,how_much):
        self.copies += how_much

    def decrease_copies(self,how_much):
        self.copies -= how_much

harry_potter=Book("Harry_Potter",5)
hardy_boys=Book("Hardy_Boys",10)

harry_potter.increase_copies(10)
hardy_boys.increase_copies(25)
harry_potter.decrease_copies(5)

print(harry_potter.name )
print(harry_potter.copies)
