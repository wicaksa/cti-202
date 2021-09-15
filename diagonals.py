# Problem Statement:
# Given an integer n, create a two-dimensional array of size n×n according to the following rules and print it:
    # On the main diagonal put 0.
    # On the diagonals adjacent to the main put 1.
    # On the next adjacent diagonals put 2, and so forth.

def diagonals(n):
   """ Given n, prints a 2D list that has digits equaling one another diagonally."""
   
   # Iterate the outer loop
   for row in range(0, n):
      # Create a value to print and set it to the outer loop 
      value = row
      # Iterate the inner loop
      for col in range(0, n):
         # Print absolute value with a " "
         print(abs(value), end=" ")
         # Decrement value 
         value = value - 1
      print('\n', end="")
   
# Main Function
def main():
   # Get user input
   num = int(input())
   # Call function
   diagonals(num)

# Call main
if __name__ == "__main__":
   main()
   
