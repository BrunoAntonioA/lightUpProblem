import data as data
import state as st

def buscarCeroCuatro(state):
    col = len(state.board) 
    rows = len(state.board[0]) 
    for x in range(col):
        for y in range(rows):
            #Si nos encontramos con una casilla que tiene valor 0
            if state.board[x][y] == "0":
                if x < col-1:
                    state.bloquearCasilla(x+1, y)
                if x > 0:
                    state.bloquearCasilla(x-1, y)
                if y < rows-1:
                    state.bloquearCasilla(x, y-1)
                if y > 0:
                    state.bloquearCasilla(x, y+1)
            elif state.board[x][y] == "4":
                if x < col-1:
                    state.ponerAmpolleta(x+1, y)
                if x > 0:
                    state.ponerAmpolleta(x-1, y)
                if y < rows-1:
                    state.ponerAmpolleta(x, y+1)
                if y > 0:
                    state.ponerAmpolleta(x, y-1)
    print("0's y 4's identificados y trabajados")





board = data.exportData(7, 7)
state = st.State(board)
state.printBoard()
buscarCeroCuatro(state)
state.printBoard()

"""
state.ponerAmpolleta(4, 4)
state.printBoard()
"""