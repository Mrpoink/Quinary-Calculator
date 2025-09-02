import unittest
from src import quinaryCalculator as gc

class TestQuinaryCalculatorOperations(unittest.TestCase):

    def test_calculatorAddition(self):
        self.assertEqual("20", gc.quinaryCalculator("12 + 3"))


if __name__ == "__main__":
    unittest.main()