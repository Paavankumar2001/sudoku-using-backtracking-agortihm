#taking the input from the user for the sudoku chart
sudoku = []
numberOfRows = 9
numberOfColumns = 9
print("enter each value and press enter ,and give 0 as value for empty characters")
for row in range (numberOfRows):
    sudoku.append([])             #adds an empty new row
    for column in range (numberOfColumns):
        value = eval(input())
        sudoku[row].append(value)
        

def display(chart):             #displays the sudoku chart based on the given input
    for i in range(len(chart)):
        if i % 3 == 0 and i != 0:       #after the third line and simultaneously for initial value
            print("- - - - - - - - - - - - - ")     #not equal to 0 prints a dotted line

        for j in range(len(chart[0])):      #same as for the third column for vertical lines
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:                  #prints 8th index position 1-9 for every row
                print(chart[i][j])
            else:
                print(str(chart[i][j]) + " ", end="")
            #prints the remaining rows and columns
display(sudoku)

def search(chart):         #searches for the empty columns throughout the chart
    for i in range(len(chart)):         #gives the position at which there are empty columns
        for j in range(len(chart[0])):
            if chart[i][j] == 0:
                return (i, j)
    return None



def check(chart, number, position):#checks if the allocated value does satisfy with the conditions are not
    # Checking rows for the conditions
    for i in range(len(chart[0])):#starting from the intitial index row from the list
        if chart[position[0]][i] == number and position[1] != i:#allocating the number to the position
            return False
        
    # Check columns for the conditions
    for i in range(len(chart)):
        if chart[i][position[1]] == number and position[0] != i:
            return False
        
    # Checking the sub 3*3 matrix
    subMatrix_row = position[1] // 3
    subMatrix_column = position[0] // 3

    for i in range(subMatrix_column*3, subMatrix_column*3 + 3):
        for j in range(subMatrix_row * 3, subMatrix_row*3 + 3):
            if chart[i][j] == number and (i,j) != position:
                return False

    return True


#backtracking algorithm using recursive function 
#callinfg for each and every element inserted at evry position by calling check function
def solve(chart):
    find = search(chart)        #calls search function
    if not find:
        return True
    else:
        horizontal, vertical = find

    for i in range(1,10):
        if check(chart, i, (horizontal, vertical)):      #calls check function
            chart[horizontal][vertical] = i
            if solve(chart):                            #calls solve function
                return True

            chart[horizontal][vertical] = 0
    
    return False

solve(sudoku)
print("___________________________________")
display(sudoku)