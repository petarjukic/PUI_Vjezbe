class Stapic:
    def __init__(self, init_number=11):
        self.floor = init_number
        self.player = "1"
        self.dict = {self.player, self.floor}


    def __str__(self):
        return ("Na podu je: ", self.floor,",a sada je",self.player, "igrac")


    def change_player(self):
        if(self.player == "1"):
            self.player = "2"
        else:
            self.player = "1"


    def action(self, number):
        self.floor -= number
        self.change_player()

    
    def undo_action(self, number):
        self.floor += number
        self.change_player()


    def is_terminal(self):
        if(self.is_solved()):
            return True
        elif(self.floor < 2):
            return True
            
        return False


    def is_solved(self):
        return self.floor == 2



if __name__ == "__main__":
    stapic = Stapic()
