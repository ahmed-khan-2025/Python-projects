import tkinter as tk
import random

# Card values dictionary
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Create deck
def createDeck():
    ranks = list(card_values.keys())
    suits = ['♠', '♥', '♦', '♣']
    deck = [rank + suit for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Score calculator
def calculateScore(hand):
    score = sum(card_values[card[:-1]] for card in hand)
    aces = sum(1 for card in hand if card.startswith('A'))
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

# Game class
class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.deck = createDeck()
        self.player_hand = []
        self.computer_hand = []

        # Labels
        self.player_label = tk.Label(root, text="Player: ", font=('Arial', 14))
        self.player_label.pack()
        self.player_cards = tk.Label(root, text="", font=('Arial', 12))
        self.player_cards.pack()

        self.computer_label = tk.Label(root, text="Computer: ", font=('Arial', 14))
        self.computer_label.pack()
        self.computer_cards = tk.Label(root, text="", font=('Arial', 12))
        self.computer_cards.pack()

        self.status_label = tk.Label(root, text="", font=('Arial', 14), fg="blue")
        self.status_label.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.hit_button = tk.Button(self.button_frame, text="Hit", width=10, command=self.hit)
        self.hit_button.grid(row=0, column=0, padx=10)

        self.stand_button = tk.Button(self.button_frame, text="Stand", width=10, command=self.stand)
        self.stand_button.grid(row=0, column=1, padx=10)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart)
        self.restart_button.pack(pady=5)

        self.startGame()

    def startGame(self):
        self.deck = createDeck()
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.computer_hand = [self.deck.pop(), self.deck.pop()]
        self.updateDisplay()

    def updateDisplay(self, reveal=False):
        player_text = f"{', '.join(self.player_hand)} (Total: {calculateScore(self.player_hand)})"
        self.player_cards.config(text=player_text)

        if reveal:
            comp_text = f"{', '.join(self.computer_hand)} (Total: {calculateScore(self.computer_hand)})"
        else:
            comp_text = f"{self.computer_hand[0]}, ?"
        self.computer_cards.config(text=comp_text)

    def hit(self):
        self.player_hand.append(self.deck.pop())
        self.updateDisplay()
        score = calculateScore(self.player_hand)
        if score > 21:
            self.endGame("You busted! Computer wins.")

    def stand(self):
        while calculateScore(self.computer_hand) < 17:
            self.computer_hand.append(self.deck.pop())
        self.updateDisplay(reveal=True)

        player_score = calculateScore(self.player_hand)
        computer_score = calculateScore(self.computer_hand)

        if computer_score > 21:
            self.endGame("Computer busted! You win.")
        elif computer_score > player_score:
            self.endGame("Computer wins.")
        elif player_score > computer_score:
            self.endGame("You win!")
        else:
            self.endGame("It's a tie!")

    def endGame(self, message):
        self.status_label.config(text=message)
        self.hit_button.config(state="disabled")
        self.stand_button.config(state="disabled")
        self.updateDisplay(reveal=True)

    def restart(self):
        self.status_label.config(text="")
        self.hit_button.config(state="normal")
        self.stand_button.config(state="normal")
        self.startGame()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()
