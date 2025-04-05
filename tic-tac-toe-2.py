import customtkinter as ctk
from functools import partial
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

boxes = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def start_game():
    global root
    root = ctk.CTk()
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    root.title("Tic-Tac-Toe")
    root.resizable(False,False)

    play_with_computer_button = ctk.CTkButton(root, text="Play with Computer", width=250, height=45, corner_radius=20, command=play_with_computer)
    play_with_computer_button.grid(row = 1, column = 2, padx=175,pady = 100)

    play_with_player_button = ctk.CTkButton(root, text="Play with Player", width=250, height=45, corner_radius=20, command=play_with_player)
    play_with_player_button.grid(row = 2, column = 2, padx=175,pady = 0)

    root.mainloop()

def play_with_computer():
    load_game(True)

def load_game(cmp = False):
    for child in root.winfo_children():
        child.destroy()

    for i in range(0, 3):
        for j in range(0, 3):
            box = ctk.CTkButton(root, text = f"", width = 100, height=70, command=partial(button_clicked, i, j, cmp))
            box.grid(row = i, column = j, padx = 50, pady = 10)
            boxes[i][j] = box

    reset_btn = ctk.CTkButton(root, text = f"Reset", width = 150,height=30, command=partial(load_game,cmp))
    reset_btn.grid(row=3, column=1)

    reset_btn = ctk.CTkButton(root, text = f"Back", width = 150,height=30, command=partial(reset,"", boxes))
    reset_btn.grid(row=4,column=1)

def play_with_player():
    load_game()

def button_clicked(i, j, cmp=False):
    if cmp:
        turn = "O"
  
        if boxes[i][j]._text != "":
            return
        boxes[i][j].configure(text = turn)

        win = check_for_win(boxes)
        if win:
            reset("Player won", boxes)
            return
        if win == []:
            reset("It's a draw", boxes)
            return
        
        turn = "X"

        index = get_computer_move(turn)
        boxes[index[0]][index[1]].configure(text = turn)

        win = check_for_win(boxes)
        if win:
            reset("Computer won", boxes)
            return
        return
    
    if not cmp:
        turn = get_turn()

        if boxes[i][j]._text != "":
            return
        boxes[i][j].configure(text = turn)

        win = check_for_win(boxes)
        if win and turn == "X":
            reset("Player1 won",boxes)
            return
        
        if win and turn == "O":
            reset("Player2 won",boxes)
            return
        if win == []:
            reset("It's a draw",boxes)
            return 
                  
def check_for_win(boxes):
    for i in range(0, 3):
        if boxes[0][i]._text == boxes[1][i]._text == boxes[2][i]._text != "":
            return True

        if boxes[i][0]._text == boxes[i][1]._text == boxes[i][2]._text !=  "":
            return True
        
    if boxes[0][0]._text == boxes[1][1]._text == boxes[2][2]._text != "" or boxes[0][2]._text == boxes[1][1]._text == boxes[2][0]._text != "": 
        return True

    for i in range(0, 3):
        for j in range(0 ,3):
            if boxes[i][j]._text == "":
                return False
    return []
      
def reset(text = "", box = ""):
    board = "Board state:\n"
    for i in range(0, 3):
        for j in range(0, 3):
            if box[i][j]._text != "":
                board += f"{box[i][j]._text}  "
            else:
                board += "    "

        board += "\n"
    
    global turn
    turn = "O"
    
    for child in root.winfo_children():
        child.destroy()
    
    play_with_computer_button = ctk.CTkButton(root, text="Play with Computer", width=250, height=45, corner_radius=20, command=play_with_computer)
    play_with_computer_button.grid(row = 1, column = 2, padx=175,pady = 100)

    play_with_player_button = ctk.CTkButton(root, text="Play with Player", width=250, height=45, corner_radius=20, command=play_with_player)
    play_with_player_button.grid(row = 2, column = 2, padx=175,pady = 0)

    ctk.CTkLabel(root, text=text).grid(row = 3 ,column = 2)
    ctk.CTkLabel(root, text=board).grid(row = 4 ,column = 2)

i = 2
def get_turn():
    global i
    if i % 2 == 0:
        i += 1
        return "X"
    
    else:
        i += 1
        return "O"

def get_computer_move(cmp):
    indexes = [0,1,2]
    
    for k in range(0,2):
        available_spaces = []
        for i in indexes:
            for j in indexes:
                boxes_copy = [[[boxes[n][m]._text] for m in range(3)] for n in range(3)]
                if boxes_copy[i][j][0] != "":
                    pass
                else:
                    boxes_copy[i][j][0] = cmp

                    available_spaces.append([i,j])
                    win = check_win(boxes_copy)
                    if win:
                        return [i,j]        
        if cmp == "X":
            cmp = "O"
        else:
            cmp = "X"
    return random.choice(available_spaces)

def check_win(board_to_check):
    for i in range(0,3):
        if  board_to_check[0][i][0] == board_to_check[1][i][0] == board_to_check[2][i][0] != "": 
            return True
        if board_to_check[i][0][0] == board_to_check[i][1][0] == board_to_check[i][2][0] != "":
            return True

    if board_to_check[0][0][0] == board_to_check[1][1][0] == board_to_check[2][2][0] != "" or board_to_check[0][2][0] == board_to_check[1][1][0] == board_to_check[2][0][0] != "": 
        return True
    return None

start_game()


