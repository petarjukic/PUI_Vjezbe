
from copy import deepcopy


class VOK:
    def __init__(self, init_start="VOKB||----", init_end="----||VOKB"): # GOTOVO
        self.board = [i for i in init_start]
        self.board_end = [i for i in init_end]
        self.board_start = deepcopy(self.board)
        self.stack = []


    def __str__(self): # GOTOVO
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


    def next_states(self): # IN PROGRESS
        state_list = []

        for act in self.next_action():
            tmp = self.copy()
            
            tmp.action(act)
            state_list.append(tmp)
        
        # print("STATE LIST ", state_list)

        return state_list


    def is_solved(self): # GOTOVO
        return self.board == self.board_end
    

    def is_terminal(self): # GOTOVO
        if ("V" in self.board[:4] and "O" in self.board[:4] and
            "B" not in self.board[:4]) or ("V" in self.board[-4:] and
            "O" in self.board[-4:] and "B" not in self.board[-4:]):
            #print("Vuk pojeo ovcu")
            return True
        elif ("O" in self.board[:4] and "K" in self.board[:4] and 
            "B" not in self.board[:4]) or ("O" in self.board[-4:] and 
            "K" in self.board[-4:] and "B" not in self.board[-4:]):
            #print("Ovca pojela kupus")   
            return True
        elif (self.board == self.board_end):
            return True
        
        return False
   
    def undo_action(self, act): # GOTOVO

        self.action(act)            
        return self.board

   
    def action(self, act): # LEGALNE AKCIJE IN PROGRESS
        # print("OVO JE ACTION ", act)
        
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

   
    def copy(self): # GOTOVO
        return deepcopy(self)


if __name__ == "__main__":
    vok = VOK()
    print(vok)
