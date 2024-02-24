a1 = "Guvi Geeks Network Private Limited"
# Stroing the given string in a variable
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# Storing vowels characters in a list variable

for i in a1:
    if i in vowels:
        #finding if vowels present in the given string
        a1 = a1.replace(i,"")
        #Replacing the vowels with empty space
print("Updated String after removing the vowels - {}".format(a1))
# Printing the new value of the string after removing the vowels