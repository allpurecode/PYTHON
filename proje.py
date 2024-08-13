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

import csv


class Student:
    def __init__(self, roll):
        self.dbReader = csv.reader(file)

    def getdetail(self, roll):
        def search(ele):
            if ele[2] == roll:
                return ele

        data = list(self.dbReader)
        mydata = list(filter(search, data))
        return mydata[0]

    def displaydetails(self):
        details = self.getdetail(self.rollNumber)
        print(details)


class Faculty(Student):
    def __init__(self):
        super().__init__()

    def addStudent(self):
        pass

    def updateStudent(self):
        pass

Fac=Faculty()
res=Fac.getdetail()