import unittest
from src import quinaryCalculator as gc

class TestQuinaryCalculatorOperations(unittest.TestCase):

    def test_calculatorAddition(self):
        self.assertEqual(30, gc.quinaryCalculator("12 + 3"))

    def test_calculatorDivisionONE(self):
        self.assertEqual(33.0, gc.quinaryCalculator("432/24"))

    def test_calculatorDivisionZERO(self):
        self.assertEqual("Error", gc.quinaryCalculator("1/6"))

    def test_calculatorSubtractPOS(self):
        self.assertEqual(30, gc.quinaryCalculator("27 - 12"))

    def test_calculatorSubtractNEG(self):
        self.assertEqual(-30, gc.quinaryCalculator("12 - 27"))

    def test_calculatorMultiply(self):
        self.assertEqual(11, gc.quinaryCalculator("1 * 6"))

    def test_calculatorSquare(self):
        self.assertEqual(4104, gc.quinaryCalculator("23^2"))

    def test_calculatorSquareRoot(self):
        self.assertEqual(10, gc.quinaryCalculator("√25"))


if __name__ == "__main__":
    unittest.main()
