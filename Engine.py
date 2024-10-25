import random

emojis = {1:"😀",2:"🥰",3:"😨",4:"🥶",5:"🦍",6:"👾",7:"🐲",
        8:"😡",9:"🦘",10:"🐳",11:"🐼",12:"🐺",13:"🦃",14:"🐫",15:"😎"}
tablero_original = []
tablero_jugador = []

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
def tablero_vacio(fila,columna):
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



def llenar_tablero(fila,columna):
    if tablero_vacio(fila,columna) is True:
        for i in range(int((fila*columna)/2)):
            n = int(random.randint(1,len(emojis)))
            emoji_aleatorio = emojis.get(n)
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


llenar_tablero(5,2)
print(tablero_original)
print(tablero_jugador)