from vok import VOK



def generate(vokb, skup):
    if(str(vokb) in skup):
        return
    
    print(vokb)
    skup.add(str(vokb))

    if(vokb.is_terminal()):
        return
    
    for i in vokb.next_action():
        vokb.action(i)
        generate(vokb, skup)
        vokb.undo_action(i)

    return

def dohvati(rijecnik, rjesenje):
    while(rjesenje != None):
        print(str(rjesenje))
        rjesenje = rijecnik[str(rjesenje)]
        


def solution_dfs(vok):
    queue = [vok]
    rijecnik = {}
    rijecnik[str(vok)] = None
    visited = set({})
    
    while(len(queue) > 0):
        q_top = queue.pop(-1) 
        
        if(q_top.is_terminal()):
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("Ima rjesenje")
                print("DUZINA VISITED ", len(visited))
                dohvati(rijecnik, q_top)
                return
        
        elif(str(q_top) not in visited):
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in rijecnik):    
                    rijecnik[str(i)] = str(q_top)
                queue.append(i)
    
    print("Nema rjesenja")
    return


def solution_bfs(vok):
    queue = [vok]
    rijecnik = {}
    rijecnik[str(vok)] = None
    visited = set({}) 

    while(len(queue) > 0):
        q_top = queue.pop(0) 
        
        if(q_top.is_terminal()):
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("Ima rjesenje")
                print("DUZINA VISITED ", len(visited))
                dohvati(rijecnik, q_top)
                return
        
        elif(str(q_top) not in visited):
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in rijecnik):    
                    rijecnik[str(i)] = str(q_top)
                queue.append(i)
    
    print("Nema rjesenja")
    return


def BestFS(vok):
    queue = [vok]
    rijecnik = {}
    rijecnik[str(vok)] = None
    visited = set({})

    while(len(queue) > 0):
        queue = sorted(queue, key=heuristic)
        q_top = queue.pop(0)
        
        if(q_top.is_terminal()):
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("Ima rjesenje")
                print("DUZINA VISITED ", len(visited))
                dohvati(rijecnik, q_top)
                return
        
        elif(str(q_top) not in visited):
            
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in rijecnik):
                    rijecnik[str(i)] = str(q_top)
                queue.append(i)
    
    print("Nema rjesenja")
    return


def heuristic(state):
    counter = 0
    right = state.board[-4:]
    
    for i in right:
        if(i == "-"):
            counter += 1

    return counter


if __name__ == "__main__":
    vokb = VOK()

    print("Generate: ")
    r = set({})
    generate(vokb, r)
    
    print("Solution dfs\n")
    solution_dfs(vokb)

    print("Solution bfs\n")
    solution_bfs(vokb)

    print("Solution BestFS\n")
    BestFS(vokb)
