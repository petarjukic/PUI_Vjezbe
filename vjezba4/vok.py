
from copy import deepcopy


class VOK:
    def __init__(self, init_start="VOKB||----", init_end="----||VOKB"):
        self.board = [i for i in init_start]
        self.board_end = [i for i in init_end]
        self.board_start = deepcopy(self.board)
        self.stack = []


    def __str__(self):
        return str(self.board)


    def next_action(self):
        next_state_list = []
        possible_solutions = ["V", "O", "K", "B"]

        boat_index = int(self.board.index("B"))

        for i in possible_solutions:
            if(boat_index > 4):
                if(i in self.board[-4:]):
                    next_state_list.append(i)
            if(boat_index < 4):
                if(i in self.board[:4]):
                    next_state_list.append(i)

        return next_state_list


    def next_states(self):
        state_list = []

        for act in self.next_action():
            tmp = self.copy()
            
            tmp.action(act)
            state_list.append(tmp)
        
        return state_list


    def is_solved(self):
        return self.board == self.board_end
    

    def is_terminal(self):
        if ("V" in self.board[:4] and "O" in self.board[:4] and
            "B" not in self.board[:4]) or ("V" in self.board[-4:] and
            "O" in self.board[-4:] and "B" not in self.board[-4:]):
            return True

        elif ("O" in self.board[:4] and "K" in self.board[:4] and 
            "B" not in self.board[:4]) or ("O" in self.board[-4:] and 
            "K" in self.board[-4:] and "B" not in self.board[-4:]):
            return True

        elif (self.board == self.board_end):
            return True
        
        return False
   
    def undo_action(self, act):

        self.action(act)            
        return self.board

   
    def action(self, act):
        index = int(self.board.index(act))
        boat_index = int(self.board.index("B"))
        
        if(index < 4 and boat_index < 4):
            new_index = index + 6
            new_boat = boat_index + 6
        elif(index > 4 and boat_index > 4):
            new_index = index - 6
            new_boat = boat_index - 6
    
        self.board[new_index] = act
        self.board[index] = "-"
        self.board[boat_index] = "-"
        self.board[new_boat] = "B"

   
    def copy(self):
        return deepcopy(self)


if __name__ == "__main__":
    vok = VOK()
    print(vok)
