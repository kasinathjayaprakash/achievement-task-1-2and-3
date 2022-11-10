#author     - kasinath jayaprakash
#assignment - 1
#course     - PROG1783

def meal_price(price , quantity):
    return price * quantity


def assignment():
    #welcome message
    print("\n welcome to KJP food court")
    #asking the details of the customer
    customer_name = (input("enter your first and last name.\n"))
    #address
    address_line1 = (input("enter your street number and street name,unit #if applicable.\n "))
    city = (input("enter your city.\n"))
    food = ""
    province = (input("enter your province.\n"))
    postal_code = (input("enter your postal code.\n"))
    special_instruction = (input("special instructions for delivery from the address.\n"))
    phone_number = (input("enter your phone number.\n"))
    quantity  = 0
    total_price = 0
    choice = 0
    price = 0.0
    while True:
        #Displaying the menu
        print("menu:.\n (1). big mac meal .\n (2). poutine meal .\n")
        #asking the customer, which meal he would like to choose
        choice = int(input("enter your choice :.\n"))
        #quantity of the meal required
        quantity = int(input("enter the quantity of the meal:.\n"))
        #if the customer choses big mac meal
        if(choice == 1):
            print("the item you chose is a big mac meal , and the quantity is" , quantity)
            food = "big mac meal"
            price = 14.50
        #if the customer choses poutine meal
        else:
            print("the item you chose is a poutine meal , and the quantity is " , quantity)
            food = "poutine meal"
            price = 13.99
        #asking the customer whether he want to confirm with this order
        confirm = input("do you want to confirm your order : Y OR N :.\n")
        #if the customer continues with the order
        if(confirm == "Y" or confirm == "y"):
             total_price = meal_price(price , quantity)
        #if the customer doesnt want to continue with the order
        else:
            print("repeat the order once more.\n")
            break
        #discounts
        discount = 0.0
        #if the customer buys a product below 100 5% discount will be applied
        if total_price < 100:
            discount = total_price * 0.05
        #if the customer buys a product between 100 and 500 10% discount will be applied
        elif total_price > 100 and total_price < 500:
            discount = total_price * 0.10
        #if the customer buys a product above 500 15% discount will be applied
        else:
            discount = total_price * 0.15
        
        student_offer = 0.0
        while True:
            #asking the customer if he/she is a student for the student offer policy
            student = input("are you a student : Y or N :.\n") 
            #if the customer is a student 10% discount will be applied
            if (student == "Y" or  student == "y"):
                student_offer = (total_price * 0.10)
            # if the customer is not a student continue with the order without the student offer
            break
        while True:
            if total_price-discount-student_offer >30:
                  charge = 5
            else:
                 charge= 0
            break
        
        delivery = input("what would you like 1).deliver 2).pickup :\n")
        if delivery == 1:
            print("\n\n\n*************KJP food court*****************\n****************RECEIPT*************")
        print("deliver address :" , address_line1 )
        print("\t", city ,  province , postal_code)
        print()
        print("order          item amount        item price        total")
        print("-----          ------------       --------          ------")
        print(food, "        ", quantity, "           $" ,price, "          $", total_price - discount )
        if(student_offer !=0.0):
            print("\nstudent savings of 10%                             :$",student_offer)
            print("\t\t sub total                         :$", total_price - discount - student_offer)
        #A tax of 13% of the total price will applied at the end
            
        if charge !=0.0:        
         tax = total_price * 0.13
        print("\t\t delivery charge                    :$", charge)
        print("\t\t tax(13%)                          :$", tax)
        print("\t\t total                             :$", total_price - discount - student_offer+charge+ tax)
        
        print("\t\t----------------------")
        print("\n special instruction :" , special_instruction)
        
            
        if delivery==2:     
        #printing the bill   
         print("\n\n\n*************KJP food court*****************\n****************RECEIPT*************")
        print("name of the customer:" , customer_name)
        print("deliver address :" , address_line1 )
        print("\t", city ,  province , postal_code)
        print()
        print("order          item amount        item price        total")
        print("-----          ------------       --------          ------")
        print(food, "        ", quantity, "           $" ,price, "          $", total_price - discount )
        if(student_offer !=0.0):
            print("\nstudent savings of 10%                             :$",student_offer)
            print("\t\t sub total                         :$", total_price - discount - student_offer)
        #A tax of 13% of the total price will applied at the end
        tax = total_price * 0.13
        print("\t\t tax(13%)                          :$", tax)
        print("\t\t total                             :$", total_price - discount - student_offer+tax)
        print("\t\t----------------------")
        print("\n special instruction :" , special_instruction)
        print("\n phone number :" , phone_number)
        
assignment()
            


        


