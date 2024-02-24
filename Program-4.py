# Approach 1 - Using set method of string

string='doodledraw'
# Storing the required string into a variable
s=set(string)  
#Creating set of Unique Un-Ordered Elements using set function and saving it into a variable
l=len(s)       
#Finding the length of 's' variable and storing into a variable
print("No. of Unique characters in the given string '{}' are {}".format(string,l))
# Printing the no. of unique characters in the given string

# Approach 2 - Using empty list to store the unique characters of the string

string='doodledrawing'
# Storing the required string into a variable
count=0
# Creating a counter variable to store no. of unique characters in the given string
temp=[]
# Creating a empty list to filter unique characters out of the given list
for i in string:
    # Iterating through each character in the string
    if(i not in temp):
        # If character of the given string is not temp
        count+=1
        # Increment the count variable
        temp.append(i)
        # Add the character into the given list
print("No. of Unique characters in the given string '{}' are {}".format(string,count))
# Printing the no. of unique characters in the given string 