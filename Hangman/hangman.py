import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# Define word list
WORDS = {
    "easy": ['cat', 'dog', 'hat', 'car', 'sun'],
    "medium": ['apple', 'robot', 'light', 'sensor', 'train'],
    "hard": ['automation', 'microscope', 'television', 'controller', 'processor']
}

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game with PNGs")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.image_folder = "images"
        self.hangman_images = [ImageTk.PhotoImage(Image.open(os.path.join(self.image_folder, f"hangman{i}.png")).resize((200, 200))) for i in range(8)]
        self.difficulty = None
        self.setupStartScreen()

    def setupStartScreen(self):
        self.clear_screen()
        tk.Label(self.root, text="Select Difficulty", font=("Helvetica", 18)).pack(pady=20)
        for level in ['easy', 'medium', 'hard']:
            tk.Button(self.root, text=level.capitalize(), font=("Helvetica", 14),
                      command=lambda l=level: self.startGame(l)).pack(pady=5)

    def startGame(self, difficulty):
        self.difficulty = difficulty
        self.word = random.choice(WORDS[difficulty])
        self.correct_letters = set(self.word)
        self.display_word = ['_' for _ in self.word]
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_attempts = 7
        self.setupGameScreen()

    def setupGameScreen(self):
        self.clear_screen()

        # Hangman image display
        self.image_label = tk.Label(self.root, image=self.hangman_images[self.wrong_guesses])
        self.image_label.pack(pady=10)

        # Word display
        self.word_label = tk.Label(self.root, text=' '.join(self.display_word), font=("Helvetica", 24))
        self.word_label.pack(pady=10)

        # Alphabet buttons
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()
        for i, letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            btn = tk.Button(self.buttons_frame, text=letter, width=4, font=("Helvetica", 14),
                            command=lambda l=letter: self.guessLetter(l.lower()))
            btn.grid(row=i // 9, column=i % 9, padx=2, pady=2)

    def guessLetter(self, letter):
        if letter in self.guessed_letters:
            return
        self.guessed_letters.add(letter)

        if letter in self.correct_letters:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.display_word[i] = letter
            self.word_label.config(text=' '.join(self.display_word))
            if set(self.display_word) == self.correct_letters:
                self.endGame(win=True)
        else:
            self.wrong_guesses += 1
            self.image_label.config(image=self.hangman_images[self.wrong_guesses])
            if self.wrong_guesses >= self.max_attempts:
                self.endGame(win=False)

    def endGame(self, win):
        for child in self.buttons_frame.winfo_children():
            child.config(state="disabled")

        result_text = "🎉 You won!" if win else f"💀 You lost! The word was '{self.word}'"
        tk.Label(self.root, text=result_text, font=("Helvetica", 16)).pack(pady=20)

        tk.Button(self.root, text="Play Again", font=("Helvetica", 14),
                  command=self.setupStartScreen).pack(pady=5)
        tk.Button(self.root, text="Exit", font=("Helvetica", 14),
                  command=self.root.quit).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
