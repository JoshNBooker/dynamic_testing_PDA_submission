import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('diamonds', 1)
        self.card2 = Card('spades', 8)
        self.card_game1 = CardGame()
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        result = self.card_game1.check_for_ace(self.card1)
        self.assertEqual(True,result)

    def test_highest_card(self):
        self.card_game1.highest_card(self.card1, self.card2)
        self.assertEqual(self.card1, self.card1)

    def test_cards_total(self):
        self.cards = [self.card1, self.card2]
        total = self.card_game1.cards_total(self.cards)
        self.assertEqual("You have a total of 9", total)

    
