#author - Kasinath jayaprakash
#achievement task - 3
#this is used to find the correct username according to the conditions

#asking the user for entering the username
username = str(input("please enter your username.\n"))
#if the username is less than or equal to one letter
if len(username) <=1:
    print("sorry,username must be longer than one letter")
#if the username is greater than or equal to 21 letters 
if len(username) >=21:
    print("sorry, username must not more than 20 letters in length")
#if the username does not contain an uppercase or a number 
if username.isalnum() == username or username.upper() == username or username.lower()== username:
    print("the username must contain atleast a uppercase and a numbera(0-9)")