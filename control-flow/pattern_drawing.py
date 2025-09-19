# Prompt User for Pattern Size:
size = int(input("Enter the size of the pattern: "))

row = 0
# use while loop for rows
while row < size:
 
 # use for loops for columns
 for col in range(size):
    print("*", end="")

# Move to the next line after each row
    print()
    row +=1