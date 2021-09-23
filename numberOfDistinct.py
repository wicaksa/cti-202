# Input: Given a list of integers
# Count how many distinct numbers it has. (This task can be solved in a single line.)

def countDistinctNumbers(lst):
   # Counts the distinct numbers in the list 
   # Input : List of intergers : lst
   # Output: None (Print Statement)
   
   # Convert list to a set 
   numSet = set(lst)
   
   # Print the length
   print(len(numSet))

def main():
   # Main function
   numList = [x for x in input().split()]
   countDistinctNumbers(numList)

# Call to main
if __name__== "__main__":
   main()
