string= "mississippi is a nice place"
# Storing the required string in a variable
print("The Original String is '{}'".format(string))
# Printing the original string
char_ex={}
# Declaring a empty Dictionary

for i in string:
    #Iterating through each character in the string
    if i in char_ex:
        # Verifying if each character of string is in the declared dictionary 
        char_ex[i]=char_ex[i]+1
        # If character of the string is found in the dictionary, iterating it.
    else:
        char_ex[i] = 1
        # Else, If the character of the string is not found in the dictionary, Just adding the character to the dictionary
print(char_ex)
#printing string characters with count in dictionary format 
result= max(char_ex, key = char_ex.get)
# Finding the maximum count of the dictionary and saving it to a variable
print("The frequently used character used in the string '{}' is {}".format(string,result))