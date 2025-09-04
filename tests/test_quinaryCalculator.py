import unittest
from src import quinaryCalculator as gc

class TestQuinaryCalculatorOperations(unittest.TestCase):

    def test_calculatorAddition(self):
        self.assertEqual(20, gc.quinaryCalculator("12 + 3"))

    def test_calculatorDivisionONE(self):
        self.assertEqual(4, gc.quinaryCalculator("4/1"))

    def test_calculatorDivisionZERO(self):
        self.assertEqual(0, gc.quinaryCalculator("1/4"))

    def test_calculatorSubtractPOS(self):
        self.assertEqual(1, gc.quinaryCalculator("2 - 1"))

    def test_calculatorSubtractNEG(self):
        self.assertEqual(-1, gc.quinaryCalculator("1 - 2"))

    def test_calculatorSubtractPOS1(self):
        self.assertEqual(2, gc.quinaryCalculator("3 - 1"))

    def test_calculatorSubtractNEG1(self):
        self.assertEqual(-2, gc.quinaryCalculator("1 - 3"))

    def test_calculatorMultiply(self):
        self.assertEqual(4, gc.quinaryCalculator("1 * 4"))

    def test_calculatorSquare(self):
        self.assertEqual(1034, gc.quinaryCalculator("22^2"))

    def test_calculatorSquareRoot(self):
        self.assertEqual(2, gc.quinaryCalculator("√4"))
    
    def test_calculatorDecimalError(self):
        self.assertEqual('Error', gc.quinaryCalculator("√3"))


if __name__ == "__main__":
    unittest.main()
