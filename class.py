import math
from functions import square
class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def scale(self, scale_factor):
        return Triangle(self.a*scale_factor, self.b*scale_factor, self.c*scale_factor)
    def is_valid(self):
        
        if ((self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c> self.a)):
            return True
        return False
    def is_right(self):
        max = self.a
        if (self.b > max):
            max = self.b
        elif (self.c > max):
            max = self.c
        if (max == self.a and square(max) == square(self.b) + square(self.c)):
            return True
        elif (max == self.b and square(max) == square(self.a) + square(self.c)):
            return True
        elif(max == self.c and square(max) == square(self.a) + square(self.b)):
            return True
        return False


