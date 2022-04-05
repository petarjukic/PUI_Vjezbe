import karte
import human
import igrac


class Briskula:
    snaga = {
        "1": 1,
        "3": 2,
        "13": 3,
        "12": 4,
        "11": 5
    }

    bodovi = {
        "1": 11,
        "3": 10,
        "13": 4,
        "12": 3,
        "11": 2
    }

    def __init__(self, igrac1, igrac2, stanje_igre1):
        self.igrac1 = igrac1
        self.igrac2 = igrac2
        self.stanje_igre1 = stanje_igre1


    def __str__(self): 
        # VIDIT KAKO IZBROJIT SPIL
        velicina = 0

        return "Broj karata je: " + str(velicina),\
            "\nIme igraca1: " + self.igrac1.ime + "\nIme igraca2: " + self.igrac2.ime, \
            "\nBriskula je: " + str(self.stanje_igre1["zog"]), \
            "\nKarte na stolu su: " + str(self.stanje_igre1["stol"]), \
            "\nKarte " + self.igrac1.ime + " su: " + str(self.stanje_igre1["ruka"])

    
    def provjera_karata(self, karta):
        if(str(karta.broj) in self.bodovi):
            return self.bodovi[str(karta.broj)]
        
        return 0

    def provjera_jacine(self, human_karta, comp_karta, zog):
        if(human_karta.zog == zog.zog and comp_karta.zog == zog.zog):
            if((str(human_karta.broj) not in self.snaga) and (str(comp_karta.broj) not in self.snaga)):
                if(human_karta.broj > comp_karta.broj):
                    print(self.igrac1.ime, " karta je jaca ", human_karta.broj)
                    return True
                else:
                    print(self.igrac2.ime, " karta je jaca: ", comp_karta.broj)
                    return False  
            elif((str(human_karta.broj) in self.snaga) and (str(comp_karta.broj) not in self.snaga)):
                print(self.igrac1.ime, " karta je jaca ", self.snaga[str(human_karta.broj)])
                return True
            else:
                print(self.igrac2.ime, " karta je jaca ", comp_karta)
                return True
        elif(human_karta.zog != zog.zog and comp_karta.zog == zog.zog):
            print(self.igrac2.ime, " karta je jaca ", comp_karta)
            return False
        elif(human_karta.zog == zog.zog and comp_karta.zog != zog.zog):
            print(self.igrac1.ime, " karta je jaca ", human_karta)
            return True
        elif(human_karta.zog != zog.zog and comp_karta.zog != zog.zog):
            if(human_karta.zog == comp_karta.zog):
                if(str(human_karta.broj) in self.snaga and str(comp_karta.broj) not in self.snaga):
                    print(self.igrac1.ime, " ima jacu kartu")
                    return True
                elif(str(human_karta.broj) not in self.snaga and str(comp_karta.broj) not in self.snaga):
                    return human_karta.broj > comp_karta.broj
                elif(str(human_karta.broj) not in self.snaga and str(comp_karta.broj) in self.snaga):
                    print(self.igrac2.ime, " ima jacu kartu ")
                    return False
                if(self.snaga[str(human_karta.broj)] > self.snaga[str(comp_karta.broj)]):
                    print(self.igrac1.ime, " ima jacu kartu")
                    return True
                else:
                    print(self.igrac2.ime, " ima jacu kartu")
                    return False
            else:
                if(str(human_karta.broj) in self.snaga and str(comp_karta.broj) not in self.snaga):
                    print(self.igrac1.ime, " ima jacu kartu")
                    return True
                elif(str(human_karta.broj) not in self.snaga and str(comp_karta.broj) in self.snaga):
                    print(self.igrac2.ime, " ima jacu kartu")
                    return False
                else:
                    return human_karta.broj > comp_karta.broj
    

    def rezultat(self):
        comp_punti = 0
        human_punti = 0

        for key, value in self.stanje_igre1.items():
            if(key == "dobivene"):
                for el in value:
                    punti = self.provjera_karata(el)
                    human_punti += punti
                if(human_punti > 60):
                    print(self.igrac1.ime, " ima ", human_punti, " punata")
                    print(self.igrac2.ime, " ima ", comp_punti, " punata")
                    return 1 # POBJEDA 1. IGRACA
            if(key == "dobivene_protivnik"):
                for el in value:
                    punti = self.provjera_karata(el)
                    comp_punti += punti
                if(comp_punti > 60):
                    print(self.igrac2.ime, " ima ", comp_punti, " punata")
                    print(self.igrac1.ime, " ima ", human_punti, " punata")
                    return 2 # POBJEDA 2. IGRACA

        print(self.igrac1.ime, " ima ", human_punti)
        print(self.igrac2.ime, " ima ", comp_punti)
        return 0 # NERIJESENO


    def stanje(self):
        velicina_ruke = len(self.stanje_igre1["ruka"])
        while(velicina_ruke < 3):
            nesto = self.stanje_igre1["stol"].peskaj()
            self.stanje_igre1["ruka"].append(nesto)
            velicina_ruke += 1

        self.stanje_igre1["dobivene"] = []
        self.stanje_igre1["dobivene_protivnik"] = []
        self.stanje_igre1["zog"] = self.stanje_igre1["stol"].peskaj()
        self.stanje_igre1.update({"stol": self.stanje_igre1["stol"]})
        
        return self.stanje_igre1


    def odigraj_partiju(self, prikaz=True):
        spil = karte.Spil()
        self.stanje_igre1["stol"] = spil
        self.stanje_igre1["ruka"] = []
        self.stanje_igre1 = self.stanje()

        print("BRISKULA JE: ", self.stanje_igre1["zog"])
        self.stanje_igre1["stol"].dodaj(self.stanje_igre1["zog"])

        while(len(self.stanje_igre1["stol"].karte)):
            try:
                while(len(self.stanje_igre1["ruka"]) < 3):
                    nesto = self.stanje_igre1["stol"].peskaj()
                    self.stanje_igre1["ruka"].append(nesto)
            except:
                print("GOTOVO")
            human_karta, comp_karta = self.odigraj_ruku(prikaz)
            peska = []
            peska.append(human_karta)
            peska.append(comp_karta)
            if(self.provjera_jacine(human_karta, comp_karta, self.stanje_igre1["zog"])):
                print(self.igrac1.ime, " ima jacu kartu")
                self.stanje_igre1["dobivene"].extend(peska)
            else:
                print(self.igrac2.ime, " ima jacu kartu")
                self.stanje_igre1["dobivene_protivnik"].extend(peska)


        if(len(self.stanje_igre1["ruka"]) > 0):
            human_karta, comp_karta = self.odigraj_ruku(prikaz)
            if(self.provjera_jacine(human_karta, comp_karta, self.stanje_igre1["zog"])):
                print(self.igrac1.ime, " ima jacu kartu")
                peska = []
                peska.append(human_karta)
                peska.append(comp_karta)
                self.stanje_igre1["dobivene"].extend(peska)
            else:
                print(self.igrac2.ime, " ima jacu kartu")
                peska = []
                peska.append(human_karta)
                peska.append(comp_karta)
                self.stanje_igre1["dobivene_protivnik"].extend(peska)

        pobjednik = self.rezultat()

        if(pobjednik == 1):
            print("IGRAC JE POBJEDNIK")
        elif(pobjednik == 2):
            print("COMP JE POBJEDNIK")
        elif(pobjednik == 0):
            print("NERIJESENO")
        else:
            print("GRESKA")

        if(prikaz):
            print(briskula1)


    def odigraj_ruku(self, prikaz=True):
        human_karta = self.igrac1.akcija(self.stanje_igre1)
        comp_karta = self.igrac2.akcija(self.stanje_igre1)
        
        if(prikaz):
            print(self.igrac1.ime, " u ruci za odigrat karta: ", human_karta)
            print(self.igrac2.ime, " u ruci za odigrat karta: ", comp_karta)
        
        return human_karta, comp_karta


class IgracBriskule:
    def __init__(self, ruka, dobivene, protivnik_dobivene):
        self.ruka = ruka
        self.dobivene = dobivene
        self.protivnik_dobivene = protivnik_dobivene

    
    
if __name__ == "__main__":    
    igrac1 = human.Human("igrac1")
    igrac2 = igrac.Igrac("igrac2")

    briskula1 = Briskula(igrac1, igrac2, {})
    broj_partija = int(input("UNESITE KOLIKO ZELITE ODIGRAT PARTIJA: "))

    while(broj_partija <= 0):
        print("Broj partija mora biti veci od 0(nula) ")
        broj_partija = int(input("UNESITE KOLIKO ZELITE ODIGRAT PARTIJA: "))
    
    while(broj_partija != 0):
        briskula1.odigraj_partiju()
        broj_partija -= 1
