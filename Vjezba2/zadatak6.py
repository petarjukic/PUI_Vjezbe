
def rezultat(broj, lista):
    if(not lista):
        if(broj == 0):
            return True
        return False
        
    
    if(rezultat(broj + lista[0], lista[1:])):
        return True

    
    if(rezultat(broj - lista[0], lista[1:])):
        return True
   
    return False


def main():
    lista = [ 1, 4, 5, 3 ]
    
    print(rezultat(0, lista))


main()
