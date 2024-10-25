#Write a Python function to check whether a string is pangram or not. (Assumethe string passed in does not have any punctuation) Note: Pangrams are words or sentences containing every letter of thealphabet at least once. For example: "The quick brown fox jumps over the lazy dog"


import string

def pangramOrnot(pan):
    
    alphabets = set(string.ascii_lowercase)
    
    iset = set(pan.lower().replace(' ', ''))
    
    return alphabets.issubset(iset)

uset = input("Enter a string: ")

if pangramOrnot(uset):
    print(f'"{uset}" It is a pangram!')
else:
    print(f'"{uset}" It is not a pangram.')



#Define the fucntion first of all. My function is called pangramOrnot.
#In line 8 we create a set of all lowercase letters from the English alphabet
#The string.ascii_lowercase gives all lowercase English letters
#alphabets is a string variable set which is created from the lowercase alphabet for easy comparison.
#In line 10 we remove spaces and convert the input to lowercase, then create a set of the input string. The input string is converted to lowercase and spaces are removed, then stored as a set of characters.
#In line 12 we check if the input set contains all letters in the alphabet set
#In line 14 we prompt the user to enter a string and then check if the input is a pangram using the if conditions.