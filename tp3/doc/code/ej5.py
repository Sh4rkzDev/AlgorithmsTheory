from pulp import LpVariable, LpProblem, LpMinimize, lpSum

def creacion_listas(ruta):

    archivo = open(ruta)
    l = []
    
    s = archivo.readline().rstrip("\n")
    while s!="":
        lista = s.split(",")
        l.append(lista)
        s = archivo.readline().rstrip("\n")

    archivo.close()

    return l

def lp_approx(sets):
    # 1) We create continuous variables for each player
    total_players = {player for s in sets.values() for player in s}
    players_vars = {player: LpVariable(f"{player}", lowBound=0, upBound=1) for player in total_players}

    # 2) We create a linear programming problem 
    problem = LpProblem("Selection", LpMinimize)

    # 3) Constraints: each subset must have at least one player
    for _, subset_players in sets.items():
        problem += lpSum(players_vars[player] for player in subset_players) >= 1
    
    # 4) We minimize the total number of selected elements
    problem += lpSum(players_vars.values())

    problem.solve()

    # 5) We extract the continuous solution
    cont_solution = [player.name for player in players_vars.values() if player.varValue > 0]

    # 6) We calculate the rounding threshold
    b = max(len(subset) for subset in sets.values())

    # 7) Rounding the solution
    rounded_solution = [player for player in total_players if players_vars[player].varValue >= 1/b]

    return rounded_solution, cont_solution

def solution_lp_approx(ruta):
    listas = creacion_listas(ruta)
    sets_dict = {f'S{i + 1}': set(inner_list) for i, inner_list in enumerate(listas)}
    rounded,_ = lp_approx(sets_dict)
    print(rounded)
    return rounded

solution_lp_approx("path")