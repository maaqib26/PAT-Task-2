st1 = 'gbcf'
# Storing String 1 in a variable
st2 = 'bcfd'
# Storing String 2 in a variable
stl1 = len(st1)
# Storing length of String 1 in a variable
stl2 = len(st2)
# Storing length of String 2 in a variable

max_count = 0
# Initializing a counter variable to store count of no. of char in the common substring
lcs = ""
# Initializing a  variable to store value of common substring

for i in range(stl1):
    # Iterating through length of string1
    for j in range(stl2):
        # Iterating through length of string2
        k = 0
        # Initializing a temp variable k
        while i+k < stl1 and j+k < stl2 and st1[i+k] == st2[j+k]:
            # Condition to check substring
            k += 1
        if k > max_count:
            max_count = k
            lcs = st1[i:i+k]

print("Length of longest common substring:", max_count)
print("Longest common substring(s):", lcs)