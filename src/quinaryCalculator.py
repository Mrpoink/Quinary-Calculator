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
    
    elif "^2" in expression:
        firstNumber = [x.strip() for x in expression.split("^2")]
        output = quinarySquare(firstNumber[0])
    
    elif "√" in expression:
        firstNumber = [x.strip() for x in expression.split("√")]
        output = quinarySquareRoot(firstNumber[1])


    return output


def quinaryAddition(firstNumber,secondNumber):
    """
    Takes in two numbers in Quinary, converts
    them to decimal, then adds them together and 
    returns the anwser in Quinary
    """

    return convertDecimalToQuinary(int(firstNumber) + int(secondNumber))


def quinarySubtraction(firstNumber,secondNumber):
    """
    Takes in two numbers in Quinary, converts
    them to decimal, then subtracts them and 
    returns the anwser in Quinary
    """

    return convertDecimalToQuinary(int(firstNumber) - int(secondNumber))


def quinaryMultiplication(firstNumber,secondNumber):
    """
    Takes in two numbers in Quinary, converts
    them to decimal, then multiplies them and 
    returns the anwser in Quinary
    """

    return convertDecimalToQuinary(int(firstNumber) * int(secondNumber))


def quinaryDivision(firstNumber,secondNumber):
    """
    Takes in two numbers in Quinary, converts
    them to decimal, then divides them and 
    returns the anwser in Quinary
    """

    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)

    initialNumber = firstNumber / secondNumber

    total = ''

    if initialNumber < 1:

        remainder = firstNumber

        for i in range(4):

            firstNumber = remainder * 5
            quotient, remainder = divmod(firstNumber, secondNumber)
            total = total + str(int(quotient))

        return float( '0' + '.' + total)

    else:

        decimal_halves = str(initialNumber).split('.')

        integer = convertDecimalToQuinary(int(decimal_halves[0]))
        fractal = convertDecimalToQuinary(int(decimal_halves[1]))

        return float(str(integer) + '.' + str(fractal))


def quinarySquare(firstNumber):
    """
    Takes in a number in in Quinary, converts
    them to decimal, then squares it and returns
    the anwser in quinary. 
    """
    firstNumberConverted = convertDecimalToQuinary(int(firstNumber) ** 2)

    return firstNumberConverted


def quinarySquareRoot(firstNumber):
    """
    Takes in a number in in Quinary, converts
    them to decimal, then find the square root and returns
    the anwser in quinary. 
    """

    return convertDecimalToQuinary(int(firstNumber) ** (1/2))


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

    negative = False
    quotient = 1
    initial_num = int(initialNumber)
    convertedNumber = ''

    if int(initialNumber) < 0:
        negative = True
        initial_num = int(initialNumber) * -1

    while not (quotient <= 0):

        quotient, remainder = divmod(initial_num, 5)

        convertedNumber = convertedNumber + str(remainder)

        initial_num = quotient

    convertedNumber = int(convertedNumber[::-1])

    if negative == True:
        convertedNumber = convertedNumber * -1
    
    return convertedNumber
