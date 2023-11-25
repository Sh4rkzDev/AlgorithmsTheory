# Problemas NP-Completos - TP3

TP realizado para la materia Teoria de Algoritmos de la FIUBA. Para poder correr el codigo, es necesario tener Python instalado en la computadora.
Para correr todos los algoritmos y ver cuanto tarda cada uno a la vez que cuantos elementos contiene su solucion, corra el siguiente comando:
```
$ python3 compare.py <archivo>
```
Siendo `<archivo>` el archivo que sirva como set de datos para correr el programa con el formato correcto.
Ya hay algunos archivos de prueba. Por ejemplo, para ejecutar el programa con el archivo `75.txt` se debe ingresar
```
$ python3 compare.py tests/75.txt
```
Para correr solo el algoritmo por **Backtracking**, correr:
```
$ python3 bt.py <archivo>
```
Para correr solo el algoritmo por **Programacion Lineal**, correr:
```
$ python3 lp.py <archivo>
```
o su version aproximada:
```
$ python3 lpa.py <archivo>
```
Para ver la diferencia y el ratio de aproximacion entre estos dos, correr:
```
$ python3 approx_analisis.py
```
Para correr el algoritmo con tecnica **Greegy**, correr:
```
$python3 greedy.py <archivo>
```
Para correr un codigo que genere un grafico:
```
$ python3 graphics.py
```
notar que correr este algoritmo creara una imagen `graphic.png` en el directorio en el cual se corra el programa.
