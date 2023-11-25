def BT2(A, jugadores, soluciones, n, utilizados, minimo):

    if n == len(A):
        copia = jugadores[:]
        minimo[0] = len(copia)
        soluciones.append(copia)
        return

    if len(jugadores) >= minimo[0]:
        return

    if (elementosEnComun(A[n], jugadores)):
        BT2(A,jugadores,soluciones,n+1,utilizados,minimo)
        return

    for jugador in A[n]:
        if jugador in utilizados:
            if utilizados[jugador] < n: continue
        else:
            utilizados[jugador] = n
        jugadores.append(jugador)
        BT2(A, jugadores, soluciones, n+1, utilizados, minimo)
        jugadores.remove(jugador)

    return soluciones
