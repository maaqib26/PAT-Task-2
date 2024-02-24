st = input("Enter the String:")
# Getting String value from the user and storing it in a variable
st = st.replace(" ","").lower()
# Removing any extra space and converting the string into lowecase
st1 = st[::-1]
# Verifying if the given string is Palindrome or not
#print(st1 == st)
if st1 == st:
    print(True)
    # If the given string is Palindrome , Returns True
else:
    print(False)
    # If the given string is Palindrome , Returns False