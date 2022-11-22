#author - kasinath jayaprakash
#task 10


#defining the properties of rectangle
class Rectangle:
    # defining constructor
    def _init_(self, height, width):
        self.height = height
        self.width = width
    
    #perimeter calculatoir
    def calculatePerimeter(self):
        return 2*(self.height + self.width)
    #area calculator
    def calculateArea(self):
        return self.height * self.width
        
    def displayInfo(self):
        
        print("height :", self.height)
        print("width :", self.width)
        print("Perimeter : ",self.calculatePerimeter())
        print("Area :", self.calculateArea())

def main():
    height = int(input("Enter height : "))       
    width = int(input("Enter width : "))
    r = Rectangle(height,width)
    r.displayInfo()
  
    
main()