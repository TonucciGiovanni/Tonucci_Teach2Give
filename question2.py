#Question 2: Write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run"

def palindromeOrnot(xin):

    cl = ''.join(xin.lower().split())
    
    
    return cl == cl[::-1]

yin = input("Enter a word or phrase: ")

if palindromeOrnot(yin):
    print(f'"{yin}" It is a palindrome.')
else:
    print(f'"{yin}" It is not a palindrome.')


#define a function. my function is known as palindromeOrnot.
# in the line of code cl = ''.join(xin.lower().split()):
# The lower() function converts the input to lowercase to ensure case insensitivity.
# The split() function removes all spaces, and ''.join() puts the characters back together.
#in line 8: we Return to check if the string (cl) is the same when reversed
#cl[::-1] - is a Python slice that reverses the string.
#in line 10: we prompt the user to enter a word or phrase
# we use an if statement to check if the input is a palindrome in line 12
#Finally, the code compares the original string (cl) to the reversed version and prints whether the input is a palindrome.
