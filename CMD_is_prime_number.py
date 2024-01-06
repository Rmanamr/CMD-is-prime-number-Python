"""Python CMD program to check whether the entered number is prime or not.
using Python version 3.12.0
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

def main():
    """
    main function for interacting with the user
    """
    while(True):
    # while loop to keep the program running

        print("Please enter a number to check whether it is prime or not :")
        input_Number = int(input())
        # casting the input string into integer

        if(is_Prime_Number(input_Number)):
            print(input_Number, " is a prime number.")
        else:
            print(input_Number, " is not a prime number.")
        
        print("***********************************************************")


def is_Prime_Number(number):
    """
    function for checking whether a number is prime or not.
    @param number: the number to check.
    @type number: integer
    @examples: 
     >>> is_Prime_Number(7)
         True
     >>> is_Prime_Number(8)
         False
    """
    divisors = []
    divisor = 2
    while (divisor < number / 2):
        if(number % divisor == 0):
            divisors.append(divisor)
        divisor += 1
        
    if(len(divisors) == 0):
        return True
    else:
        return False
    # a prime number has only 2 divisors, number 1 and the number itself, we start divisin by 2 and end by (number/2)
    # so if the divisors list is empty, it's a prime number.
    

if __name__ == '__main__':
    main()
    # run the main function after executing this file