import unittest
from src.player import Player
from src.card import Card
from src.deck import Deck

class WarGame():
    def __init__(self, player1: Player, player2: Player) -> None:
        self.player1 = player1
        self.player2 = player2
        self.iteration = 1

    def play(self) -> str:
        while True:
            assert len(self.player1.hand) + len(self.player1.winnings) + len(self.player2.hand) + len(self.player2.winnings) == 52, "The total number of cards in the game is not 52."
            card1 = self.player1.play()
            card2 = self.player2.play()

            if card1 is None and card2 is None:
                return "It's a draw!"
            elif card1 is None:
                return "Player 2 wins!"
            elif card2 is None:
                return "Player 1 wins!"

            if card1.rank > card2.rank:
                self.player1.pickupCards([card1, card2])
            elif card2.rank > card1.rank:
                self.player2.pickupCards([card1, card2])
            else: # War
                self.war(player1Cards = [card1, self.player1.play(), self.player1.play(), self.player1.play()], player2Cards = [card2, self.player2.play(), self.player2.play(), self.player2.play()])

            if self.iteration == 1_000_000:
                return "It's a draw!"
            
            self.iteration += 1
            
    def war(self, player1Cards: list[Card], player2Cards: list[Card]) -> None:
        player1RemoveNone = [card for card in player1Cards if isinstance(card, Card)]
        player2RemoveNone = [card for card in player2Cards if isinstance(card, Card)]
        
        if len(player1RemoveNone) == 0 and len(player2RemoveNone) == 0:
            return
        elif len(player1RemoveNone) == 0:
            self.player2.pickupCards(player1RemoveNone + player2RemoveNone)
            return
        elif len(player2RemoveNone) == 0:
            self.player1.pickupCards(player1RemoveNone + player2RemoveNone)
            return

        player1WarCard = player1RemoveNone[-1]
        player2WarCard = player2RemoveNone[-1]

        if player1WarCard.rank > player2WarCard.rank:
            self.player1.pickupCards(player1RemoveNone + player2RemoveNone)
        elif player2WarCard.rank > player1WarCard.rank:
            self.player2.pickupCards(player1RemoveNone + player2RemoveNone)
        else:
            self.iteration += 1
            self.war(
                player1Cards = player1RemoveNone + [self.player1.play(), self.player1.play(), self.player1.play(), self.player1.play()], 
                player2Cards = player2RemoveNone + [self.player1.play(), self.player2.play(), self.player2.play(), self.player2.play()]
            )

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    player1 = Player(name = "Player One", hand = deck.cards[:26])
    player2 = Player(name = "Player Two", hand = deck.cards[26:])

    game = WarGame(player1, player2)
    game.play()