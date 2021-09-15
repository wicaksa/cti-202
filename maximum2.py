# Given two integers - the number of rows m and columns n of m×n 2d list - and subsequent m rows of n integers, 
# find the maximal element and print its row number and column number. 
# If there are many maximal elements in different rows, report the one with smaller row number. 
# If there are many maximal elements in the same row, report the one with smaller column number.

def find_maximum(l, row, col):
   """Finds the row and column number of the maximum value of the input 2D list. """
   
   # Create variables to store max_value, max_row, and max_col
   max_value = l[0][0]
   max_row = 0
   max_col = 0
   
   # Iterate through the list to find the maximum value and it's row and column numbers
   for r in range(0, row):
      for c in range(0, col):
         if l[r][c] > max_value:
            max_value = l[r][c]
            max_row = r
            max_col = c
   print(max_row, max_col)

def main():
    # Get value for m and n using string comprehension
    m, n = [int(x) for x in input().split()]
    # Create an empty list to hold your final list elements
    num_list = []
    
    # Iterate to get user input and store them in a 2D list
    for i in range(0, m):
       temp_list = []
       temp_list = input().split()
       num_map   = map(int, temp_list)
       int_list  = list(num_map)
       num_list.append(int_list)
   
    # call the function 
    find_maximum(num_list, m, n)

# call to main
if __name__ == "__main__":
    main()
