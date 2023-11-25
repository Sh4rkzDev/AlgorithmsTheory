# Función para realizar mediciones con diferentes instancias
from pulp import LpVariable, LpProblem, LpMinimize, lpSum
from ej4 import solution_lp
from ej5 import solution_lp_approx

def calculate_approximation_ratio(optimal_sol, approx_sol):
    if optimal_sol == 0:
        return 1.0  
    return approx_sol / optimal_sol

def perform_measurements(instances):
    for instance in instances:
        optimal_solution = solution_lp(instance)
        approx_solution = solution_lp_approx(instance)

        print(f"Optimal: {optimal_solution}")
        print(f"Approximate: {approx_solution}")
        approximation_ratio = calculate_approximation_ratio(len(optimal_solution), len(approx_solution))
        print(f"Approximation Ratio (r(A)): {approximation_ratio}\n")


ruta = []

ruta1 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\7.txt"
ruta2 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\10_pocos.txt"
ruta3 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\10_todos.txt"
ruta4 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\10_varios.txt"
ruta5 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\15.txt"
ruta6 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\20.txt"
ruta6 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\50.txt"
ruta7 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\100.txt"
ruta8 = "C:\\Users\\Helen\\OneDrive\\Documentos\\FIUBA\\TDA\\tp3\\200.txt"


ruta.append(ruta1)
ruta.append(ruta2)
ruta.append(ruta3)
ruta.append(ruta4)
ruta.append(ruta5)
ruta.append(ruta6)
ruta.append(ruta7)
ruta.append(ruta8)
perform_measurements(ruta)