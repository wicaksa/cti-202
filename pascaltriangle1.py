# Problem Statement:
# Given a positive integer n, print the value '1' n times as output.

def print_one(n):
   # Prints the value '1' n times
   # Input: Positive integer n 
   # Output: None (prints out)
   
   # Iterate from 0 - n:
   for i in range(0, n):
      # Print '1' with a space after
      print('1', end="")
      
def main():
   # Get user input
   n = int(input())
   # Call print_one function
   print_one(n)

# Call Main
if __name__ == "__main__":
   main()
