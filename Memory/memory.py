import tkinter as tk
from tkinter import messagebox
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.difficulty = "easy"
        self.sequence = []
        self.shuffled = []
        self.user_guess = []

        self.label = tk.Label(root, text="Select difficulty:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.diff_frame = tk.Frame(root)
        self.diff_frame.pack()
        for level in ["easy", "medium", "hard"]:
            tk.Button(self.diff_frame, text=level.capitalize(),
                      command=lambda l=level: self.startGame(l), width=10).pack(side=tk.LEFT, padx=5)

        self.display_frame = tk.Frame(root)
        self.button_frame = tk.Frame(root)
        self.guess_frame = tk.Frame(root)
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.checkGuess, state=tk.DISABLED)

    def generateSequence(self):
        if self.difficulty == 'easy':
            return random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4)
        elif self.difficulty == 'medium':
            return random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 6)
        elif self.difficulty == 'hard':
            return random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*", 8)

    def startGame(self, level):
        self.difficulty = level
        self.sequence = self.generateSequence()
        self.user_guess = []

        self.label.config(text="Memorize this sequence:")
        self.display_frame.pack(pady=10)
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        for char in self.sequence:
            tk.Label(self.display_frame, text=char, font=("Arial", 18)).pack(side=tk.LEFT, padx=5)

        self.root.after(3000, self.showButtons)

    def showButtons(self):
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        self.label.config(text="Click buttons in the original order:")
        self.shuffled = self.sequence.copy()
        random.shuffle(self.shuffled)

        self.button_frame.pack()
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        for char in self.shuffled:
            tk.Button(self.button_frame, text=char, font=("Arial", 14),
                      command=lambda c=char: self.selectChar(c), width=4).pack(side=tk.LEFT, padx=2)

        self.guess_frame.pack(pady=10)
        for widget in self.guess_frame.winfo_children():
            widget.destroy()
        self.guess_label = tk.Label(self.guess_frame, text="", font=("Arial", 16))
        self.guess_label.pack()

        self.submit_button.pack(pady=10)
        self.submit_button.config(state=tk.NORMAL)

    def selectChar(self, char):
        if len(self.user_guess) < len(self.sequence):
            self.user_guess.append(char)
            self.updateGuessDisplay()

    def updateGuessDisplay(self):
        self.guess_label.config(text="Your guess: " + " ".join(self.user_guess))

    def checkGuess(self):
        if self.user_guess == self.sequence:
            messagebox.showinfo("Correct!", "🎉 You remembered the sequence correctly!")
        else:
            messagebox.showwarning("Wrong!", "❌ That's not correct. Try again!")
        self.resetGame()

    def resetGame(self):
        self.label.config(text="Select difficulty:")
        self.submit_button.config(state=tk.DISABLED)
        self.button_frame.pack_forget()
        self.guess_frame.pack_forget()
        self.display_frame.pack_forget()
        self.user_guess = []


if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
