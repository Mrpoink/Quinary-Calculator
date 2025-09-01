def quinaryCalculator(expression):
    """
    Takes a string in the format a + b. Returns
    the appropriate quinary calculation.
    """
    output = None

    if "+" in expression:
        firstNumber, secondNumber = [x.strip() for x in expression.split("+")]
        output = quinaryAddition(firstNumber,secondNumber)
    
    elif "-" in expression:
        firstNumber, secondNumber = [x.strip() for x in expression.split("-")]
        output = quinarySubtraction(firstNumber,secondNumber)
    
    elif "*" in expression:
        firstNumber, secondNumber = [x.strip() for x in expression.split("*")]
        output = quinaryMultiplication(firstNumber,secondNumber)
    
    elif "/" in expression:
        firstNumber, secondNumber = [x.strip() for x in expression.split("/")]
        output = quinaryDivision(firstNumber,secondNumber)

    return output


def quinaryAddition(firstNumber,secondNumber):
    """
    Takes in two numbers in Quinary, converts
    them to decimal, then adds them together and 
    returns the anwser in Quinary
    """
    firstNumberConverted = convertQuinaryToDecimal(firstNumber)
    secondNumberConverted = convertQuinaryToDecimal(secondNumber)

    return convertDecimalToQuinary(firstNumberConverted + secondNumberConverted)


def quinarySubtraction(firstNumber,secondNumber):
    """
    Takes in two numbers in Quinary, converts
    them to decimal, then subtracts them and 
    returns the anwser in Quinary
    """
    firstNumberConverted = convertQuinaryToDecimal(firstNumber)
    secondNumberConverted = convertQuinaryToDecimal(secondNumber)

    return convertDecimalToQuinary(firstNumberConverted - secondNumberConverted)


def quinaryMultiplication(firstNumber,secondNumber):
    """
    Takes in two numbers in Quinary, converts
    them to decimal, then multiplies them and 
    returns the anwser in Quinary
    """
    firstNumberConverted = convertQuinaryToDecimal(firstNumber)
    secondNumberConverted = convertQuinaryToDecimal(secondNumber)

    return convertDecimalToQuinary(firstNumberConverted * secondNumberConverted)


def quinaryDivision(firstNumber,secondNumber):
    """
    Takes in two numbers in Quinary, converts
    them to decimal, then divides them and 
    returns the anwser in Quinary
    """
    firstNumberConverted = convertQuinaryToDecimal(firstNumber)
    secondNumberConverted = convertQuinaryToDecimal(secondNumber)

    return convertDecimalToQuinary(firstNumberConverted // secondNumberConverted)


def convertQuinaryToDecimal(initialNumber):
    """
    Takes in a quinary number and converts it to decimal
    """
    quotient = int(initialNumber)
    converetdNumber = 0
    exponent = 0

    while quotient != 0:
        converetdNumber += (pow(5,exponent) * (quotient % 10))
        quotient = quotient // 10
        exponent += 1
    
    return converetdNumber


def convertDecimalToQuinary(initialNumber):
    """
    Takes in a decimal number and converts it 
    to Quinary
    """
    quotient = int(initialNumber)
    converetdNumber = ""

    while quotient != 0:
        converetdNumber = str(quotient % 5) + converetdNumber
        quotient = quotient // 5
    
    return converetdNumber



def main():

    assert "430" == quinaryCalculator("243 + 132")
    assert "131" == quinaryCalculator("324 - 143")
    assert "432" == quinaryCalculator("23 * 14")
    assert "13" == quinaryCalculator("432 / 24")


if __name__ == "__main__":
    main()