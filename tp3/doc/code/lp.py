from pulp.apis import PULP_CBC_CMD
from pulp import LpProblem, LpMinimize, LpVariable, lpSum

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
    problem.solve(PULP_CBC_CMD(msg=False))

    # 5) We extract the solution
    solution = []
    for _, player in players_vars.items():
        if player.varValue > 0:
            solution.append(f"{player}")

    return solution
