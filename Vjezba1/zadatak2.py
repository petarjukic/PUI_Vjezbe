
def checkSize(firstNumber, secondNumber):
    if(len(firstNumber) != len(secondNumber)):
        return False
    return True


def chechNumbers(firstNumber, secondNumber):
    strSortedFirst = sorted(str(firstNumber))
    strSortedSecond = sorted(str(secondNumber))

    if(not checkSize(strSortedFirst, strSortedSecond)):
        return "Nisu iste velicine"

    for i in range(len(strSortedFirst)):
        if(strSortedFirst[i] != strSortedSecond[i]):
            return "Brojevi nisu isti"

    return "Brojevi su isti"

def main():
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))

    print(chechNumbers(firstNumber, secondNumber))


main()