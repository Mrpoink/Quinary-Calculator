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
    firstNumberConverted = convertQuinaryToDecimal(firstNumber)
    secondNumberConverted = convertQuinaryToDecimal(secondNumber)

    return convertDecimalToQuinary(firstNumberConverted // secondNumberConverted)


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
    initial_str = str(initialNumber).strip()
    
    negative = initial_str.startswith('-')
    if negative:
        initial_str = initial_str[1:]

    convertedNumber = 0
    exponent = 0
    for digit in reversed(initial_str):
        if digit not in "01234":
            return "Error"
        convertedNumber += int(digit) * (5 ** exponent)
        exponent += 1


    if negative: 
        return -convertedNumber
    else:
        return convertedNumber


def convertDecimalToQuinary(initialNumber):
    if initialNumber == 0:
        return "0"

    initial_num = abs(int(initialNumber))
    digits = []

    while initial_num > 0:
        initial_num, remainder = divmod(initial_num, 5)
        digits.append(str(remainder))

    quinary = ''.join(reversed(digits))
    
    if(initialNumber < 0):
        return ('-' + quinary)
    else:
        return quinary

