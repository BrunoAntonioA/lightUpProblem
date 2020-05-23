import csv

def exportData(col, rows):
    #Relleno tablero con 0 con el propósito de declarar la matriz de tamaño col y rows
    board = [[0 for x in range(col)] for y in range(rows)] 
    
    #Leo archivo csv y relleno board
    c, r = 0, 0
    with open('input.csv','r')as f:
        data = csv.reader(f)
        for row in data:
            for x in row:
                board[r][c] = x
                if c == 6:
                    c = 0
                    r = r + 1
                else:
                    c = c + 1

    return board
    

        