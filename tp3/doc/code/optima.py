import input
import backtracking

def solucionOptima(ruta):
    A = input.ReadInputs(ruta)
    soluciones = backtracking.BT2(A,[],[],0,{},[float("inf")])
    return min(soluciones,key=lambda item:len(item))
