"""
Módulo que agrupa las funciones que describen la lógica interna del juego
"""

from entrada import (
    pedir_entrada_numero,
    pedir_entrada_numero_delimitado,
    pedir_entrada_si_o_no,
)


def jugar_una_vez(numero, minimo, maximo):
    intento = pedir_entrada_numero_delimitado("Adivine el numero", minimo, maximo)

    # Se comprueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
        victoria = False
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
        victoria = False
    else:
        print("¡Ha ganado!")
        victoria = True
        minimo = maximo = intento
    return victoria, minimo, maximo


def pedir_entrada_del_numero_incognita(minimo, maximo):
    return pedir_entrada_numero_delimitado("Introduzca el número a adivinar",
                                        minimo, maximo)

def intentoss(nivell):
    numero_maximo_intentos=0
    if nivell==1:
        numero_maximo_intentos=5
        
    if nivell==2:
        numero_maximo_intentos=15
        
    if nivell==3:
        numero_maximo_intentos=25
        
    if nivell==4:
        numero_maximo_intentos=35
        
    return numero_maximo_intentos
def jugar_una_partida(numero, minimo, maximo):
    niv=0
    if maximo==100:
        niv=1
    if maximo==1000:
        niv=2
    if maximo==1000000:
        niv=3
    if maximo==1000000000000:
        niv=4
    intento=0
    intentosMax=intentoss(niv)
    while True:
        # Se entra en un bucle infinito
        # que permite jugar varias veces
        if intento==intentosMax:
            print("Has supèrado los intentos maximos")
            break
        victoria, minimo, maximo = jugar_una_vez(numero, minimo, maximo)
        intento+=1
        if (victoria):
            return intento


def decidir_limites():
    while True:
        minimo = pedir_entrada_numero("Quelle est la borne minimale ?")
        maximo = pedir_entrada_numero("Quelle est la borne maximale ?")
        if maximo > minimo:
            return minimo, maximo

def nivel():
    nivel=int(input("introduzca un numero del 1 al 4"))
    intentos=0
    minimo=0
    max=0
    if nivel==1:
        
        max=100
    if nivel==2:
        
        max=1000
    if nivel==3:
        
        max=1000000
    if nivel==4:
        
        max=10000000000000
    return minimo,max

def jugar():
    minimo, maximo = nivel()
    puntos={}
    while True:
        numero = pedir_entrada_del_numero_incognita(minimo, maximo)
        
        punt=jugar_una_partida(numero, minimo, maximo)
        nombre=input("introduzca su nombre:" )
        puntos[nombre]=punt
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?"):
            print("¡Hasta pronto!")
            return puntos

print(jugar())
