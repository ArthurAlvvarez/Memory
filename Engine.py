import random

emojis = {1:"😀",2:"🥰",3:"😨",4:"🥶",5:"🦍",6:"👾",7:"🐲",
        8:"😡",9:"🦘",10:"🐳",11:"🐼",12:"🐺",13:"🦃",14:"🐫",15:"😎"}
tablero = [[],[]]

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

def tablero_vacio(fila,columna):
    if max(fila,columna) == True:
        for i in range(len(fila)):
            for j in range(len(columna)):
                tablero[[]].append(0)



def crear_tablero(fila,columna):
    if max(fila,columna) == True:
        for i in range((fila*columna)/2):
            numero_aleatorio = random.randint(1,len(emojis))
            for j in range(2):
                f1 = random.randint(0,fila-1)
                c1 = random.randint(0,columna-1)
                if tablero[f1][c1] != 0:
                    tablero[f1][c1] = emojis.get(numero_aleatorio)

print(tablero)