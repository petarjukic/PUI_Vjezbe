from igrac import Igrac


class Human(Igrac):
    
    def __init__(self, ime):
        self.ime = ime

    def akcija(self, stanje_igre):
        
        index_karte = int(input("Unesi broj izmedu 0 i 2 za izvuc kartu: "))
        while(index_karte > 2 or index_karte < 0):
            index_karte = int(input("Unesi broj izmedu 0 i 2 za izvuc kartu: "))
        
        for key, value in stanje_igre.items():
            if(key == "briskula"):
                print(value, " briskula HUMAN")
            elif(key == "ruka"):
                print(value[index_karte], " Odabrana karta iz ruke")
                value.pop(index_karte)
                return value[index_karte]
            elif(key == "stol"):
                print(value, "Stol")
            elif(key == "dobivene"):
                print(value, "dobivene")
            else:
                print(value, "protivnik")


if __name__ == "__main__":
    igrac = Human("igrac1")
