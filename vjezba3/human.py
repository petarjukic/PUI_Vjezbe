from igrac import Igrac


class Human(Igrac):
    
    def __init__(self, ime):
        self.ime = ime

    def akcija(self, stanje_igre):
        print("Karte u ruci su: ", stanje_igre["ruka"])
        index_karte = int(input("Unesi broj izmedu 0 i 2 za izvuc kartu: "))
        while(index_karte > len(stanje_igre["ruka"]) or index_karte < 0):
            index_karte = int(input("Unesi broj izmedu 0 i 2 za izvuc kartu: "))
        
        for key, value in stanje_igre.items():
            if(key == "ruka"):
                odabrana_karta = value.pop(index_karte)
                return odabrana_karta


if __name__ == "__main__":
    igrac = Human("igrac1")
