from random import randint


class Igrac:
    def __init__(self, ime):
        self.ime = ime

    def akcija(self, stanje_igre):
        index_karte = randint(0, len(stanje_igre["ruka"] ) - 1)
        for key, value in stanje_igre.items():
            if(key == "ruka"): 
                odabrana_karta = value[index_karte]
                value.pop(index_karte)
                return odabrana_karta
        

if __name__ == "__main__":
    igrac2 = Igrac("igrac2")
    