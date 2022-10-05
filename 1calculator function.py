
#author - kasinath jayaprakash
#achievement task - 1
#this is a geometry calculator
#this tool is used for finding the area and perimeter of three different shapes

while True:
    #asking the user, which shape he would like to chose
    print("1.calculate the area of rectangle")
    print("2.calculate the area of the triangle")
    print("3.calculate the area of the circle")
    print("4.quit")
    shape_1 = int(input("enter your choice.\n"))
    
    #if user choses 1 
    if shape_1 == 1:
        #ask the user, the length and breadth of the rectangle
        length = int(input("enter the length of the rectangle in cm.\n"))
        breadth = int(input("enter the breadth of the rectangle in cm.\n"))
        #calculating the area and perimeter of the rectangle
        rectangle_area = length * breadth 
        rectangle_perimeter = 2 * (length + breadth)
        #fimal result, area and perimeter of the triangle
        print("the area of the recatngle is " , rectangle_area , "cm")
        print("the permimeter of the rectangle is" , rectangle_perimeter , "cm")
    
    
    #if user choses 2
    elif shape_1 == 2:
        #ask the user, the height, breadth, length1, and length 2
        height = int(input("enter the height of the triangle in cm.\n"))
        breadth = int(input("enter the breadth of the triangle in cm.\n"))
        length_1 = int(input("enter the length 1 of the triangle in cm.\n"))
        length_2 = int(input("enter the length 2 of the trianglr in cm.\n"))
        #calculating area and perimeter of the triangle
        triangle_area = 0.5 * height * breadth
        triangle_perimeter = breadth + length_1 + length_2
        #final result - area and perimeter of the triangle
        print("the area of the triangle is " , triangle_area , "cm ")
        print("the perimeter of the triangle is" , triangle_perimeter , "cm" ) 
    
    #if user choses 3
    elif shape_1 == 3:
        #ask the user
        radius = int(input("enter the radius of the circle in cm.\n"))
        #calculating the area and perimeter of the circle
        circle_area = 3.14 * radius * radius
        circle_perimeter = 2 * 3.14 * radius
        #final result, area and perimeter of the circle
        print("the area of the circle is" , circle_area , "cm")
        print("the perimeter of the circle is " , circle_perimeter , "cm")
    
    #if user choses 4
    elif shape_1 == 4:
        #if the user wants to quit doing the calculation
        print("thank you")
    
    #if user choses an option other than the 4 options, which is given
    else:
        print("invalid option")
        
    break
