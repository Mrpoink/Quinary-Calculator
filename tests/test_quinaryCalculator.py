import unittest
from src import quinaryCalculator as gc


class TestQuinaryCalculatorOperations(unittest.TestCase):

    def test_calculatorAddition(self):
        self.assertEqual('20', gc.quinaryCalculator("12 + 3"))

    def test_calculatorDivisionONE(self):
        self.assertEqual('13', gc.quinaryCalculator("432/24"))

    def test_calculatorDivisionZERO(self):
        self.assertEqual('0', gc.quinaryCalculator("1/4"))

    def test_calculatorSubtractPOS(self):
        self.assertEqual('10', gc.quinaryCalculator("22 - 12"))

    def test_calculatorSubtractNEG(self):
        self.assertEqual('-10', gc.quinaryCalculator("12 - 22"))

    def test_calculatorMultiply(self):
        self.assertEqual('4', gc.quinaryCalculator("1 * 4"))

    def test_calculatorSquare(self):
        self.assertEqual('1134', gc.quinaryCalculator("23^2"))

    def test_calculatorSquareRoot(self):
        self.assertEqual('2', gc.quinaryCalculator("√4"))


if __name__ == "__main__":
    unittest.main()
