La clase Engine maneja un juego de memoria. El juego consiste en crear una cuadrícula de emojis y permitir a los jugadores descubrir y emparejar pares de emojis coincidentes.
La clase tiene los siguientes métodos:

1.vaciar(): Restablece el estado del juego, borrando todos los tableros y puntuaciones.
2.tope(fila, columna): Verifica si el tamaño de cuadrícula solicitado (número de filas y columnas) es válido, es decir, entre 2x2 y 6x5 o 5x6, y que el número total de celdas sea par.
3.crear_tablero(fila, columna): Crea los tableros del juego (del jugador, de la CPU y original) en función del tamaño de cuadrícula solicitado.
4.random_emoji(): Genera un emoji aleatorio único de un diccionario predefinido de emojis.
5.llenar_tablero(fila, columna): Rellena los tableros del juego con emojis colocados aleatoriamente.
6.mostrar_tablero_original(fila, columna): Imprime el tablero original lleno de emojis.
7.mostrar_tablero_jugador(fila, columna): Imprime el tablero del jugador, mostrando los emojis destapados y las celdas ocultas.
8.comprobar_posicion(fila, columna, nombre): Maneja el turno del jugador, donde el jugador selecciona dos celdas para descubrir. Verifica si las celdas seleccionadas contienen emojis coincidentes y actualiza el estado del juego en consecuencia.
9.PJvsPJ(fila, columna, nombre1, nombre2): Gestiona un juego de jugador contra jugador, donde dos jugadores humanos se turnan.
10.CPU_NORMAL(fila, columna, nombre): Maneja el turno de la CPU en el modo de dificultad "Normal", donde la CPU intenta recordar y descubrir pares coincidentes revelados anteriormente.
11.CPU_DIFICIL(fila, columna, nombre): Maneja el turno de la CPU en el modo de dificultad "Difícil", donde la CPU tiene una función de memoria más avanzada para recordar y descubrir pares coincidentes revelados anteriormente.
12.CPU(fila, columna, modo, nombre): Gestiona el turno de la CPU, despachando al modo de dificultad apropiado.
13.PJVsCPU(fila, columna, nombre1, modo, nombre2): Gestiona un juego de jugador contra CPU, donde el jugador humano se turna con la CPU.
14.CPUVsCPU(fila, columna, modo, nombre, nombre2): Gestiona un juego de CPU contra CPU, donde dos CPUs del mismo modo de dificultad juegan entre sí.
15.play(): El punto de entrada principal del juego, donde el usuario puede elegir el modo de juego y comenzar a jugar.
