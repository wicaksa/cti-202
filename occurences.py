# Given two lists of numbers, count how many numbers of the first one occur in the second one.

def occurence(A, B):
   # Counts the occurences of items in list A that's in list B
      # Convert each to a set
      A = set(A)
      B = set(B)
      
      # Get the length of the intersection between the two lists
      print(len(A.intersection(B)))
      
def main(): 
   # Get user input and convert it into two lists 
   A = [num for num in input().split()]
   B = [num for num in input().split()]
   
   # Call to occurence()
   occurence(A, B)

if __name__ == "__main__":
   main()
