from karte import Spil


class Briskula:
    snaga = {
        "A": 1,
        "3": 2,
        "K": 3,
        "Q": 4,
        "J": 5
    }

    bodovi = {
        "A": 11,
        "3": 10,
        "K": 4,
        "Q": 3,
        "J": 2
    }

    def __init__(self, igrac1, igrac2):
        self.igrac1 = igrac1
        self.igrac2 = igrac2


    def __str__(self):
        ispis = self.igrac1.ime + " ima karte: " + self.igrac2.ime
        ispis += " Briksula je: "
        print(self.igrac1)
        return ispis

    
    def provjera_karata(self, karta):
        if(karta[0] in self.bodovi):
            return self.bodovi[karta[0]]
        
        return 0

    def provjera_jacine(self, human_karta, comp_karta, zog):
        human_karta = human_karta[0]
        comp_karta = comp_karta[0]
        if(human_karta in zog and comp_karta in zog):
            if((human_karta not in self.snaga) and (comp_karta not in self.snaga)):
                if(human_karta > comp_karta):
                    print(" human karta je jaca ", self.snaga[human_karta])
                    return 1
                else:
                    print("comp karta je jaca: ", self.snaga[comp_karta])
                    return 0    
            elif((human_karta in self.snaga) and (comp_karta not in self.snaga)):
                print("human karta je jaca ", self.snaga[human_karta])
                return 1
            else:
                print("comp karta je jaca ")
                return 1
        elif(human_karta not in zog and comp_karta in zog):
            print("comp karta je jaca ", comp_karta)
            return 0
        
        elif(human_karta in zog and comp_karta not in zog):
            print("human karta je jaca ", human_karta)
            return 1
    

    def rezultat(self, stanje_igre):
        comp_punti = 0
        human_punti = 0

        for key, value in stanje_igre.items():
            if(key == "dobivene"):
                for el in value:
                    punti = self.provjera_karata(el)
                    human_punti += punti
                if(human_punti > 60):
                    return 1 # POBJEDA 1. IGRACA
            if(key == "dobivene_protivnik"):
                for el in value:
                    punti = self.provjera_karata(el)
                    comp_punti += punti
                if(comp_punti > 60):
                    return 2 # POBJEDA 2. IGRACA
        
        return 0 # NERIJESENO


    def stanje(self):
        stanje_igre = {}
        spil = Spil()
        karte_igraca1 = []

        karta = spil.peskaj()
        karte_igraca1.append(karta)
        karta = spil.peskaj()
        karte_igraca1.append(karta)
        karta = spil.peskaj()
        karte_igraca1.append(karta)

        print("Rjecink potreban za metodu agenta akcija")
        # human ruka
        bris = spil.peskaj()
        stanje_igre["briskula"] = bris.zog
        stanje_igre["ruka"] = karte_igraca1
        stanje_igre["dobivene"] = []
        stanje_igre["dobivene_protivnik"] = []
        stanje_igre["stol"] = spil

        return stanje_igre


    def odigraj_partiju(self, prikaz=True):
        print(prikaz)


    def odigraj_ruku(self, prikaz=True):
        # trenutna_karta = Karte.izvuci()
        
        if(prikaz):
            print("trenutna_karta")


if __name__ == "__main__":
    briskula = Briskula("igrac1", "igrac2")

    print(briskula.stanje())
