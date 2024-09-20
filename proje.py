'''import random
from tkinter import *

# dictionary and variables
s = {
    "rock": {"rock": 1, "paper": 0, "scissors": 2},
    "paper": {"rock": 2, "paper": 1, "scissors": 0},
    "scissors": {"rock": 0, "paper": 2, "scissors": 1}
}
computer_score = 0
player_score = 0


# functions
def outcome_handler(user_choice):
    global computer_score
    global player_score
    outcomes = ["rock", "paper", "scissors"]
    random_number = random.randint(0, 2)
    computer_choice = outcomes[random_number]
    result = s[user_choice][computer_choice]

    player_choice_label.config(fg="red", text="player choice: " + str(user_choice))
    computer_choice_label.config(fg="green", text="computer choice:" + str(computer_choice))

    if result == 2:
        player_score = player_score + 2
        player_score_label.config(text="player:" + str(player_score))
        outcome_label.config(fg="blue", text="outcome : player won")
    elif result == 1:
        player_score = player_score + 1
        computer_score = computer_score + 1
        player_score_label.config(text="player:" + str(player_score))
        computer_score_label.config(text="computer:" + str(computer_score))
        outcome_label.config(fg="blue", text="outcome:Draw")
    elif result == 0:
        computer_score = computer_score + 2
        computer_score_label.config(text="computer: " + str(computer_score))
        outcome_label.config(fg="blue", text="outcome : Computer won ")


# main screen
master = Tk()
master.title("rock_paper_scissors")

# label
Label(master, text="rock, paper, scissors", font=("callibri", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(master, text="please enter the option", font=("callibri", 12)).grid(row=1, sticky=N)
player_score_label = Label(master, text="player : 0", font=("callibri", 12))
player_score_label.grid(row=2, sticky=W)
computer_score_label = Label(master, text="computer : 0", font=("callibri", 12))
computer_score_label.grid(row=2, sticky=E)
player_choice_label = Label(master, font=("callibri", 12))
player_choice_label.grid(row=3, sticky=W)
computer_choice_label = Label(master, font=("callibri", 12))
computer_choice_label.grid(row=3, sticky=E)
outcome_label = Label(master, font=("callbri", 12))
outcome_label.grid(row=3, sticky=N)

# buttons
Button(master, text="rock", width=15, command=lambda: outcome_handler("rock")).grid(row=4, sticky=W, padx=5, pady=5)
Button(master, text="paper", width=15, command=lambda: outcome_handler("paper")).grid(row=4, sticky=N, pady=5)
Button(master, text="scissors", width=15, command=lambda: outcome_handler("scissors")).grid(row=4, sticky=E, padx=5,
                                                                                            pady=5)

# dummy label
Label(master).grid(row=5)
master.mainloop()'''

#-----------------------------------------------------------------------------------------------------------------------------------
# QUEENS
def initialize(n):
    for key in ['queen','row','col','nwtose','swtone']:
        board[key] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1),n):
        board['nwtose'][i] = 0
    for i in range(2*n-1):
        board['swtone'][i] = 0

def printboard():
    for row in sorted(board['queen'].keys()):
        print((row,board['queen'][row]))

def free(i,j):
    return(board['row'][i] == 0 and board['col'][j] == 0 and
           board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)

def addqueen(i,j):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['nwtose'][j-i] = 1
    board['swtone'][j+i] = 1

def undoqueen(i,j):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['nwtose'][j-i] = 0
    board['swtone'][j+i] = 0

def placequeen(i):
    n = len(board['queen'].keys())
    for j in range(n):
        if free(i,j):
            addqueen(i,j)
            if i == n-1:
                return(True)
            else:
                extendsoln = placequeen(i+1)
            if extendsoln:
                return(True)
            else:
                undoqueen(i,j)
    else:
        return(False)

board = {}
n = int(input("How many queens? "))
initialize(n)
if placequeen(0):
    printboard()

# WITH ALL SOLUTIONS
def initialize(n):
    for key in ['queen','row','col','nwtose','swtone']:
        board[key] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1),n):
        board['nwtose'][i] = 0
    for i in range(2*n-1):
        board['swtone'][i] = 0

def printboard():
    for row in sorted(board['queen'].keys()):
        print((row,board['queen'][row]),end=" ")
    print("")

def free(i,j):
    return(board['row'][i] == 0 and board['col'][j] == 0 and
           board['nwtose'][j-i] == 0 and board['swtone'][j+i] == 0)

def addqueen(i,j):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['nwtose'][j-i] = 1
    board['swtone'][j+i] = 1

def undoqueen(i,j):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['nwtose'][j-i] = 0
    board['swtone'][j+i] = 0

def placequeen(i):
    n = len(board['queen'].keys())
    for j in range(n):
        if free(i,j):
            addqueen(i,j)
            if i == n-1:
                printboard()
            else:
                extendsoln = placequeen(i+1)
            undoqueen(i,j)

board = {}
n = int(input("How many queens? "))
initialize(n)
if placequeen(0):
    printboard()

