
def drugiRek(broj, nizSecond):
    if(len(nizSecond) == 0):
        return True
    
    if(broj == nizSecond[0]):
        return True
    
    else:
        nizSecond = nizSecond.replace(nizSecond[0], "")
        return drugiRek(broj, nizSecond)


def check(firstNumber, secondNumber):
    if(len(firstNumber) == 0):
        return True

    if(not drugiRek(firstNumber[0], secondNumber)):
        return False
    
    else:
        firstNumber = firstNumber.replace(firstNumber[0], "")
        return check(firstNumber, secondNumber) 
    


def checkLength(firstNumber, secondNumber):
    if(len(firstNumber) == len(secondNumber)):
        return True

    return False

def main():
    firstNumber = 1124
    secondNumber = 1224
    firstNumber = str(firstNumber)
    secondNumber = str(secondNumber)

    if(checkLength(firstNumber, secondNumber) and check(firstNumber, secondNumber)):
        print("Brojevi su isti")
    else:
        print("Brojevi nisu isti")


main()
