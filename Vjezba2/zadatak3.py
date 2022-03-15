
def binSearch(lista, element, start=0, end=-1):
    if(end == -1):
        end = len(lista)
    
    if(start >= end):
        return "Element ne postoji u listi"
    
    mid = (start + end) // 2
    
    if(element == lista[mid]):
        return "Element je u listi na poziciji", mid
    elif(element < lista[mid]):
        return binSearch(lista, element, start, mid)
    elif(element > lista[mid]):
        return binSearch(lista, element, mid + 1, end)
    

def main():
    lista = [1, 2, 5, 6, 7, 9]

    print(binSearch(lista, 5))


main()
