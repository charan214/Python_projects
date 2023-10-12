import math
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
        print(f"Area of the rectangle {self.length}*{self.breadth}={self.length*self.breadth}")

class Circle(Rectangle):
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        print(f"Area of the Circle {self.radius**2}*{math.pi}={self.radius**2*math.pi}")
def find(x):
    x.Area()
def main():
    x=int(input("Length:"))
    y=int(input("Breadth:"))
    z=int(input("Radius:"))
    rect_obj=Rectangle(x,y)
    cir_obj=Circle(z)
    for i in [rect_obj,cir_obj]:
        find(i)
if __name__=="__main__":
    main()
        


