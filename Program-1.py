count = 0
# Creating counter variable for each vowel
count_1 = 0
# Creating counter variable for each vowel
count_2 = 0
# Creating counter variable for each vowel
count_3 = 0
# Creating counter variable for each vowel
count_4 = 0
# Creating counter variable for each vowel
a = "Guvi Geeks Network Private Limited"
# Saving the given string in a variable 'a'

for i in a:
    if i == 'a':
        # Verifiying if vowel 'a' is present in the given string
        x1=i
        # Saving the vowel found in a variable
        count=count+1
        # Incrementing the counter variable
    elif i == 'e':
        # Verifiying if vowel 'e' is present in the given string
        x2=i
        # Saving the vowel found in a variable
        count_1=count_1+1
        # Incrementing the counter variable
    elif i == 'i':
        # Verifiying if vowel 'i' is present in the given string
        x3=i
        # Saving the vowel found in a variable
        count_2=count_2+1
        # Incrementing the counter variable
    elif i == 'o':
        # Verifiying if vowel 'o' is present in the given string
        x4=i
        # Saving the vowel found in a variable
        count_3=count_3+1
        # Incrementing the counter variable
    elif i == 'u':
        # Verifiying if vowel 'u' is present in the given string
        x5=i
        # Saving the vowel found in a variable
        count_4=count_4+1
        # Incrementing the counter variable

# Printing the vowels found in string for no. of times

print("Vowel {} has been found {} times in the given string".format(x1,count))
print("Vowel {} has been found {} times in the given string".format(x2,count_1))
print("Vowel {} has been found {} times in the given string".format(x3,count_2))
print("Vowel {} has been found {} times in the given string".format(x4,count_3))
print("Vowel {} has been found {} times in the given string".format(x5,count_4)) 
