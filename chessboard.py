def chessboard(row, col):
   # Creates a chessboard pattern with * and . depending on given input.
   # Input : row : int representing the rows
   #         col : int representing the columns
   # Output: None (Print the result list)
   
   # Create Checkerboard inititially w/ "."
   arr = [["." for i in range(col)] for j in range(row)]
   # debug print(arr)
   
   # Iterate through the list
   for r in range(0, row):
      for c in range(0, col):
         # On odd rows, populate even columns with "*"
         if (r % 2 != 0):
            if (c % 2 == 0):
               arr[r][c] = "*"
         # On even rows populate odd columns with "*"
         elif (r % 2 == 0):
            if (c % 2 != 0):
               arr[r][c] = "*"
         print(arr[r][c], end = " ")
      print("\n", end="")
   
def main():
   n, m = [int(x) for x in input().split()]
   # debug print(n, m)
   chessboard(n, m)

# Call to Main
if __name__ == "__main__":
   main()
