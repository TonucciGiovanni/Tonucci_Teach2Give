#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string. Examples: "hi"=> returns "Hi" "i love programming"=> returns "I Love Programming"


def cap_words():
    capp = input("Enter a string: ")
    
    if capp.isalpha() or " " in capp:

        cap_str = capp.title()
        return cap_str
    else:
        print("Error: Please enter a valid string.")


cap_res = cap_words()
if cap_res:
    print("Uppercase First letter:", cap_res)


#First we define a function known as cap_words.
#Line 7 checks if the input is a string containing alphabetic characters. If the user enters numbers or special characters without spaces, it shows an error. This in ensured by isalpha() and " " condition.
#In Line 9 we capitalize the first letter of each word in the string using the title() method.
#In Line 15 we call the function and print the result