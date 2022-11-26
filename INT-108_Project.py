N=int(input("Enter the value of N: "))    # Taking User input for the value of N
magicSquare = [[0 for i in range(N)] for i in range(N)]
k=(N*(N*N)+1)/2
def OddMagicsquare(x): #Defining a function to create a magic square
    
    Matrix=[[0 for a in range(N)] for b in range(N)] #Intializing a 2D array with all the values set to zero

    i=N//2  #Intializing Position of 1
    j=N-1   #Intializing Position of 1
    num=1
    while num<=(N*N):
        if i==-1 and j==N:
            i=0
            j=N-2
        else:
            
            if j==N:
                j=0
            if i<0:
                i=N-1
        if Matrix[int(i)][int(j)]:
            i=i+1
            j=j-2
            continue
        else:
            Matrix[int(i)][int(j)]=num
            num=num+1
        i=i-1
        j=j+1
    for i in range(0, N):
        for j in range(0, N):
            print('%2d ' % (Matrix[i][j]),end='')
            if j == N - 1:
                print()
    return Matrix,N


def fillSinglyEvenOrder(magicSquare, N):
    # Build odd order magic square for each quarter:
    # Top left:
    fillQuarterOfSinglyEvenOrder(magicSquare, 0, N/2, 0, N/2, 1, (N/2)*(N/2))
    # Bottom right:
    fillQuarterOfSinglyEvenOrder(magicSquare, N/2, N, N/2, N, (N/2)*(N/2) + 1, N*N/2)
    # Top right:
    fillQuarterOfSinglyEvenOrder(magicSquare, 0, N/2, N/2, N, N*N/2 + 1, 3*(N/2)*(N/2))
    # Bottom left:
    fillQuarterOfSinglyEvenOrder(magicSquare, N/2, N, 0, N/2, 3*(N/2)*(N/2) + 1, N*N)

    shiftCol = int((N/2 - 1)/2)
    # Exchange columns in left quarters:
    for i in range(N//2):
        for j in range(shiftCol):
            # If we're at middle row of top left quarter, shift 1 to the right:
            if i == N//4:
                exchangeCell(i, j + shiftCol, magicSquare)
            else: 
                exchangeCell(i, j, magicSquare)
    # Exchange columns in right quarters if N > 6
    for i in range(N//2):
        for j in range(N - 1, N - shiftCol, -1):
            exchangeCell(i, j, magicSquare)

# Helper method fills a quarter of a singly-even order magic square to make an 
# odd order magic square.
def fillQuarterOfSinglyEvenOrder(magicSquare, firstRow, lastRow, firstCol, lastCol, num, lastNum):
    # Initialize position for 1st number:
    i = firstRow 
    j = (lastCol + firstCol)//2

    # One by one put all values in magic square 
    while num <= lastNum: 
        # 4th condition:
        if i < firstRow and j >= lastCol: 
            i += 2 
            j -= 1
        # 2nd condition:
        # If next number goes to out of square's right side 
        if j >= lastCol: 
            j = firstCol 
        # 1st condition:
        # If next number goes to out of square's upper side 
        if i < firstRow: 
            i = lastRow - 1 
        # 3rd condition:
        if magicSquare[int(i)][int(j)] != 0: 
            i += 2 
            j -= 1 
            continue 
        else:
            # Add num to cell:
            magicSquare[int(i)][int(j)] = num
            # Increment num to next one:
            num += 1
        i -= 1 
        j += 1 
    return magicSquare

# Helper method exchanges cell i,j with N/2+i,j
def exchangeCell(i, j, matrix):
    r = len(matrix)//2 + i
    matrix[i][j], matrix[r][j] = matrix[r][j], matrix[i][j]


def DoublyEven(N):
     
    # 2-D matrix with all entries as 0
    arr = [[(N*y)+x+1 for x in range(N)]for y in range(N)]
 
    # Change value of array elements at fix location
    # as per the rule (N*N+1)-arr[i][[j]
     
    # Corners of order (N/4)*(N/4)
    # Top left corner
    for i in range(0,N//4):
        for j in range(0,N//4):
            arr[i][j] = (N*N + 1) - arr[i][j];
     
    # Top right corner
    for i in range(0,N//4):
        for j in range(3 * (N//4),N):
            arr[i][j] = (N*N + 1) - arr[i][j];
 
    # Bottom Left corner
    for i in range(3 * (N//4),N):
        for j in range(0,N//4):
            arr[i][j] = (N*N + 1) - arr[i][j];
     
    # Bottom Right corner
    for i in range(3 * (N//4),N):
        for j in range(3 * (N//4),N):
            arr[i][j] = (N*N + 1) - arr[i][j];
             
    # Centre of matrix,order (N/2)*(N/2)
    for i in range(N//4,3 * (N//4)):
        for j in range(N//4,3 * (N//4)):
            arr[i][j] = (N*N + 1) - arr[i][j];
     
    # Printing the square
    for i in range(N):
        for j in range(N):
            print ('%2d ' %(arr[i][j]),end=" ")
        print()
         
# Driver Program
if N%2!=0:
    OddMagicsquare(N)
    print("The Magic Sum is: ")
elif N%4==2:
    fillSinglyEvenOrder(magicSquare, N)
    for i in range(N):
        for j in range(N):
            print('%2d ' % (magicSquare[i][j]),end='')
            if j == N - 1:
                print()
else:
    DoublyEven(N)



















     


