from briskula import Briskula
from human import Human
from igrac import Igrac
from karte import Spil


if __name__ == "__main__":
    broj_partija = int(input("UNESITE KOLIKO ZELITE ODIGRAT PARTIJA: "))

    while(broj_partija <= 0):
        print("Broj partija mora biti veci od 0(nula) ")
        broj_partija = int(input("UNESITE KOLIKO ZELITE ODIGRAT PARTIJA: "))

    igrac1 = Human("igrac1")
    igrac2 = Igrac("igrac2")


    briskula1 = Briskula(igrac1, igrac2)
    stanje_igre = briskula1.stanje()

    while(broj_partija != 0):
        try:
            while(stanje_igre["stol"]):
                human_karta = igrac1.akcija(stanje_igre)
                comp_karta = igrac2.akcija(stanje_igre)
                if(briskula1.provjera_jacine(human_karta, comp_karta, stanje_igre["zog"])):
                    stanje_igre["ruka"].update(stanje_igre["stol"].peskaj())
                    print("jaca je od human, human baca prvi")
                else:
                    print("jaca je od comp, comp baca prvi")
        except:
            print("GOTOVO")
        broj_partija -= 1
        spil = Spil()
        stanje_igre.update({"stol": spil})
    
