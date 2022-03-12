from random import randint

def main():
    generatedNumber = randint(0, 999)
    print(generatedNumber)
    userNumber = 0

    while True:
        userNumber = int(input("Unesi broj: "))

        if(userNumber == generatedNumber):
            print(userNumber)
            return "Broj je pogoden"
        elif(userNumber > generatedNumber):
            print("Broj je manji od unesenog")
        elif(userNumber < generatedNumber):
            print("Boje je veci od unesenog")
    

print(main())