class Triangle:
    def triangle(self):
        print("I am a triangle")

class Righttriangle():
    def righttriangle(self):
        print("In an Right angle triangle")

class Isosceles(Triangle,Righttriangle):  # Inheriting from Triangle and Righttriangle
    def isosceles(self):
        print("I am an isosceles triangle")


a = Isosceles()

a.isosceles()
a.righttriangle()
a.triangle()
