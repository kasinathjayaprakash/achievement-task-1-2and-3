#author - kasinath jayaprakash
#task - 6

#creating a list
list_of_numbers = []
# asking the user to Enter the numbers separated by comma
list_of_numbers = list(map(int,input("Enter the numbers : ").strip().split(',')))
print("The entered list is: ",list_of_numbers)

my_list = list_of_numbers
# creating a prime number list by applying some conditions
prime = []
for i in my_list:
#declaring a variable to count
    count=0
    for j in range(1,i):
        if i%j ==0:
            #increasing the count by 1
            count+=1
    #if the count equals 1
    if count==1:
        prime.append(i)
#printing prime numbers
print("the prime numbers are ",prime )

#creating a non prime number list by removing the prime list from the main list
non_prime = [i for i in list_of_numbers if i not in prime]
#printing non prime numbers
print("the non prime numbers are",non_prime)