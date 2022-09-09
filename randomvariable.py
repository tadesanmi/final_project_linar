# A program to create a guessing game
# to import  random module
import random
# to create a range of numbers between 1-10
n = random.randrange(1,100)
# to take a user input to enter a number
suggest = int(input("enter any number: "))
while n!= suggest: #means if n is not equal to the suggested input
    # if suggested input is less than n
    if suggest < n:
        print("Too low")
        # ask for the input again 
        suggest = int(input("Enter number again: "))
    #if suggested input is greater than n 
    elif suggest > n:
        print("Too high")
        # ask for the input again
        suggest = int(input("Enter number again: "))
    # if the suggested value is equal to the value of n terminate the while loop
    else:
        break
print("you guess is very accurate!!")