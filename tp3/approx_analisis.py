from lp import solution_lp
from lpa import solution_lp_approx

def calculate_approximation_ratio(optimal_sol, approx_sol):
    if optimal_sol == 0:
        return 1.0  
    return approx_sol / optimal_sol

def perform_measurements(instances):
    for instance in instances:
        path = "tests/" + instance
        optimal_solution = solution_lp(path)
        approx_solution = solution_lp_approx(path)

        print(f"Optimal: {optimal_solution}")
        print(f"Approximate: {approx_solution}")
        approximation_ratio = calculate_approximation_ratio(len(optimal_solution), len(approx_solution))
        print(f"Approximation Ratio (r(A)): {approximation_ratio}\n")


ruta = ["7.txt", "10_pocos.txt", "10_todos.txt", "10_varios.txt", "15.txt", "20.txt", "50.txt", "100.txt", "200.txt"]
perform_measurements(ruta)
