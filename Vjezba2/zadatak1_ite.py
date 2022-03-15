
from sqlalchemy import true


def count(lista, funk):
    counter = 0
    for ime in lista:
        if(funk(ime)):
            counter += 1
        
    return count

def predikat(ime):
    if(ime == "ante"):
        return True
    
    return False


def main():
    lista = ["ante", "petar", "ante", "marko", "jure", "ante"]

    print("Broj elemenata koji zadovoljavaju uvjet ", count(lista, predikat))


main()