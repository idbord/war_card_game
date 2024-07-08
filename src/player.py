import unittest
import random
from src.card import Card
from src.deck import Deck

class Player():
    def __init__(self, name: str, hand: list[Card]) -> None:
        self.name = name
        self.hand = hand
        self.winnings = []

    def play(self) -> Card:
        if len(self.hand) == 0 and len(self.winnings) == 0:
            return None
        elif len(self.hand) == 0 and len(self.winnings) > 0:
            self.hand = self.winnings.copy()
            self.winnings.clear()
            self.shuffleHand()
        
        return self.hand.pop()

    def shuffleHand(self) -> None:
        random.shuffle(self.hand)

    def pickupCards(self, cards) -> None:
        self.winnings.extend(filter(lambda card: isinstance(card, Card), cards))

        if len(self.hand) == 0:
            self.hand = self.winnings.copy()
            self.winnings.clear()
            self.shuffleHand()



class TestPlayer(unittest.TestCase):
    def test_playing_card(self):
        deck = Deck()
        deck.shuffle()

        player = Player(name = "Random Name", hand = deck.cards[:len(deck) // 2])
        self.assertEqual(len(player.hand), 26)
        cardPlayed = player.play()
        self.assertEqual(len(player.hand), 25)
        self.assertIsInstance(cardPlayed, Card)
    
    def test_shuffling_hand(self):
        deck = Deck()
        deck.shuffle()

        player = Player(name = "Random Name", hand = deck.cards[:len(deck) // 2])
        handBeforeShuffle = player.hand.copy()
        player.shuffleHand()
        self.assertNotEqual(handBeforeShuffle, player.hand)

    def test_empty_hand(self):
        deck = Deck()
        deck.shuffle()

        player = Player(name = "Random Name", hand = deck.cards[:len(deck) // 2])
        for _ in range(25):
            player.play()
        
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(len(player.winnings), 0)
        lastCard = player.play()
        self.assertEqual(len(player.hand), 0)
        self.assertEqual(len(player.winnings), 0)

    def test_pickup_cards(self):
        deck = Deck()
        deck.shuffle()

        player = Player(name = "Random Name", hand = deck.cards[:len(deck) // 2])
        player.pickupCards(deck.cards[len(deck) // 2:])
        self.assertEqual(len(player.hand), 26)
        self.assertEqual(len(player.winnings), 26)

        for _ in range(27):
            player.play()
        
        self.assertEqual(len(player.hand), 25)
        self.assertEqual(len(player.winnings), 0)

if __name__ == '__main__':
    unittest.main()