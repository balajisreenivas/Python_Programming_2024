class Square:
    def __init__(self, side):
        self.side = side

    # TODO: Initialize side with the passed value

    def calculate_area(self):
        if(self.side <= 0):
            return -1

        else:
            return self.side * self.side

    # TODO: Calculate and return the area of the square

    def calculate_perimeter(self):
        if (self.side <= 0):
            return -1
        else:
            return 4 * self.side
    # TODO: Calculate and return the perimeter of the square

square = Square(5)
print(square.calculate_area())  # Output: 25
print(square.calculate_perimeter())  # Output: 20

# Example 2
square_with_zero_side = Square(0)
print(square_with_zero_side.calculate_area())  # Output: -1
print(square_with_zero_side.calculate_perimeter())  # Output: -1

# Example 3
square_with_non_positive_side = Square(-5)
print(square_with_non_positive_side.calculate_area())  # Output: -1
print(square_with_non_positive_side.calculate_perimeter())  # Output: -1