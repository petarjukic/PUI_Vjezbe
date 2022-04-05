from briskula import Briskula
from igrac import Igrac


if __name__ == "__main__":
    igrac1 = Igrac("agent1")
    igrac2 = Igrac("agent2")

    i = 0
    briskula = Briskula(igrac1, igrac2, {})
    while(i < 1): # TRIBA BIT 100
        # POLA PARTIJA IGRA PRVI A POLA DRUGI AGENT
        briskula.odigraj_partiju(False)
        i += 1
    