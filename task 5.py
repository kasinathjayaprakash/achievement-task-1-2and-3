#author - kasinath jayaprakash
#task - 5

#asking the user to enter a number
number=int(input("Input a number\n "))
#creating a dictionary
dictionary = dict()

#adding conditions to the dictionary
for x in range(1,number+1):
    dictionary[x]=x*x*x

print(dictionary) 