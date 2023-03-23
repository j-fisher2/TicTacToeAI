import random

class TicTacToe:
    def __init__(self):
        self.players=['X','O']
        self.board=[" " for i in range(9)]
        self.curPlayer=self.players[0]
        self.first_move=True
    
    def print_board(self):
        print("-------------")
        for i in range(3):
            print("|",self.board[3*i],"|",self.board[3*i+1],"|",self.board[3*i+2],"|")
            print("-------------")
    
    def setPlayer(self,choice):
        if choice==1:
            self.curPlayer=self.players[1]
            self.first_move=False

    def get_winner(self):
        for i in range(3):
            if self.board[i]==self.board[i+3]==self.board[i+6]!=" ":
                return self.board[i]
            if self.board[3*i]==self.board[3*i+1]==self.board[3*i+2]!=" ":
                return self.board[3*i]
        if self.board[0]==self.board[4]==self.board[8]!=" ":
            return self.board[0]
        if self.board[2]==self.board[4]==self.board[6]!=" ":
            return self.board[2]
        if self.full():
            return "Draw"
        return None
        
    def full(self):
        return " " not in self.board
    
    def get_empty(self):
        res=list()
        for i in range(9):
            if self.board[i]==" ":
                res.append(i)
        return res     
    
    def get_children(self):
        children=[]
        for square in self.get_empty():
            child=TicTacToe()
            child.board=self.board.copy()
            child.board[square]=self.curPlayer
            child.curPlayer="O" if self.curPlayer=="X" else "X"
            children.append(child)
        return children
    
    def getMove(self,child):
        for i in range(len(child.board)):
            if child.board[i]!=" " and self.board[i]==" ":
                self.board[i]=child.board[i]
    
    def minimax(self,maximizing=True):
        winner=self.get_winner()
        if winner!=None:
            if winner=='X':
                return 1
            elif winner=='O':
                return -1
            elif winner=="Draw":
                return 0
        if maximizing: 
            best_score=float("-inf")
            for child in self.get_children():
                child_value=child.minimax(False)
                if child_value>best_score:
                    best_score=child_value
            return best_score
        else: 
            best_score=float("inf")
            
            for child in self.get_children():
                child_value=child.minimax()
                if child_value<best_score:
                    best_score=child_value
            return best_score
    
    def make_move(self,row=None,col=None):
        if not self.first_move:
            self.board[0]="O"
            self.curPlayer="X"
            self.first_move=True
            return
        if row==None and col==None:
            best_move=None
            best_value=float("inf")
            for child in self.get_children():
                child_value=child.minimax(True)
                if child_value<best_value:
                    best_value=child_value
                    best_move=child
            self.getMove(best_move)
            self.curPlayer="X"
            return None

        else:
            if self.board[3*row+col]==" ":
                self.board[3*row+col]=self.curPlayer
                self.curPlayer="O"
            else:
                print("Invalid move. Try again.")
                return None
        return None

def play_game():
    game=TicTacToe()
    print("Welcome to TicTacToe")
    print("Computer plays as \'O\'")
    game.print_board()
    choice=0
    print("Who goes first? Enter 1 for the computer, 2 for you.")
    while choice!=1 and choice!=2:
        choice=int(input())
    game.setPlayer(choice)
    while not game.get_winner():
        if game.curPlayer=="X":
            row=int(input("Enter Row between 1 and 3: "))
            if row<1 or row>3:
                print("Invlid input")
                continue
            col=int(input("Enter Column between 1 and 3: "))
            if col<1 or col>3:
                print("Invalid input")
                continue
            game.make_move(row-1,col-1)
        else:
            game.make_move()
        game.print_board()
    w=game.get_winner()
    if w=="O":
        print("You Lost")
    elif w=="X":
        print("You Won")
    else:
        print("Its a tie")
    
play_game()