import random

emojis = {1:"😀",2:"🥰",3:"😨",4:"🥶",5:"🦍",6:"👾",7:"🐲",
        8:"😡",9:"🦘",10:"🐳",11:"🐼",12:"🐺",13:"🦃",14:"🤢",15:"😎"}
tablero_original = []
tablero_jugador = []
usados = []

# Metodo que recibe por parametro el numero de filas y de columnas, si excede las 6 filas y 5 columnas o viceversa devuelve false.
# Devuelve tambien false si el tamaño no es par o en menor que 2x2.
def max(fila,columna):
    if fila < 2 or columna < 2:
        return False
    if (fila <= 6 and columna <= 5) or (fila <= 5 and columna <= 6):
        if (fila * columna) % 2 == 0:
            return True
        else:
            return False
    else:
        return False

#Crea dos tableros "vacios" segun las filas y columnas que haya pedido el usuario.
def crear_tablero(fila,columna):
    if max(fila,columna) == True:
        for i in range(fila):
            rows = []
            for j in range(columna):
                rows.append("+")
            tablero_jugador.append(rows)
            tablero_original.append(rows)
        return True
    else:
        return False

#Metodo que genera un emoji aleatorio del diccionario pero si la clave ya esta guardado en la lista usados vuelve a generar otro emoji distintinto
def random_emoji():
    while True:
        n = random.randint(1, 15)
        emoji_aleatorio = emojis[n]
        
        if n not in usados:
            usados.append(n)
            return emoji_aleatorio
        else:
            n = random.randint(1, len(emojis))
            emoji_aleatorio = emojis[n]

# Metodo que comprueba primero si el tablero se ha podido crear y si es asi rellena el tablero de emojis de forma aleatoria con el metodo "random_emoji()", 
# genera una posicion aleatoria una vez ya tiene el emoji generado, si la posicion no esta vacia genera otra posicion, y asi hasta generar una posicion que este vacia. 
# No se genera otro emoji hasta que se han llenado dos posiciones con el mismo emoji.
def llenar_tablero(fila,columna):
    if crear_tablero(fila,columna) is True:
        for i in range(int((fila*columna)/2)):
            emoji_aleatorio = random_emoji()
            for n in range(2):
                while True:
                    fila_aleatoria = random.randint(0,fila-1)
                    columna_aleatoria = random.randint(0,columna-1)
                    if tablero_original[fila_aleatoria][columna_aleatoria] != '+':
                        fila_aleatoria = random.randint(0,fila-1)
                        columna_aleatoria = random.randint(0,columna-1)
                    else:
                        tablero_original[fila_aleatoria][columna_aleatoria] = emoji_aleatorio
                        break


def mostrar_tablero_original(fila,columna):
    if crear_tablero(fila,columna) is True:
        llenar_tablero(fila,columna)
        for i in tablero_original:
            for j in i:
                print(j, end= "   ")
            print()

mostrar_tablero_original(5,2)