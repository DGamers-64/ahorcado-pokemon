import getpass

def preguntar_modo():
    print("¿Qué modo quieres jugar?")
    print("1. Aleatorio")
    print("2. Definido por rival")
    modo = int(input("Elige: "))
    if(modo != 1 and modo != 2):
        print("Respuesta no válida")
        modo = preguntar_modo()
    return modo

def preguntar_seguir_jugando():
    print('--------------------')
    respuesta = input("¿Quieres seguir jugando? (y/n) ")
    print('--------------------')
    if(respuesta != 'y' and respuesta != 'n'):
        print("Respuesta no válida")
        respuesta = preguntar_seguir_jugando()
        return respuesta
    return respuesta

####################################################

def imprimir_tablero(palabra, letras):
    for i in palabra:
        if(i in letras):
            print(i, end=" ")
        else:
            print("_", end=" ")
    print()
    print()
    for i in letras:
        if(i not in palabra):
            print(i, end=" ")
    print()
    return True

####################################################

def preguntar_letra(letras):
    letra = input("Dime una letra: ")
    letra = letra.upper()
    letras.append(letra)
    return letras

def comprobar_resultado(palabra, letras):
    errores = 0
    correcto = 0
    for i in letras:
        if(i not in palabra):
            errores += 1
        else:
            correcto += 1
    return correcto, errores

def aleatorio():
    return

def versus():
    pokemon = getpass.getpass("Introduce un Pokémon: ")
    generacion = getpass.getpass("Introduce la generación: ")
    tipo = getpass.getpass("Introduce el tipo: ")
    tipo = tipo.upper()
    pokemon = pokemon.upper()
    errores = 0
    completado = False
    letras = []
    while(errores < 7 and completado != True):
        print('--------------------')
        imprimir_tablero(pokemon, letras)
        if(errores == 5):
            print(generacion, "a generación", sep="")
        if(errores == 6):
            print(generacion, "a generación", sep="")
            print(tipo, "es un tipo del Pokémon")
        print('--------------------')
        letras = preguntar_letra(letras)
        correcto, errores = comprobar_resultado(pokemon, letras)
        if(correcto == len(pokemon)):
            completado = True
    if(completado == True):
        print("¡Enhorabuena, el pokémon era ", pokemon.capitalize(), "!", sep="")
    else:
        print("¡Se acabó! El pokémon era", pokemon.capitalize())
    return

def juego(modo):
    match modo:
        case 1:
            aleatorio()
        case 2:
            versus()
    return

seguir_jugando = 'y'

while(seguir_jugando == 'y'):
    modo = preguntar_modo()
    juego(modo)
    seguir_jugando = preguntar_seguir_jugando()