import copy
import random

GAME_OPTIONS = ["X", "O"]

board = [[[1], [2], [3]],
        [[4], [5], [6]],
        [[7], [8], [9]]]

board_place = { 1:board[0][0], 2:board[0][1], 3:board[0][2],
                4:board[1][0], 5:board[1][1], 6:board[1][2],
                7:board[2][0], 8:board[2][1], 9:board[2][2]}

print("Welcome to Tic Tac Toe")
def main():
    while True:

        choice = input("Play with Computer(c) or another Player(p)[q to quit]").lower()

        if choice == "c":
            play_with_computer()
        elif choice == "p":
            play_with_player()
        elif choice == "q":
            quit()

def play_with_player():

    player1 = random.choice(GAME_OPTIONS)
    (player2 := "X") if player1 == "O" else (player2 := "O")
    print(f"Player1 is {player1} and Player2 is {player2}") 

    while True:

        player1_move = get_player_move()
        place_in_board(board_place, player1_move, player1)
        check_for_win(board, "Player1")

        player2_move = get_player_move()
        place_in_board(board_place, player2_move, player2)
        check_for_win(board, "Player2")

def play_with_computer():

    player = random.choice(GAME_OPTIONS)
    (computer := "X") if player == "O" else (computer := "O")
    print(f"You are {player} and Computer is {computer}")

    while True:
        player_move = get_player_move()
        place_in_board(board_place, player_move, player)
        check_for_win(board,"Player")

        computer_move = get_computer_move(computer,player)
        place_in_board(board_place, computer_move, computer)
        check_for_win(board,"Computer")
        



def get_player_move():
    while True:
        print_board(board)
        player_mv = input("Where do you want to place: ")
        try:
            player_mv = int(player_mv)
        except:
            print("Please enter a valid number")
            continue
        if player_mv >= 1 and player_mv <= 9:
            if str(board_place[player_mv][0]).isdigit():
                return player_mv
            
        print("Please enter a valid number")
        

def get_computer_move(cmp,player):
    


    avilable_moves = []
    for move in range(1,10):

        board_copy = copy.deepcopy(board)
        board_place_copy = { 1:board_copy[0][0], 2:board_copy[0][1], 3:board_copy[0][2],
                            4:board_copy[1][0], 5:board_copy[1][1], 6:board_copy[1][2],
                            7:board_copy[2][0], 8:board_copy[2][1], 9:board_copy[2][2]}
        

        if str(board_place_copy[move][0]).isdigit():
            avilable_moves.append(move)
            place_in_board(board_place_copy,move,cmp)
            if check_for_win(board_copy,for_comp=True):
                print("winnig move")
                return move
            


    for move in range(1,10):

        board_copy = copy.deepcopy(board)
        board_place_copy = { 1:board_copy[0][0], 2:board_copy[0][1], 3:board_copy[0][2],
                            4:board_copy[1][0], 5:board_copy[1][1], 6:board_copy[1][2],
                            7:board_copy[2][0], 8:board_copy[2][1], 9:board_copy[2][2]}

        if str(board_place_copy[move][0]).isdigit():
            place_in_board(board_place_copy,move,player)
            if check_for_win(board_copy,for_comp=True):
                print("defending move")
                return move
            board_copy = copy.deepcopy(board)
        board_place_copy = { 1:board_copy[0][0], 2:board_copy[0][1], 3:board_copy[0][2],
                            4:board_copy[1][0], 5:board_copy[1][1], 6:board_copy[1][2],
                            7:board_copy[2][0], 8:board_copy[2][1], 9:board_copy[2][2]}
    print("Avilable moves")

    return random.choice(avilable_moves)

def check_for_win(board_to_check,obj="",for_comp = False):
    for i in range(0,3):
        if  board_to_check[0][i][0] == board_to_check[1][i][0] == board_to_check[2][i][0]:
            if for_comp:
                return True
            print_board(board_to_check)
            print(f"{obj} won")
            reset()
            return None
        
        if board_to_check[i][0][0] == board_to_check[i][1][0] == board_to_check[i][2][0]:
            if for_comp:
                return  True
            
            print_board(board_to_check)
            print(f"{obj} won")
            reset()
            return None
            

    if board_to_check[0][0][0] == board_to_check[1][1][0] == board_to_check[2][2][0] or board_to_check[0][2][0] == board_to_check[1][1][0] == board_to_check[2][0][0]:
        if for_comp:
            return True
        print_board(board_to_check)
        print(f"{obj} won")
        reset()
        return None

    for i in range(0,3):
        for j in range(0,3):
            if str(board_to_check[i][j][0]).isdigit():
                return False
            
    print_board(board_to_check)
    print("It's a draw")
    reset()
    return None

def reset():
    global board,board_place
    board = [[[1], [2], [3]],
            [[4], [5], [6]],
            [[7], [8], [9]]]

    board_place = { 1:board[0][0], 2:board[0][1], 3:board[0][2],
                    4:board[1][0], 5:board[1][1], 6:board[1][2],
                    7:board[2][0], 8:board[2][1], 9:board[2][2]}
    
    main()


def place_in_board(board_place,box_no,obj):
    board_place[box_no][0] = obj

def print_board(board):
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j][0], end = " ")
        print("")

main()
