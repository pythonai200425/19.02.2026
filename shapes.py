import math

from typing_extensions import override
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_hekef(self):
        pass

    @override
    def __str__(self):
        return f"name: {self.name}"

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__('Triangle')
        self.a = a
        self.b = b
        self.c = c

    @override
    def get_hekef(self):
        return self.a + self.b + self.c

    @override
    def __str__(self):
        return f"{super().__str__()}, a: {self.a}, b: {self.b}, c: {self.c} hekef: {self.get_hekef()}"

class TriangeEqualSides(Triangle):
    def __init__(self, a, c):
        super().__init__(a, a, c)
        self.name += ' Equal Sides'

    @override
    def get_hekef(self):
        return self.a * 2 + self.c


class TriangleEquilateral(TriangeEqualSides):
    def __init__(self, a):
        super().__init__(a, a, a)
        self.name += ' Equilateral'

    @override
    def get_hekef(self):
        return self.a * 3

class FourSides(Shape):
    def __init__(self, a, b, c, d):
        super().__init__('4 sides')
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    @abstractmethod
    def get_area(self):
        pass

    @override
    def get_hekef(self):
        return self.a + self.b + self.c + self.d

class Rectangle(FourSides):  # malben
    def __init__(self, width, height):
        super().__init__(width, height, width, height)
        self.name += ' rectangle'

    @override
    def get_hekef(self):
        return 2 * (self.a + self.b)


class Square(Rectangle):  # ribua
    def __init__(self, a):
        super().__init__(a, a, a, a)
        self.name += ' square'

    @override
    def get_hekef(self):
        return 4 * self.a

class Circle(Shape):
    def __init__(self, r):
        super().__init__('Circle')
        self.r = r

    @override
    def get_hekef(self):
        return 2 * math.pi * self.r

    @override
    def __str__(self):
        return f"{super().__str__()}, r: {self.r} hekef: {self.get_hekef()}"

tr1 = Triangle(7, 7, 8)
print(tr1)
circle1 = Circle(8.77)
print(circle1)

circle1.get_koter = lambda x : x*2
del circle1.get_koter

TriangeEqualSides(3, 2)