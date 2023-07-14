import math
class Circle:
    def _init_(self,radius):
        self.radius=radius
    def area(self):
        area=math.pi *self.radius*self.radius
        return area
    def perimeter(self):
        perimeter=math.pi*self.radius
        return perimeter
    
    
getArea=Circle(5)
print (getArea.area())
getCircumference=Circle(9)
print (getCircumference.perimeter())