import unittest

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

class Card:
    def __init__(self, suit: str, rank: int) -> None:
        assert rank >= 2 and rank <= 14, "Rank must be between 2 and 14"
        assert suit in SUITS, "Invalid suit"

        self.suit: str = suit
        self.rank: int = rank
        self.rank_name: str = self.get_rank_name()

    def __repr__(self) -> str:
        return f"{self.rank_name} of {self.suit}"

    def get_rank_name(self) -> str:
        if self.rank == 11:
            return "Jack"
        elif self.rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"
        elif self.rank == 14:
            return "Ace"
        else:
            return str(self.rank)

class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card('Hearts', 10)
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(card.rank, 10)
        self.assertEqual(str(card), '10 of Hearts')

    def test_card_representation(self):
        card = Card('Spades', 14)
        self.assertEqual(repr(card), 'Ace of Spades')

    def test_invalid_rank(self):
        with self.assertRaises(AssertionError):
            card = Card('Diamonds', 15)

    def test_invalid_suit(self):
        with self.assertRaises(AssertionError):
            card = Card('Stars', 10)

if __name__ == '__main__':
    unittest.main()
