string1 = "Listen"
# Assising 1st string into a variable
string2 = "Silent"
# Assising 2nd string into a variable
string1 = string1.lower()
# Converting the 1st string into lowercase
string2 = string2.lower()
# Converting the 2nd string into lowercase

if sorted(string1)==sorted(string2):
    # Sorting both the strings and comparing them if they are anagram or not
    print(True)
    # If both the string are anagram, Print True
else:
    print(False)
    # If both the string are not anagram, Print False