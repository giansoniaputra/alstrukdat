import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()

# Contoh penggunaan
class CardGame:
    def __init__(self):
        self.deck = Deck()

    def start_game(self):
        print("Welcome to Card Game!")
        self.deck.shuffle()
        print("Shuffling the deck...")
        self.play()

    def play(self):
        print("Dealing the cards...")
        while True:
            card = self.deck.deal_card()
            if card is None:
                print("No more cards in the deck. Game over.")
                break
            print(f"Dealt card: {card}")

# Contoh permainan
game = CardGame()
game.start_game()