import random

tablero = {"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}

def tablerolleno():
    global tablero
    if " " not in list(tablero.values()):
        tablero = {"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}

def marcarX(casilla):
    if tablero.keys().__contains__(casilla):
        if tablero[casilla] == " ":
            return draw("x", casilla)
        else:
            raise ValueError("Casilla invalida")
    else:
        raise ValueError("Casilla invalida")

def marcarO(casilla):
    if tablero.keys().__contains__(casilla):
        if tablero[casilla] == " ":
            return draw("o", casilla)
        else:
            raise ValueError("Casilla invalida")
    else:
        raise ValueError("Casilla invalida")

def draw(marca, casilla):
    tablero[casilla] = marca

def table():
    return tablero["1"] + " | " + tablero["2"] + " | " + tablero["3"] + "\t\t1 | 2 | 3" + "\n" + tablero["4"] + " | " + tablero["5"] + " | " + tablero["6"] + "\t\t4 | 5 | 6" + "\n" + tablero["7"] + " | " + tablero["8"] + " | " + tablero["9"] + "\t\t7 | 8 | 9"

def winner():
    winner = status()
    if winner == "x":
        print(table())
        print(input("Lo siento jugador 2, haz perdido..."))
        clear()
        exit()
    elif winner == "o":
        print(table())
        print(input("Lo siento jugador 1, haz perdido..."))
        clear()
        exit()

def status():
    horizontal = hori()
    vertical = vert()
    diagonal = diag()
    if horizontal == "x" or horizontal == "o":
        return horizontal
    elif vertical == "x" or vertical == "o":
        return vertical
    elif diagonal == "x" or diagonal == "o":
        return diagonal

def hori():
    if tablero["1"] == tablero["2"] == tablero["3"] != " ":
        return tablero["1"]
    elif tablero["4"] == tablero["5"] == tablero["6"] != " ":
        return tablero["4"]
    elif tablero["7"] == tablero["8"] == tablero["9"] != " ":
        return tablero["7"]

def vert():
    if tablero["1"] == tablero["4"] == tablero["7"] != " ":
        return tablero["1"]
    elif tablero["2"] == tablero["5"] == tablero["8"] != " ":
        return tablero["2"]
    elif tablero["3"] == tablero["6"] == tablero["9"] != " ":
        return tablero["3"]

def diag():
    if tablero["1"] == tablero["5"] == tablero["9"] != " ":
        return tablero["1"]
    elif tablero["3"] == tablero["5"] == tablero["7"] != " ":
        return tablero["3"]

def clear() -> None:
    print('\n'*100)

def jugar():
    while True:
        print(table())
        try:
            casilla = marcarX(input("Numero ---> "))
        except ValueError:
            print(input("Casilla invalida..."))
        else:
            casilla
            clear()
            winner()
            tablerolleno()
            jugar2()
        clear()

def jugar2():
    while True:
        print(table())
        try:
            casilla = marcarO(str(random.randint(1,9)))
        except ValueError:
            print(input("Casilla invalida..."))
        else:
            casilla
            clear()
            winner()
            tablerolleno()
            jugar()
        clear()

if __name__ == '__main__':
    print("Bienvenido al tateti de mipi")
    print(input("Presiona una tecla para continuar..."))
    jugar()