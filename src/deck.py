import unittest
import random
from src.card import Card, SUITS

class Deck:
    def __init__(self) -> None:
        self.cards = []
        for suit in SUITS:
            for rank in range(2, 15):
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

class TestDeck(unittest.TestCase):
    def test_deck_creation(self):
        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_deck_deal(self):
        deck = Deck()
        card = deck.deal()
        self.assertEqual(len(deck), 51)
        self.assertIsInstance(card, Card)

    def test_deck_shuffle(self):
        deck = Deck()
        original_cards = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_cards)

    def test_deck_empty(self):
        deck = Deck()
        for _ in range(52):
            deck.deal()
        self.assertEqual(len(deck), 0)
        with self.assertRaises(IndexError):
            deck.deal()

if __name__ == '__main__':
    unittest.main()
