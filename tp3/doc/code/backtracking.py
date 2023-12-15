def BT2(A, jugadores, solucion, n, utilizados):

    if n == len(A):                 #Ya revise todas las listas que habian
        copia = jugadores[:]
        solucion[0] = copia
        return solucion

    if len(solucion[0]) != 0 and len(jugadores) >= len(solucion[0]):   #Hago mayor igual porque si esta aca es porque va a iterar devuelta
        return solucion

    if (elementosEnComun(A[n], jugadores)):
        BT2(A, jugadores, solucion, n+1, utilizados)
        return solucion

    for jugador in A[n]:
        if jugador in utilizados:
            if utilizados[jugador] < n: continue       #Ya probo todas las combinaciones con ese jugador.
        else:
            utilizados[jugador] = n
        jugadores.append(jugador)
        BT2(A, jugadores, solucion, n+1, utilizados)
        jugadores.remove(jugador)

    return solucion
