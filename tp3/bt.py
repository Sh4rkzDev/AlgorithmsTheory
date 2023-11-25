import input

def elementosEnComun(listaA, listaB):
    """
    Devuelve True si contienen elementos en comun, False si no.
    """
    for elemento in listaA:
        if elemento in listaB:
            return True
    return False

def BT2(A, jugadores, soluciones, n, utilizados, minimo):

    if n == len(A):                 #Ya revise todas las listas que habian
        copia = jugadores[:]
        minimo[0] = len(copia)
        soluciones.append(copia)
        return
    
    if len(jugadores) >= minimo[0]:   #Hago mayor igual porque si esta aca es porque va a iterar devuelta
        return

    if (elementosEnComun(A[n], jugadores)):
        BT2(A, jugadores, soluciones, n+1, utilizados, minimo)
        return

    for jugador in A[n]:
        if jugador in utilizados:
            if utilizados[jugador] < n: continue       #Ya probo todas las combinaciones con ese jugador.
        else:
            utilizados[jugador] = n
        jugadores.append(jugador)
        BT2(A, jugadores, soluciones, n+1, utilizados, minimo)
        jugadores.remove(jugador)

    return soluciones

def solucionOptima(A):
    soluciones = BT2(A,[],[],0,{},[float("inf")])
    return min(soluciones,key=lambda item:len(item))

def main():
    A = input.ReadInputs()
    solucionOptima(A)

if __name__ == "__main__":
    main()
