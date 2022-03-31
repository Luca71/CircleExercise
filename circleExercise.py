from math import pi, pow

class Circle:

    def __init__(self, radius = None, diameter = None):
        self._radius = radius if radius is not None else diameter * 0.5
        self._diameter = diameter if diameter is not None else radius * 2;
        self.circle_area()
    
    def circle_area(self):
        self._area = pi * pow(self._radius, 2)
        return self._area

    def __str__(self):
        return f"This is a Circle:\nRadius: {self._radius}\nDiameter: {self._diameter}\nArea: {self._area}\n"

    def __add__(self, other):
        return Circle(self._radius + other._radius)
    
    def __gt__(self, other):
        return self._radius > other._radius

    def __eq__(self, other):
        return self._radius == other._radius
    
    def sort(self):
        return self._radius

