#author - kasinath jayaprakash
#task - 8

#function for converting the temperature according to the users input.
def Temperatureconversion(degree, temperatureunit):
    
    # raising an error if the temperature unit is not correct.
    if temperatureunit not in ['c', 'f']:
        raise ValueError('enter a valid unit')
        
    # raising an error if the degree is not correct
    try:
        degree = float(degree)
    except ValueError:
        raise ValueError('enter a valid degree for the temperature')
     #if the unit is c   
    if temperatureunit == 'c': 
        #converting celsius to fahrenheit
        temperature = ((9 * degree) / 5 + 32) 
     
     #if the unit is f 
    elif temperatureunit == 'f': 
        #converting fahrenheit to celsius
        temperature = ((degree - 32) * 5 / 9) 
     
     #returns the value of the temperature 
    return temperature 

#function for converting the speed according to the users input.
def speedconversion(speedvalue, speedunit):
    
    #raising an error if the unit of the speed is not correct.
    if speedunit not in ['kph', 'mph']:
        raise ValueError('enter a valid unit')
        
    #raising an error if the value of the speed is not correct
    try:
        speedvalue = float(speedvalue)
    except ValueError:
        raise ValueError('enter a valid value for the speed')
    
    #if the unit is kph
    if speedunit == 'kph': 
        #converting kph to mph
        speed = 0.6214 * speedvalue 
    
    #if the unit is mph
    elif speedunit == 'mph': 
        #converting mph to kph
        speed = speedvalue * 1.60934; 
    
    #returns the value of the temperature  
    return speed 

#main Function to get inputs and pass inputs to function
def main():
    
    # Iterating till a valid choice is supplied
    while True:
        
        try:
            
            
            # if the input is not integer, a eroor will be raised
            choice = int(input("what would you like to convert -\nEnter 1 for Temperature or 2 for Speed : "))
            
            # Checking if choice is 1 or 2
            if 1 <= choice <= 2:
                break
            else:
                print("Error: Enter either 1 or 2")
        
        # error
        except ValueError:
            print("enter a valid value")
            
    if choice == 1:
        
        while True:
            valueTemp = (input("\nenter the value of the temperature : "))
            unitTemp = input(" which unit you would like to convert (C or F) : ")
            #converting to small case letters
            unitTemp = unitTemp.strip().lower()
        
            try:    
                print("Temperature after conversion is : {:.2f}".format(Temperatureconversion(valueTemp, unitTemp)))
            
            except ValueError as error:
                print(error)
                continue
            break
                    
    elif choice == 2:
        
        # Iterating till valid speed and unit values are supplied
        while True:
            valueSpeed = (input("\nenter the value of the speed : "))
            unitSpeed = input(" which unit would you like to convert (KPH or MPH) : ")
            #converting to smaller case letters
            unitSpeed = unitSpeed.strip().lower()
            
            try:
                
                print("Speed after conversion is : {:.2f}".format(speedconversion(valueSpeed, unitSpeed)))
            
            
            except ValueError as error:
                print(error)
                continue
            
            break
                
            

#calling the function
main()