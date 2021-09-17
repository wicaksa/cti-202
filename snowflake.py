def snowflake(n):
    # Prints a snoflake pattern with "." and "*" arranged in a pattern.
    # Input : n integer used to create an nxn 2d array.
    # Output: None (Prints out image).
   
    # Create a nxn 2d array filled with ".".
    # This creates a list with n different objects that point to different memory locations
    arr = [["." for i in range(n)] for j in range(n)]
   
    # Iterate through the 2D array and place "*" where they go
    for row in range(0, n):
        for col in range(0, n):
            # Middle column
            if col == n//2:
                arr[row][col] = "*"
            # Diagonal 1
            elif row == col:
                arr[row][col] = "*"
                arr[col][row] = "*"
            # Diagonal 2
            elif (n-1) == (row+col):
                arr[row][col] = "*"
                arr[col][row] = "*"
            # Middle Row should be all *
            elif row == n//2:
                arr[row][col] = "*"
                
    # Print snowflake
    for row in range(0, n):
        for col in range(0, n):
            print(arr[row][col], end = " ")
        print("\n", end="")
        
def main():
    n = int(input())
    # DEBUG n = 7
    snowflake(n)

if __name__ == "__main__":
    main()
