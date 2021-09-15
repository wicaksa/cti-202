# Given an integer n, create a two-dimensional array of size n×n according to the following rules and print it:
   # On the antidiagonal put 1.
   # On the diagonals above it put 0.
   # On the diagonals below it put 2.

def triangles(n):
   """ Creates an n*n 2D array with a 1 on the antidiagonal, with a 0 above 1, and with a 2 below it."""
   
   # Create an empty 2D array of size n*n
   arr = [[0]*n]*n
   
   # Create a variable count to keep track of the index of where 1 should be go
   count = n - 1
   
   # Iterate outer loop
   for row in range(0, n):
      # Iterate inner loop
      for col in range(0, n):
         # Case 1: If the column == count variable
         if col == count:
            # set the value to a 1 and decrement count
            arr[row][col] = 1
            count -= 1
         # Case 2: If you're not in the 0th index and the previous element is either a 1 or a 2, append a 2
         elif (row != 0) and (arr[row][col] == 1 or arr[row][col] == 2):
            arr[row][col] = 2
         # Case 3: Else, append a 0
         else:
            arr[row][col] = 0
         # Print as we go
         print(arr[row][col], end=" ")
      print("\n", end="")

# Main function
def main(): 
   # Get user input
   n = int(input())
   # Call function
   triangles(n)

# Call main
if __name__ == "__main__":
   main()
