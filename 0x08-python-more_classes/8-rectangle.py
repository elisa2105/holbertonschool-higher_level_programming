#!/usr/bin/python3
class Rectangle():
    '''Class that define a rectangle'''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for wigth"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width*2) + (self.__height*2)

    def __str__(self):
        """ print() __str__ method """
        rec = ""
        if self.__width == 0 or self.height == 0:
            return rec

        for i in range(self.__height):
            rec += (str(self.print_symbol) * self.__width + '\n')

        rec = rec.rstrip()
        return rec

    def __repr__(self):
        """Return class representation"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """method destructor"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
