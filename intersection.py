# Input : Given two lists of numbers.
# Output: Find all the numbers that occur in both the first and the second list. 
#         Print them in ascending order.

def main():
   # Main function
   
   # Get user input and convert it to a list of int
   A = [int(x) for x in input().split()]
   B = [int(x) for x in input().split()]
   
   # Call intersection
   intersection(A, B)

def intersection(A, B):
   # Convert the two lists into sets 
   A = set(A)
   B = set(B)
   
   # Get the intersection of A and B 
   C = A.intersection(B)
   
   # Print the sorted list 
   print(*sorted(C))

if __name__ == "__main__":
   main()
