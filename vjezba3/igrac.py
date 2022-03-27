from random import randint


class Igrac:
    def __init__(self, ime):
        self.ime = ime

    def akcija(self, stanje_igre):
        index_karte = randint(0, 2)
        for key, value in stanje_igre.items():
            if(key == "briskula"):
                print(value, " briskula")
            elif(key == "ruka"):
                odabrana_karta = value[index_karte]
                value.pop(index_karte)
                print(odabrana_karta, " Slucajno odabrana karta iz ruke")
                return odabrana_karta
            elif(key == "stol"):
                print(value, " Stol")
            elif(key == "dobivene"):
                print(value, " dobivene")
            else:
                print(value, " protivnik")
        


if __name__ == "__main__":
    igrac2 = Igrac("igrac2")
    