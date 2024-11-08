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
        self.p1 = 0
        self.p2 = 0

    def vaciar(self):
        self.tablero_original = []
        self.tablero_jugador = []
        self.lista_claves = []
        self.tablero_cpu = []
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
                self.tablero_jugador.append(rows.copy())
                self.tablero_original.append(rows.copy())
                self.lista_claves.append(rows.copy())
            return True
        else:
            return False

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

    def comprobar_posicion(self,fila,columna,nombre):
        posiciones = []
        print("Te toca ",nombre)
        self.mostrar_tablero_jugador(fila,columna)
        for i in range(2):
            f = int(input("Dime la fila: "))-1
            c = int(input("Dime la columna: "))-1
            while True:
                if f < 0 or f >= fila or c < 0 or c >= columna:
                    print("Esa posicion no está en el tablero")
                    f = int(input("Dime la fila: "))-1
                    c = int(input("Dime la columna: "))-1
                elif self.tablero_jugador[f][c] != "+":
                    print("Esta carta ya está dada la vuelta")
                    f = int(input("Dime la fila: "))-1
                    c = int(input("Dime la columna: "))-1
                elif self.tablero_jugador[f][c] == "+":
                    self.tablero_jugador[f][c] = self.tablero_original[f][c]
                    posiciones.append(f)
                    posiciones.append(c)
                    break
            self.mostrar_tablero_jugador(fila,columna) 
        if self.lista_claves[posiciones[0]][posiciones[1]] == self.lista_claves[posiciones[2]][posiciones[3]]:
            return True
        else:
            self.tablero_cpu.append(self.lista_claves[posiciones[0]][posiciones[1]])
            self.tablero_cpu.append(self.lista_claves[posiciones[2]][posiciones[3]])
            self.tablero_jugador[posiciones[0]][posiciones[1]] = "+"
            self.tablero_jugador[posiciones[2]][posiciones[3]] = "+"
            print("Has fallado...(enter)")
            input()
            for i in range(20):
                print()
            return False

    def PJvsPJ(self,fila,columna,nombre1,nombre2):
        if self.llenar_tablero(fila, columna) is True:
            parejas = int((fila*columna)/2)
            while self.p1 + self.p2 < parejas:
                while self.p1 + self.p2 < parejas and self.comprobar_posicion(fila,columna,nombre1) is True:
                    print("Has acertado la pareja!!!")
                    self.p1 += 1
                while self.p1 + self.p2 < parejas and self.comprobar_posicion(fila,columna,nombre2) is True:
                    self.p2 += 1
                    print("Has acertado la pareja!!!")
            if self.p1 > self.p2:
                resultado = f"Has ganado: {nombre1}, puntos: {self.p1}"
            elif self.p1 < self.p2:
                resultado = f"Has ganado: {nombre2}, puntos: {self.p2}"
            else:
                resultado = f"Empate: {nombre1}, puntos: {self.p1} - {nombre2}, puntos: {self.p2}"
        print(resultado)
        return resultado

    def CPU(self,fila,columna,modo):
        posicion = []
        match modo:
            case "FACIL":
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
                    self.tablero_jugador[posicion[0]][posicion[1]] = "+"
                    self.tablero_jugador[posicion[2]][posicion[3]] = "+"
                    print("Ha fallado la maquina...(enter)")
                    input()
                    for i in range(20):
                        print()
                    return False
            case "Normal":
                for n in range(2):
                    while True:
                        if len(self.tablero_cpu >= 2):
                            for i in range(len(self.tablero_cpu)):
                                #aqui tengo que encontrar el primer valor que se repita varias veces y ver en que posicion esta y si la carta no está dada la vuelta
                        else:        
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
                    self.tablero_cpu.append(self.lista_claves[posicion[0]][posicion[1]])
                    self.tablero_cpu.append(self.lista_claves[posicion[2]][posicion[3]])
                    self.tablero_jugador[posicion[0]][posicion[1]] = "+"
                    self.tablero_jugador[posicion[2]][posicion[3]] = "+"
                    print("Ha fallado la maquina...(enter)")
                    input()
                    for i in range(20):
                        print()
                    return False
                    

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
            
    def play(self):
        opcion = 6
        print("¡Bienvenido a Memory!")
        nombre = input("Dime tu nombre: ")
        jugador = Jugador(nombre)

        while opcion != 0:
            self.vaciar()
            print("Hola ", jugador.getNombre())
            opcion = int(input("¿Que quieres hacer?: \n 1 .Como jugar \n 2. P1 Vs P2 \n 3. P1 Vs CPU \n 4. CPU VS CPU \n 0.Salir \n"))

            match opcion:
                case 1:
                    print("Memory es un juego de memoria como su nombre dice, puedes jugar contra otra persona, contra la máquina o la máquina contra la máquina.\nSi eliges jugar contra la máquina puedes jugar en fácil o difícil. Si eliges difícil, en el momento que hayas levantado todas las posiciones pero\nsin emparejar ninguna carta, la máquina ya sabrá sonde está cada carta y su pareja, asique, ¡TEN CUIDADO!\nElige la fila y la columna de la carta que quieres dar la vuelta, vuelve a elegir otra posición y si las dos son iguales ganas un punto y sigues jugando,\nsi fallas le toca al jugador o a la máquina.")
                    break
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
                # case 4:

                case 0:
                    print("¡Hasta la próxima!")
                    break
                case _:
                    print ("No hay esa opción")