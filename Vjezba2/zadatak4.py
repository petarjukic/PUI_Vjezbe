
def merge(lista1, lista2):
    if(lista1 == [] or lista1[0] > lista2[0]):
        if(lista2 != []):
            element = lista2.pop(0)
            return [element] + merge(lista1, lista2)
        else:
            return []

    if(lista2 == [] or lista2[0] > lista1[0]):
        if(lista1 != []):
            element = lista1.pop(0)
            return [element] + merge(lista1, lista2)
        else:
            return []


def main():
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4, 6, 8]

    print(merge(lista1, lista2))


main()