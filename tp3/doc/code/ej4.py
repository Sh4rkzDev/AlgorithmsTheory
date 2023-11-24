from pulp import LpProblem, LpMinimize, LpVariable, lpSum
def list_creation(ruta):
    file = open(ruta)
    l = []
    
    s = file.readline().rstrip("\n")
    while s!="":
        lista = s.split(",")
        l.append(lista)
        s = file.readline().rstrip("\n")
    file.close()
    return l

def hitting_set_lp(sets):
    # 1) We create binary variables for each player
    total_players = {player for s in sets.values() for player in s}
    players_vars = {player: LpVariable(f"{player}", cat='Binary') for player in total_players}

    # 2) We create a linear programming problem 
    problem = LpProblem("HittingSet", LpMinimize)

    # 3) Constraints: each subset must have at least one player
    for _, subset_players in sets.items():
        problem += lpSum(players_vars[player] for player in subset_players) >= 1
    
    # 4) We minimize the total number of selected elements
    problem += lpSum(players_vars.values())

    problem.solve()

    # 5) We extract the solution
    solution = []
    for _, player in players_vars.items():
        if player.varValue > 0:
            solution.append(f"{player}")

    return solution
     

def solution_lp(ruta):
    listas = list_creation(ruta)
    sets_dict = {f'S{i + 1}': set(inner_list) for i, inner_list in enumerate(listas)}
    hs = hitting_set_lp(sets_dict)
    return hs

solution_lp("nombre de la ruta")


