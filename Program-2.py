rows = 20
# Initializing the needed no. of rows and saving it to a variable
for i in range(1, rows + 1):
    # Iterating through no. of rows to print required spaces   
    print(" " * (rows - i), end="")
    # Print required spaces
        
    
    for j in range(1, i + 1):
        #Iterating through rows to print required numbers
        print(j, end=" ")
        # Print required numbers according to the row number
        
    
    for k in range(i - 1, 0, -1):
        # Iterating through rows to print numbers in reverse based on the row number
        print(k, end=" ")
        # Print numbers in reverse order according to row number
                        
    print()
    # Move to the next line