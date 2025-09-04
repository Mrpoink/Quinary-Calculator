def quinaryCalculator(expression):
    output = None
    if "+" in expression:
        firstNumber, secondNumber = [x.strip() for x in expression.split("+")]
        output = quinaryAddition(firstNumber, secondNumber)
    elif "-" in expression:
        firstNumber, secondNumber = [x.strip() for x in expression.split("-")]
        output = quinarySubtraction(firstNumber, secondNumber)
    elif "*" in expression:
        firstNumber, secondNumber = [x.strip() for x in expression.split("*")]
        output = quinaryMultiplication(firstNumber, secondNumber)
    elif "/" in expression:
        firstNumber, secondNumber = [x.strip() for x in expression.split("/")]
        output = quinaryDivision(firstNumber, secondNumber)
    elif "^2" in expression:
        firstNumber = [x.strip() for x in expression.split("^2")]
        output = quinarySquare(firstNumber[0])
    elif "√" in expression:
        firstNumber = [x.strip() for x in expression.split("√")]
        output = quinarySquareRoot(firstNumber[1])
    return output


def quinaryAddition(firstNumber, secondNumber):
    return convertDecimalToQuinary(
        convertQuinaryToDecimal(firstNumber) + convertQuinaryToDecimal(secondNumber)
    )


def quinarySubtraction(firstNumber, secondNumber):
    return convertDecimalToQuinary(
        convertQuinaryToDecimal(firstNumber) - convertQuinaryToDecimal(secondNumber)
    )


def quinaryMultiplication(firstNumber, secondNumber):
    return convertDecimalToQuinary(
        convertQuinaryToDecimal(firstNumber) * convertQuinaryToDecimal(secondNumber)
    )


def quinaryDivision(firstNumber, secondNumber):
    a = convertQuinaryToDecimal(firstNumber)
    b = convertQuinaryToDecimal(secondNumber)
    if b == 0:
        return "Error"
    if a % b != 0:
        return "Error"
    return convertDecimalToQuinary(a // b)


def quinarySquare(firstNumber):
    num = convertQuinaryToDecimal(firstNumber)
    return convertDecimalToQuinary(num ** 2)


def quinarySquareRoot(firstNumber):
    num = convertQuinaryToDecimal(firstNumber)
    root = int(num ** 0.5)
    if root * root != num:
        return "Error"
    return convertDecimalToQuinary(root)


def convertQuinaryToDecimal(initialNumber):
    quotient = int(initialNumber)
    convertedNumber = 0
    exponent = 0
    while quotient != 0:
        convertedNumber += (pow(5, exponent) * (quotient % 10))
        quotient = quotient // 10
        exponent += 1
    return convertedNumber


def convertDecimalToQuinary(initialNumber):
    negative = False
    quotient = 1
    initial_num = int(initialNumber)
    convertedNumber = ''
    if initial_num < 0:
        negative = True
        initial_num = abs(initial_num)
    while not (quotient <= 0):
        quotient, remainder = divmod(initial_num, 5)
        convertedNumber = convertedNumber + str(remainder)
        initial_num = quotient
    convertedNumber = int(convertedNumber[::-1])
    if negative:
        convertedNumber = -convertedNumber
    return convertedNumber

