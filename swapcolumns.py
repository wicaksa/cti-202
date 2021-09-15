# Problem Statement

# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, 
# followed by two non-negative integers i and j less than n, swap the columns i and j of 2d list and print the result.

def swap_columns(l, row, col, col1, col2):
   # Swaps the numbers in the specified columns of the list and prints the resulting list.
   
   # Input: 2D int list: l 
   #        int: row 
   #        int: col
   #        int: col1
   #        int: col2
   # Output: None (Prints l)
   
   # Iterate through the rows and perform a swap to the list in the specified columns
   for r in range(0, row):
      l[r][col1], l[r][col2] = l[r][col2], l[r][col1]
   
   # Iterate through the list and print the result
   for i in range(0, row):
      for j in range(0, col):
         print(l[i][j], end=" ")
      print("\n", end="")

# Main function    
def main():
   # Get m and n using string comprehension
   m, n = [int(x) for x in input().split()]
   
   # Create an empty list to store the input 
   num_list = []
   
   # Covert the input which is a string of numbers separated by white space into a list of integers
   # Append the list of integers to num_list
   for i in range(0, m):
      temp_list = []
      temp_list = input().split() # split a string into a list of strings
      num_map = map(int, temp_list)
      int_list = list(num_map)
      num_list.append(int_list)
   
   # Get values for i and j using string comprehension
   i, j = [int(x) for x in input().split()]
   
   # Call swap_columns
   swap_columns(num_list, m, n, i, j)
  
# Call main()
if __name__ == "__main__":
   main()
