
class State:
    def __init__(self, board):
        self.board = board


    def printBoard(self):
        for x in range(len(self.board)):
            print("")
            for y in range(len(self.board[x])):
                print("  ", self.board[x][y], end="")
        print("")

    #Funcion para poner una ampolleta
    def ponerAmpolleta(self, x, y):
        r = len(self.board)
        c = len(self.board[0])

        if x > c:
            print("error")
        if self.board[x][y] != "B":
            print("Lo siento, no puedes insertar una ampolleta aquí")
            return 0
        else:
            #Pongo la ampolleta en x y
            self.board[x][y] = "A"
            #Ilumino las casillas hacia abajo
            if(x != r):
                for i in range(x+1, r):
                    if self.board[i][y] != "B":
                        break
                    self.board[i][y] = "I"
            #Ilumino las casillas hacia la arriba
            if(x != 0):
                for i in range(x-1, -1, -1):
                    if self.board[i][y] != "B":
                        break
                    self.board[i][y] = "I"
            #Ilumino las casillas hacia la derecha
            if(y != c):
                for i in range(y+1, r):
                    if self.board[x][i] != "B":
                        break
                    self.board[x][i] = "I"
            #Ilumino las casillas hacia la izquierda
            if(y != c):
                for i in range(y-1, -1, -1):
                    if self.board[x][i] != "B":
                        break
                    self.board[x][i] = "I"
        print("")

    #Funcion para bloquear casillas
    def bloquearCasilla(self, x, y):
        r = len(self.board)
        c = len(self.board[0])
        if self.board[x][y] == "A" or self.board[x][y] == "N" or self.board[x][y] == "0" or self.board[x][y] == "1" or self.board[x][y] == "2" or self.board[x][y] == "3" or self.board[x][y] == "4":
            print("Esta casilla es un bloque negro o tiene una ampolleta. No se puede bloquear")
            return 0
        else:
            self.board[x][y] = "X"
        return self

                

            
