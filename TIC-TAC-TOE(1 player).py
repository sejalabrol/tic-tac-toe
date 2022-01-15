import os
import time
import random

def print_header():
    print("WELCOME TO")
    print("""
    _______     ____    _______         ____    _______   _____    ______   
       |    |  /           |     /\    /           |     /     \  |          1 | 2 | 3 
       |    | |      __    |    /  \  |      __    |    |       | |_____    ---|---|---
       |    | |            |   /----\ |            |    |       | |          4 | 5 | 6        
       |    |  \____       |  /      \ \____       |     \_____/  |______   ---|---|---
                                                                             7 | 8 | 9      
                                                                        """)        

board=[" "," "," "," "," "," "," "," "," "]

def print_board():
    print("   |   |   ")
    print(" "+board[0]+" "+"|"+" "+board[1]+" "+"|"+" "+board[2]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[3]+" "+"|"+" "+board[4]+" "+"|"+" "+board[5]+" ")
    print("___|___|___")
    print("   |   |   ")
    print(" "+board[6]+" "+"|"+" "+board[7]+" "+"|"+" "+board[8]+" ")
    print("   |   |   ")

def is_winner(board,player):
    if (board[0]==player and board[1]==player and board[2]==player) or \
     (board[3]==player and board[4]==player and board[5]==player) or \
     (board[6]==player and board[7]==player and board[8]==player) or \
     (board[0]==player and board[3]==player and board[6]==player) or \
     (board[1]==player and board[4]==player and board[7]==player) or \
     (board[2]==player and board[5]==player and board[8]==player) or \
     (board[0]==player and board[4]==player and board[8]==player) or \
     (board[2]==player and board[4]==player and board[6]==player) :
        return True
    else:
        return False

def is_tie(board):
    if " " in board :
        return False

    else:
        print("It's a Tie !")
        time.sleep(2)
        return True

def input_player(board,player):
    entry=False
    while entry==False :
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header()
        print_board()
        choice=int(input("Enter your choice (Player "+player+") : "))
        if board[choice-1]==" ":
            board[choice-1]=player
            entry=True
        else :
            print("This space is full")
            time.sleep(1)

def get_move(board):
    for i in range(0,9):
        if board[i]==" ":
            board[i]="o"
            if is_winner(board,"o") :
                return i
            else:
                board[i]=" "

    for i in range(0,9):
        if board[i]==" ":
            board[i]="x"
            if is_winner(board,"x") :
                board[i]=" "
                return i
            else:
                board[i]=" "
                
    while True:
        move=random.randint(0,8)
        if board[move]==" ":
            return move
            break
    
while True :
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    print_board()

    input_player(board,"x")

    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    print_board()

    if is_winner(board,"x"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header()
        print_board()
        print("Player x won !!")
        time.sleep(2)
        break


    if is_tie(board):
        break

    time.sleep(0.25)

    choice=get_move(board)
    board[choice]="o"
    
  
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header()
    print_board()

    if is_winner(board,"o"):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header()
        print_board()
        print("Player o won !!")
        time.sleep(2)
        break

    
        

       

