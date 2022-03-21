import unittest
import tynerpond

file = open('tyner.txt', 'r', encoding='utf-8')

class TynerTest(unittest.TestCase):

    def test_regex_list_length(self):
        result = tynerpond.regex(file)
        self.ass
