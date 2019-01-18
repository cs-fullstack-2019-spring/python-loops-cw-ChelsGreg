def main():
    #prob1()
    # prob2()
    #prob3()
    prob4()








#Print -20 to and including 50. Use any loop you want.

#
# def prob1():
#
#     for numPrint in range(-20, 51):
#         print(numPrint)




#Create a loop that prints even numbers
# from 0 to and including 20.
#
# def prob2():
#
#     for evenOnly in range(0, 21,2):
#          print(evenOnly)




#Prompt the user for 3 numbers.
# Then print the 3 numbers along with their average
# after the 3rd number is entered.
#


# def prob3():
#
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter a 2nd number:"))
#     num3 = int(input("Enter a 3rd number:"))
#     average = ((num1 + num2 + num3) / 3)
#     print("The average of ", num1, "+", num2, "+", num3, "is", average)




#Password Checker - Ask the user to enter a password.
# Ask them to confirm the password.
# If it's not equal, keep asking until it's correct
# or they enter 'Q' to quit.


def prob4():


    while True:
        passWord = input("Enter a password")
        confirm = input("Confirm password")
        if confirm == 'q':
            break
        if confirm != passWord:
            print("Passwords dont match.")
        else:
            break





if __name__ == '__main__':
    main()