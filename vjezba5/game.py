from stapici import Stapic


def minimax(igra):
    if(igra.is_terminal()):
        if(igra.player == "1"):
            return 100
        else:
            return -100

    if(igra.player == "1"):
        max_num = 100
        for i in range(1, 3):
            igra.action(i)
            v = minimax(igra)
            igra.undo_action(v)
            if(v > max_num):
                max_num = v

        return max_num
    
    else:
        min_num = -100
        for i in range(1, 3):
            igra.action(i)
            m = minimax(igra)
            igra.undo_action(i)

            if(m < min_num):
                min_num = m

        return min_num



def provjera(num):
    return num == 1 or num == 2


if __name__ == "__main__":
    igra = Stapic()

    while(not igra.is_terminal()):
        if(igra.player == "1"):
            num = int(input("Unsei broj stapica: "))
            while(not provjera(num)):
                num = int(input("Unsei broj stapica: "))
            
            if(igra.floor < num):
                break
           
            igra.action(num)
            print(igra)
            print("Broj stapica ", num)
            igra.change_player()
        else:
            comp_num = minimax(igra)
            
            if(igra.floor < comp_num):
                break

            igra.action(comp_num)
            print("Broj stapica kod compa je: ", comp_num)
            print(igra)
            igra.change_player()

    igra.change_player()
    print("Pobjednik je ", igra.player)
