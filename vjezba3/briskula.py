    
# from karte import Karte


class Briskula:
    # bodovi = 0
    # snaga = 0 

    def __init__(self, igrac1, igrac2, bodovi={}, snaga={}):
        self.igrac1 = igrac1
        self.igrac2 = igrac2
        self.bodovi = bodovi
        self.snaga = snaga


    def __str__(self):
        # return self.igrac1.akcija()
        print(self.igrac1)
        return "Ispis stanja igre"


    def rezultat():
        if(True):
            return 1 # POBJEDA 1. IGRACA
        elif(False):
            return 2 # POBJEDA 2. IGRACA
        else:
            return 0 # NERIJESENO


    def stanje(stanje_igre):
        print("Rjecink potreban za metodu agenta akcija")
        return stanje_igre


    def odigraj_partiju(prikaz=True):
        print(prikaz)


    def odigraj_ruku(prikaz=True):
        # trenutna_karta = Karte.izvuci()
        
        if(prikaz):
            print("trenutna_karta")

