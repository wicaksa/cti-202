# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, followed by one integer c. 
# Multiply every element by c and print the result.

# Get rows and columns
rows, cols = [int(x) for x in input().split()]

# Create an empty list 
result_list = []

# Add input to empty list
for i in range(0, rows):
   temp_list = []
   temp_list = input().split() # list of string  # temp_list = ['1', '2', '3']
   map_obj = map(int, temp_list) # turn into int 
   int_list = list(map_obj) # now it's a int list
   result_list.append(int_list)

# Get value of c
c = int(input())

# Multiply each element by c
for row in range(0, rows):
   for col in range(0, cols):
      result_list[row][col] = result_list[row][col]*c
      print(result_list[row][col], end=" ")
   # print on a new line
   print('\n', end="")
