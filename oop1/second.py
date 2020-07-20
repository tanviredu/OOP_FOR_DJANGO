import math 

class Circle():
    def __init__(self,redius):
        self.redius = redius


    def area(self):
        return math.pi * (self.redius **2)


    def perimeter(self):
        return 2*math.pi * self.redius



r = int(input("Enter the readius\n>"));
obj = Circle(r)
print("AREA      : {}".format(obj.area()))
print("PERIMETER : {}".format(obj.perimeter()))
