#!/usr/bin/env python
# basic_classes.py

class Circle():
    def __init__(self,color,radius):
        self.color = color
        self.radius = radius
    


    def diameter(self):
        return self.radius*2

    def circumfrence(self):
        return self.radius*2*3.14
    
    def isRed(self):
        return self.color == 'red'



quan = Circle('red',10)
print(quan.isRed())
print(quan.diameter())
print(quan.circumfrence())
quan = Circle('green',50)
print(quan.isRed())
print(quan.diameter())
print(quan.circumfrence())





class GraduateStudent():
    def __init__(self, first_name, last_name, year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major


    def year_matriculted(self):
        return 2020-self.year
me = GraduateStudent('ruihan','wang',2,'Bioinformatics')
print(me.year_matriculted())

