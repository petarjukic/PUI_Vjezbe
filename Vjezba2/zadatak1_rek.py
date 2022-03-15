
def count(lista, funk):
    if(len(lista) != 0):
        if(funk(lista[0])):
            return 1 + count(lista[1:], funk)
        else:
            return 0 + count(lista[1:], funk)
    else:
        return 0
    
def predikat(ime):
    if(ime == "ante"):
        return True
    return False

def main():
    lista = ["ante", "petar", "ante", "marko", "jure", "ante"]

    print("Broj elemenata koji zadovoljavaju uvjet ", count(lista, predikat))


main()