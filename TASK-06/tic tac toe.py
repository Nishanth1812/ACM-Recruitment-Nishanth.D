import random

board = ["-"] * 9
symbols = {"player": "", "computer": ""}
currentPlayer = None
winner = None
gameRunning = True

def displayBoard():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

def makeMove(player):
    if player == symbols["player"]:
        while True:
            try:
                move = int(input("Choose a spot (1-9): ")) - 1
                if 0 <= move < 9 and board[move] == "-":
                    board[move] = symbols["player"]
                    break
                else:
                    print("Spot already taken or invalid.")
            except ValueError:
                print("Enter a valid number between 1 and 9.")
    else:  
        move = random.choice([i for i, spot in enumerate(board) if spot == "-"])
        board[move] = symbols["computer"]


def checkGameState():
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6)]
    
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] and board[a] != "-":
            return board[a]

    if "-" not in board:
        return "Tie"
    
    return None

def switchTurn():
    global currentPlayer
    currentPlayer = symbols["computer"] if currentPlayer == symbols["player"] else symbols["player"]

def initSymbols():
    while True:
        choice = input("Do you want to be X or O? ").upper()
        if choice in ["X", "O"]:
            symbols["player"] = choice
            symbols["computer"] = "O" if choice == "X" else "X"
            break
        else:
            print("Invalid choice, please pick X or O.")

def playGame():
    global currentPlayer
    initSymbols()
    currentPlayer = symbols["player"]  

    while gameRunning:
        displayBoard()
        print(f"{currentPlayer}'s turn:")
        makeMove(currentPlayer)
        
        result = checkGameState()
        if result:
            displayBoard()
            if result == "Tie":
                print("It's a tie!")
            else:
                print(f"The winner is {result}!")
            break

        switchTurn()
while True:
    playGame()
    ch=input("do you want to play again? (yes/no): ")
    if ch.lower()=="no":
        print("thank you for playing")
        break
    else:
        continue
