from briskula import Briskula
from igrac import Igrac


if __name__ == "__main__":
    igrac1 = Igrac("agent1")
    igrac2 = Igrac("agent2")

    i = 0
    briskula = Briskula(igrac1, igrac2, {})
    while(i < 50):
        briskula.odigraj_partiju(False)
        i += 1

    briskula1 = Briskula(igrac2, igrac1, {})
    while(i < 100):
        briskula.odigraj_partiju(False)
        i += 1
    