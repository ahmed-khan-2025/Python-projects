import tkinter as tk
import random

choices = ["rock", "scissors", "bag"]

def getWinner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "bag") or \
         (player == "bag" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play(player_choice):
    computer_choice = random.choice(choices)
    result = getWinner(player_choice, computer_choice)
    
    result_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}")

    if result == "draw":
        outcome_label.config(text="It's a draw. Try again!")
    elif result == "player":
        outcome_label.config(text="You win!")
        disableButtons()
    else:
        outcome_label.config(text="You lose!")
        disableButtons()

def disableButtons():
    for btn in buttons:
        btn.config(state="disabled")

def restartGame():
    for btn in buttons:
        btn.config(state="normal")
    result_label.config(text="")
    outcome_label.config(text="Choose your move:")

# GUI Setup
root = tk.Tk()
root.title("Rock-Scissors-Bag")
root.geometry("300x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock - Scissors - Bag", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

outcome_label = tk.Label(root, text="Choose your move:", font=("Arial", 12))
outcome_label.pack()

# Buttons for user choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

buttons = []
for choice in choices:
    btn = tk.Button(button_frame, text=choice.capitalize(), width=10, font=("Arial", 12),
                    command=lambda c=choice: play(c))
    btn.pack(side="left", padx=5)
    buttons.append(btn)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

restart_button = tk.Button(root, text="Restart Game", font=("Arial", 10), command=restartGame)
restart_button.pack(pady=5)

root.mainloop()
