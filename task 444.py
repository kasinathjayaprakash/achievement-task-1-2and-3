#author - kasinath jayaprakash
#task - 4

#function for the formula
def temp_Conversion(degree, Unit_of_temp):
    #cross checks whether the unit is correct
    if Unit_of_temp == 'c':  
        #formula for converting celsius to fahreheit 
        convertedTemp = ((9 * degree) / 5 + 32) 
    #cross checks whether the unit is correct
    elif Unit_of_temp == 'f': 
        #formula for converting fahrenheit to celsius
        convertedTemp = ((degree - 32) * 5 / 9)  
       #returns the value 
    return convertedTemp  

#function for the formula
def speed_Conversion(speed, Unit_of_speed):
    #cross checks whether the unit is correct
    if Unit_of_speed == 'kph': 
        #formula for converting kmp to mph 
        convertedSpeed = 0.6214 * speed  
    #cross checks whether the unit is correct
    elif Unit_of_speed== 'mph': 
        #formula for converting mph to kph
        convertedSpeed = speed * 1.60934;   
        #returns the value
    return convertedSpeed  



#function for defining the input of the user using the above defined formulas
def main():
    #asks the user which conversion would the user like to chose
    print("1.temperature")
    print("2. speed")
    conversion = int(input("What do you want to convert: \n"))
    #if the user selects temperature
    if conversion == 1:
        #asks the user to input the temperature
        Temperature1 = float(input("Enter the temperature you want to convert :\n "))
        #ask the user to enter the unit for the temperature
        Unit = input("Enter the unit for the temperature :\n ")
        #if the user types the unit in capital letter, the below function converts it inot small letters.
        Unit = Unit.strip().lower() 
        # this command uses the above defined temp conversion formula to convert the temperature 
        print("the Converted temperature is : {:.2f}".format(temp_Conversion(Temperature1, Unit)))
    #if the user selects speed    
    elif conversion == 2:   
        #asks the user to input the speed 
        Speed1 = float(input("\nEnter the speed you want to convert :\n"))
        #asks the user to enter the unit for speed
        Unit = input("Enter the  unit for the speed :\n ")
        #if the user types the unit in capital letter, the below function converts it inot small letters.
        Unit = Unit.strip().lower()  
        #this command uses the above defined speed conversion formula to convert the speed.
        print("the Converted speed is : {:.3f}".format(speed_Conversion(Speed1, Unit)))
    #the program will be invalid if the user enters any other choice   
    else:
        print("enter valid input")

main()