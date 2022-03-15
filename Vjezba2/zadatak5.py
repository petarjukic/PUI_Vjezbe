

def kombinacije(s, velicina):
    if len(s) == velicina:
        return [s]
        
    else:
        return kombinacije(s + "A", velicina) + kombinacije(s + "B", velicina) + kombinacije(s + "C", velicina)
    

def main():
    velicina = 3
    print(kombinacije("", velicina))


main()
