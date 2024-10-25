#Write a program that takes an integer as input and returns an integer with reversed digit ordering. Examples:For input 500, the program should return 5.For input -56, the program should return -65. For input -90, the program should return -9. For input 91, the program should return 19.

def rev_int():
    while True:
        try:
            acc = int(input("Enter an integer: "))
            
            if acc < 0:
                rev_num = int('-' + str(acc)[:0:-1])
            else:
                rev_num = int(str(acc)[::-1])

            return rev_num
        
        except ValueError:
            print("Error: Please enter a valid integer.")

result_int = rev_int()
print(f"Reversed integer: {result_int}")


#First we create a function known as rev_int.
# We then prompt the user for input and check if it's an integer in line 6.
#I used the try and except block so that it ensures that only an integer is accepted. If any other data type (like a string or float) is entered, a ValueError will trigger, and an error message will be displayed.
#In line 8 we convert the integer to a string and reverse it, handling negative numbers
#The condition if acc < 0 reverses the digits of negative numbers correctly. The slice str(acc)[:0:-1] reverses the string after skipping the "-"sign.
#For positive integers, the string is reversed using [::-1], and then it's converted back to an integer.
#Line 18 calls the function and prints the result (result_int)