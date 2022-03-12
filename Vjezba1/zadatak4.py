
from random import randint


def checkRange(secretNumber):
    if(secretNumber >= 0 and secretNumber < 1000):
        return True
    return False

def main():
    secretNumber = int(input("Unesi broj izmedu 0 i 999: "))
    print(secretNumber)
    minNum = 0
    maxNum = 999

    while(checkRange(secretNumber) != True):
        print("Unos je pogresan")
        secretNumber = int(input("Unesi broj izmedu 0 i 999: "))

    while True:
        computerNumber = randint(minNum, maxNum)
        print(computerNumber)
        
        if(secretNumber == computerNumber):
            print("Broj je pogoden")
            break
        
        hint = input("Je li trenutni broj veci ili manji od zadanog? ")

        if(hint.lower() == "veci"):
            maxNum = computerNumber
        elif(hint.lower() == "manji"):
            minNum = computerNumber
        else:
            print("Pogresan unos")


main()