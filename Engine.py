import random
from Jugador import Jugador

class Engine:

    def __init__(self):
        self.emojis = {1:"😀",2:"🥰",3:"😨",4:"🥶",5:"🦍",6:"👾",7:"🐲",
            8:"😡",9:"🦘",10:"🐳",11:"🐼",12:"🐺",13:"🦃",14:"🤢",15:"😎"}
        self.tablero_original = []
        self.tablero_jugador = []
        self.lista_claves = []
        self.tablero_cpu = []
        self.usados = []
        self.lista_claves_cpu = []
        self.p1 = 0
        self.p2 = 0

    def vaciar(self):
        self.tablero_original = []
        self.tablero_jugador = []
        self.lista_claves = []
        self.tablero_cpu = []
        self.lista_claves_cpu = []
        self.usados = []
        self.p1 = 0
        self.p2 = 0

    # Metodo que recibe por parametro el numero de filas y de columnas, si excede las 6 filas y 5 columnas o viceversa devuelve false.
    # Devuelve tambien false si el tamaño no es par o en menor que 2x2.
    def tope(self,fila,columna):
        if fila < 2 or columna < 2:
            print("El numero de filas y columnas no puede ser menor de 2")
            return False
        if (fila <= 6 and columna <= 5) or (fila <= 5 and columna <= 6):
            if (fila * columna) % 2 == 0:
                return True
            else:
                print("El numero de filas x columnas debe ser par")
                return False
        else:
            print("El numero de filas y columnas no puede exceder de 6x5 o de 5x6")
            return False

    #Crea dos tableros "vacios" segun las filas y columnas que haya pedido el usuario.
    def crear_tablero(self,fila,columna):
        if self.tope(fila,columna) == True:
            for i in range(fila):
                rows = []
                for j in range(columna):
                    rows.append("+")
                self.tablero_cpu.append(rows.copy())
                self.tablero_jugador.append(rows.copy())
                self.tablero_original.append(rows.copy())
                self.lista_claves.append(rows.copy())
            return True
        else:
            return False
    #vuelve a esconder las posiciones desveladas    
    def vaciar_maquina(self,fila,columna):
            self.tablero_cpu = []
            for i in range(fila):
                rows = []
                for j in range(columna):
                    rows.append("+")
                self.tablero_cpu.append(rows.copy())

    #Metodo que genera un emoji aleatorio del diccionario pero si la clave ya esta guardado en la lista usados vuelve a generar otro emoji distintinto
    def random_emoji(self):
        while True:
            n = random.randint(1, 15)
            self.emoji_aleatorio = self.emojis[n]
            
            if n not in self.usados:
                self.usados.append(n)
                return self.emoji_aleatorio
            else:
                n = random.randint(1, len(self.emojis))
                self.emoji_aleatorio = self.emojis[n]

    # Metodo que comprueba primero si el tablero se ha podido crear y si es asi rellena el tablero de emojis de forma aleatoria con el metodo "random_emoji()", 
    # genera una posicion aleatoria una vez ya tiene el emoji generado, si la posicion no esta vacia genera otra posicion, y asi hasta generar una posicion que este vacia. 
    # No se genera otro emoji hasta que se han llenado dos posiciones con el mismo emoji.
    def llenar_tablero(self,fila,columna):
        if self.crear_tablero(fila,columna) is True:
            for i in range(int((fila*columna)/2)):
                emoji_aleatorio = self.random_emoji()
                for n in range(2):
                    while True:
                        fila_aleatoria = random.randint(0,fila-1)
                        columna_aleatoria = random.randint(0,columna-1)
                        if self.tablero_original[fila_aleatoria][columna_aleatoria] != '+':
                            fila_aleatoria = random.randint(0,fila-1)
                            columna_aleatoria = random.randint(0,columna-1)
                        else:
                            self.tablero_original[fila_aleatoria][columna_aleatoria] = emoji_aleatorio
                            self.lista_claves[fila_aleatoria][columna_aleatoria] = self.usados[i]
                            break
            return True
        return False

    # Metodo que imprime el tablero lleno de emojis segun las especificaciones del usuario.
    def mostrar_tablero_original(self,fila,columna):
        if self.llenar_tablero(fila,columna) is True:
            for i in self.tablero_original:
                for j in i:
                    print(j, end= "   ")
                print()

    # Metodo que muestra el tablero del jugador con el numero de filas al lado de cada fila y el numero de columnas encima de cada columna.
    def mostrar_tablero_jugador(self, fila, columna):
            print("    ", end="")
            for c in range(columna):
                print(c+1, end="   ")
            print()

            cont = 1
            for i in self.tablero_jugador:
                print(cont, end="   ")
                for j in i:
                    print(j, end="   ")
                print()
                cont += 1

    #Metodo que comprueba si la posicion elegida es correcta o no
    def comprobar_posicion(self,fila,columna,nombre):
        posiciones = []
        print("Te toca ",nombre)
        #Muestra el tablero del jugador al usuario
        self.mostrar_tablero_jugador(fila,columna)
        #elige una posicion y si está dentro de los parametros se descubre la carta, despues vuelve a elegir otra carta
        for i in range(2):
            f = int(input("Dime la fila: "))-1
            c = int(input("Dime la columna: "))-1
            while True:
                if f < 0 or f >= fila or c < 0 or c >= columna:
                    print("Esa posicion no está en el tablero")
                    f = int(input("Dime la fila: "))-1
                    c = int(input("Dime la columna: "))-1
                #si ya está dada la vuelta vuelve a elegir otra posicion
                elif self.tablero_jugador[f][c] != "+":
                    print("Esta carta ya está dada la vuelta")
                    f = int(input("Dime la fila: "))-1
                    c = int(input("Dime la columna: "))-1
                #si no está dado la vuelta la carta la descubre y añade la posicion al array posiciones
                elif self.tablero_jugador[f][c] == "+":
                    self.tablero_jugador[f][c] = self.tablero_original[f][c]
                    posiciones.append(f)
                    posiciones.append(c)
                    break
            #vuelve a mostrar el tablero al usuario con la carta dada la vueta
            self.mostrar_tablero_jugador(fila,columna)
        #si las dos posiciones que ha dicho el usuario coinciden con las claves devuelve true
        if self.lista_claves[posiciones[0]][posiciones[1]] == self.lista_claves[posiciones[2]][posiciones[3]]:
            return True
        else:
            #si no son iguales las claves se vuelve a tapar las cartas y se añaden las claves al tablero de la cpu, devuelve false
            self.lista_claves_cpu.append(self.lista_claves[posiciones[0]][posiciones[1]])
            self.lista_claves_cpu.append(self.lista_claves[posiciones[2]][posiciones[3]])

            self.tablero_cpu[posiciones[0]][posiciones[1]] = self.lista_claves[posiciones[0]][posiciones[1]]
            self.tablero_cpu[posiciones[2]][posiciones[3]] = self.lista_claves[posiciones[2]][posiciones[3]]

            self.tablero_jugador[posiciones[0]][posiciones[1]] = "+"
            self.tablero_jugador[posiciones[2]][posiciones[3]] = "+"
            print("Has fallado...(enter)")
            input()
            #deja limpia la consola para el siguiente jugador juegue
            for i in range(20):
                print()
            return False

    #Metodo que realiza la partida de jugador contra jugador
    def PJvsPJ(self,fila,columna,nombre1,nombre2):
        #si se puede llenar el tablero se puede jugar
        if self.llenar_tablero(fila, columna) is True:
            parejas = int((fila*columna)/2)
            #este while se seguirá ejecutando hasta que las puntuaciones de los dos jugadores sea igual que la mitad de lo que vale el tablero
            while self.p1 + self.p2 < parejas:
                #mientras que el jugador1 acierte sigue jugando y suma un punto, si falla pasa de turno
                while self.p1 + self.p2 < parejas and self.comprobar_posicion(fila,columna,nombre1) is True:
                    print("Has acertado la pareja!!!")
                    self.p1 += 1
                while self.p1 + self.p2 < parejas and self.comprobar_posicion(fila,columna,nombre2) is True:
                    self.p2 += 1
                    print("Has acertado la pareja!!!")
            #si la puntuacion 1 es mayor que la dos, gana el jugador uno y viceversa o empate
            if self.p1 > self.p2:
                resultado = f"Has ganado: {nombre1}, puntos: {self.p1}"
            elif self.p1 < self.p2:
                resultado = f"Has ganado: {nombre2}, puntos: {self.p2}"
            else:
                resultado = f"Empate: {nombre1}, puntos: {self.p1} - {nombre2}, puntos: {self.p2}"
        print(resultado)
        return resultado
    




    #Metodo que lleva el control de las jugadas de la CPU
    def CPU(self,fila,columna,modo):
        posicion = []
        #La dificultad dependerá de lo que elija el usuario
        match modo:
            case "FACIL":
                #elige dos cartas
                for n in range(2):
                    #si la posicion que elige esta sin descubrir da la vuelta a la carta y sale del while sino sigue generando posiciones
                    while True:
                        fila_aleatoria = random.randint(0, fila-1)
                        columna_aleatoria = random.randint(0, columna-1)
                        if self.tablero_jugador[fila_aleatoria][columna_aleatoria] == '+':
                            self.tablero_jugador[fila_aleatoria][columna_aleatoria] = self.tablero_original[fila_aleatoria][columna_aleatoria]
                            posicion.append(fila_aleatoria)
                            posicion.append(columna_aleatoria)
                            print("La máquina elige la fila: ", fila_aleatoria + 1, " y la columna: ", columna_aleatoria + 1, "...(enter)")
                            input()
                            break
                    self.mostrar_tablero_jugador(fila,columna)
                #si las claves son iguales devuelve True sino las vuelve a tapar  
                if self.lista_claves[posicion[0]][posicion[1]] == self.lista_claves[posicion[2]][posicion[3]]:
                    return True
                else:
                    self.tablero_jugador[posicion[0]][posicion[1]] = "+"
                    self.tablero_jugador[posicion[2]][posicion[3]] = "+"
                    print("Ha fallado la maquina...(enter)")
                    input()
                    for i in range(20):
                        print()
                    return False
            #caso normal   
            case "NORMAL":
                k = 0
                #si se tiene cuatro claves registradas en el array entra
                if len(self.lista_claves_cpu) >= 4:
                    while k < len(self.lista_claves_cpu):
                        f1 = 0
                        c1 = 0
                        f2 = 0
                        c2 = 0
                        v = 0
                        #dos for para recorrer el array de claves y de las claves de la cpu, guarda las dos posiciones donde se encuentra esa clave
                        for i in range(fila):
                            for j in range(columna):
                                if self.lista_claves[i][j] == self.lista_claves_cpu[k]:
                                    if v == 0:
                                        f1 = i
                                        c1 = j
                                        v += 1
                                    else:
                                        f2 = i
                                        c2 = j
                                        break
                        #si en el tablero de la cpu ya está destapada las dos cartas entra
                        if self.tablero_cpu[f1][c1] != '+' and  self.tablero_cpu[f2][c2] != '+':
                            #si una de las parejas está tapada entra y devuelve true       
                            if self.tablero_jugador[f1][c1] == '+':
                                self.tablero_jugador[f1][c1] =  self.tablero_original[f1][c1]
                                self.tablero_jugador[f2][c2] =  self.tablero_original[f2][c2]
                                print("La máquina ha recordado donde hay dos cartas iguales fila: ", f1+1, " columna: ", c1+1, " y fila:", f2+1, " columna: ", c2+1 )
                                self.mostrar_tablero_jugador(fila,columna)
                                input()
                                self.lista_claves_cpu = []
                                self.vaciar_maquina(fila,columna)
                                return True
                        else:
                            k += 1
                for n in range(2):
                    while True:
                        fila_aleatoria = random.randint(0, fila-1)
                        columna_aleatoria = random.randint(0, columna-1)
                        if self.tablero_jugador[fila_aleatoria][columna_aleatoria] == '+':
                            self.tablero_jugador[fila_aleatoria][columna_aleatoria] = self.tablero_original[fila_aleatoria][columna_aleatoria]
                            posicion.append(fila_aleatoria)
                            posicion.append(columna_aleatoria)
                            print("La máquina elige la fila: ", fila_aleatoria + 1, " y la columna: ", columna_aleatoria + 1, "...(enter)")
                            input()
                            break
                    self.mostrar_tablero_jugador(fila,columna)  
                if self.lista_claves[posicion[0]][posicion[1]] == self.lista_claves[posicion[2]][posicion[3]]:
                    return True
                else:
                    self.lista_claves_cpu.append(self.lista_claves[posicion[0]][posicion[1]])
                    self.lista_claves_cpu.append(self.lista_claves[posicion[2]][posicion[3]])
                    #desvela las claves en el tablero de la cpu
                    self.tablero_cpu[posicion[0]][posicion[1]] = self.lista_claves[posicion[0]][posicion[1]]
                    self.tablero_cpu[posicion[2]][posicion[3]] = self.lista_claves[posicion[2]][posicion[3]]

                    self.tablero_jugador[posicion[0]][posicion[1]] = "+"
                    self.tablero_jugador[posicion[2]][posicion[3]] = "+"
                    print("Ha fallado la maquina...(enter)")
                    input()
                    for i in range(1):
                        print()
                    return False
            
                    
    #metodo que controla la partida del jugador contra la cpu, igual que PJVSPJ
    def PJVsCPU(self,fila,columna,nombre1,modo):
        if self.llenar_tablero(fila, columna) is True:
            parejas = int((fila*columna)/2)
            while self.p1 + self.p2 < parejas:
                while self.p1 + self.p2 < parejas and self.comprobar_posicion(fila,columna,nombre1) is True:
                    print("Has acertado la pareja!!!")
                    self.p1 += 1
                while self.p1 + self.p2 < parejas and self.CPU(fila,columna,modo) is True:
                    self.p2 += 1
                    print("La maquina ha hecho pareja")
            if self.p1 > self.p2:
                resultado = f"Has ganado: {nombre1}, puntos: {self.p1}"
            elif self.p1 < self.p2:
                resultado = f"Ha ganado la máquina, puntos: {self.p2}"
            else:
                resultado = f"Empate: {nombre1}, puntos: {self.p1} - máquina, puntos: {self.p2}"
        print(resultado)
        return resultado
    
    #metodo que lleva el control de la cpu contra otra cpu al igual que PJVSPJ
    def CPUVsCPU(self,fila,columna,modo):
        if self.llenar_tablero(fila, columna) is True:
            parejas = int((fila*columna)/2)
            while self.p1 + self.p2 < parejas:
                while self.p1 + self.p2 < parejas and self.CPU(fila,columna,modo) is True:
                    self.p1 += 1
                    print("La maquina 1 ha hecho pareja")
                while self.p1 + self.p2 < parejas and self.CPU(fila,columna,modo) is True:
                    self.p2 += 1
                    print("La maquina 2 ha hecho pareja")
            if self.p1 > self.p2:
                resultado = f"Ha ganado: la maquina 1, puntos: {self.p1}"
            elif self.p1 < self.p2:
                resultado = f"Ha ganado la máquina 2, puntos: {self.p2}"
            else:
                resultado = f"Empate: máquina 1, puntos: {self.p1} - máquina 2, puntos: {self.p2}"
        print(resultado)
        return resultado
    
    #metodo que controla todo el juego
    def play(self):
        opcion = 6
        print("¡Bienvenido a Memory!")
        nombre = input("Dime tu nombre: ")
        jugador = Jugador(nombre)
        #si el usurio no introduce un 0 el juego sigue en curso
        while opcion != 0:
            self.vaciar()
            print("Hola ", jugador.getNombre())
            opcion = int(input("¿Que quieres hacer?: \n 1 .Como jugar \n 2. P1 Vs P2 \n 3. P1 Vs CPU \n 4. CPU VS CPU \n 0.Salir \n"))

            match opcion:
                #imprime como se juega a memory
                case 1:
                    print("Memory es un juego de memoria como su nombre dice, puedes jugar contra otra persona, contra la máquina o la máquina contra la máquina.\nSi eliges jugar contra la máquina puedes jugar en fácil o difícil. Si eliges difícil, en el momento que hayas levantado todas las posiciones pero\nsin emparejar ninguna carta, la máquina ya sabrá sonde está cada carta y su pareja, asique, ¡TEN CUIDADO!\nElige la fila y la columna de la carta que quieres dar la vuelta, vuelve a elegir otra posición y si las dos son iguales ganas un punto y sigues jugando,\nsi fallas le toca al jugador o a la máquina.")
                    break
                #se juega a PJVSPJ si se puede crear el tablero
                case 2:
                    nombre2 = input("¿Como se llama el jugador 2?")
                    jugador2 = Jugador(nombre2)
                    while True:
                        filas = int(input("¿Cuantas filas tendrá el tablero?: "))
                        columnas = int(input("¿Cuantas columnas tendrá el tablero?: "))
                        if self.tope(filas,columnas) is False:
                            filas = int(input("¿Cuantas filas tendrá el tablero?: "))
                            columnas = int(input("¿Cuantas columnas tendrá el tablero?: "))
                        else:
                            self.PJvsPJ(filas,columnas,jugador.getNombre(),jugador2.getNombre())
                            break
                #se juega a PJVSCPU
                case 3:
                    modo = input("Que dificultad tendrá la maquina?: Fácil, Normal o  Difícil")
                    while True:
                        filas = int(input("¿Cuantas filas tendrá el tablero?: "))
                        columnas = int(input("¿Cuantas columnas tendrá el tablero?: "))
                        if self.tope(filas,columnas) is False:
                            filas = int(input("¿Cuantas filas tendrá el tablero?: "))
                            columnas = int(input("¿Cuantas columnas tendrá el tablero?: "))
                        else:
                            self.PJVsCPU(filas,columnas,nombre,modo.upper())
                            break
                #juega CPUVSCPU
                case 4:
                    modo = input("Que dificultad tendrá la maquina?: Fácil, Normal o  Difícil")
                    while True:
                        filas = int(input("¿Cuantas filas tendrá el tablero?: "))
                        columnas = int(input("¿Cuantas columnas tendrá el tablero?: "))
                        if self.tope(filas,columnas) is False:
                            filas = int(input("¿Cuantas filas tendrá el tablero?: "))
                            columnas = int(input("¿Cuantas columnas tendrá el tablero?: "))
                        else:
                            self.CPUVsCPU(filas,columnas,modo.upper())
                            break
                #sale del juego
                case 0:
                    print("¡Hasta la próxima!")
                    break
                #si introduce un numero que no está entre 0 y 4, vuelve a pedir otro
                case _:
                    print ("No hay esa opción")
                    break