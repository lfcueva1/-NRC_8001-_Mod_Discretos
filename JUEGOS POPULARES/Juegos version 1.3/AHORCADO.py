import os #importamos os para usar la funcion os.system("pause") y os.system("cls")
import time #importamos time para usar la funcion time.sleep
import random #importamos random para usar la funcion de generar nuemros aleatorios
import sys #importamos sys para usar sys.exit()

"""
Ahorcado, es un juego de adivinanzas, consiste en pensar una letra por cada intento para tratar de adivinar la palabra 
dentro de un cierto numero de oportunidades
Autores:
Luis Fernando Cueva Flores
Lisbeth Adali Carvajal Escobar
Erick Patricio Ramirez Ortiz
Verisión:
VER.1.3
"""
def imprimir_menu():
    '''
    Imprime el menu de opciones en donde el jugador indicará con la que desea jugar

    Parametros:
    ------------
        Esta funcion no tiene parametros.
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.

    '''
    #mensaje que imprime inicio del juego
    print("\x1b[1;33m"+"EMPEZANDO EL JUEGO...") 
    #hacemos que se agregue un retraso a la ejecucion del codigo
    time.sleep(1) 
    #imprimimos el nombre del jugar preguntandole con que categoria desea jugar en color verde
    print(chr(27)+"[1;32m"+"",nombre_jugador,",Con que categoria de palabras desea jugar?") 
    #con esta linea de ahora en adelante se imprimira las letras en color cian
    print("\033[;36m")

    #en las siguientes 3 lineas imprimimos las opciones que el jugador podra elegir para jugar
    print("1. Frutas")
    print("2. Instrumentos musicales")
    print("3. colores")
def dibujo_presentacion_del_juego():
    '''
    Imprime el muñeco del ahorcado en blanco que se usara al inicio del juego

    Parametros:
    ------------
        Esta funcion no tiene parametros.
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    print(chr(27)+"[1;37m") #blanco
    print("   ┌-------------------------")
    print("   |                        |")
    print("   |                        |")
    print("   |                      █████")
    print("   |                     ███████")
    print("   |                      █████")
    print("   |                        █")
    print("   |                  █▀▀▀▀▀█▀▀▀▀▀█")
    print("   |                  █     █     █")
    print("   |                        █      ")
    print("   |                        █      ")
    print("   |                       █ █     ")
    print("   |                      █   █")
    print("   |                     █     █")
    print("   |                   ▀▀▀     ▀▀▀")
    print("███████")
    print("███████")


def mensaje_ganador():
    '''
    Imprime en letres gigantes "GANASTE" en color verde"
    Parametros:
    ------------
        Esta funcion no tiene parametros.
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    print(chr(27)+"[1;32m")#verde
    print("███████████   ███████████   ██         ██   ███████████   ███████████   ███████████   ███████████")
    print("██            ██       ██   ████       ██   ██       ██   ██                ██        ██")
    print("██            ██       ██   ██ ██      ██   ██       ██   ██                ██        ██")
    print("██            ██       ██   ██  ██     ██   ██       ██   ██                ██        ██")
    print("██     ████   ███████████   ██   ██    ██   ███████████   ███████████       ██        ███████████")
    print("██       ██   ██       ██   ██    ██   ██   ██       ██            ██       ██        ██")
    print("██       ██   ██       ██   ██     ██  ██   ██       ██            ██       ██        ██")
    print("██       ██   ██       ██   ██      ██ ██   ██       ██            ██       ██        ██")
    print("███████████   ██       ██   ██       ████   ██       ██   ███████████       ██        ███████████")

def ingreso_nombre_de_jugadores(nombreJugador):
    '''
    Funcion que permite al jugador ingresar su nombre dentro del juego 
    Parametros:
    ------------
        nombreJugador : lista
            Variable donde se guardara la cadena que ingrese el jugador
    
    Retorna:
    ------------
        Retorna la variable nombreJugador como str.
       
    '''
    
    #imprime en color cian
    print(chr(27)+"[;36m") 
    #Variable donde se ingresa el nombre del jugador
    nombreJugador=input("Ingrese nombre del jugador:")
    #limpia la pantalla
    os.system("cls")
    return nombreJugador

def validacion_de_la_opcion_menu():
    '''
    Funcion donde se valida si el numero ingresado por el jugador es entero, si lo que se ingresó no es un numero
    entero entonces el jugador tendra que volver a ingresar un dato hasta que sea entero
    
    Parametros:
    ------------
        Esta funcion no tiene parametros.
    Retorna:
    ------------
        Retorna la variable categoria como int.
    '''
    #para validar usamos un ciclo for donde mientras sea verdad:
    while True:
        try:
            #ingresamos un numero
            categoria=int(input("Elija una opcion: "))
            #rompemos ciclo repetitivo
            break
        #si ve que lo que se ha ingresado no es un numero entero entonces imprimira un mensaje de error
        except ValueError: 
            print("No ha ingresado un numero entero.")
    #una vez que el numero sea validado entonces se retornara el numero entero para ser usado en el main
    return categoria 

def validar_letra_ingresada_por_el_usuario(letra):
    '''
    Funcion donde se valida que se ingrese solo un caracter, en caso de recibir mas de uno entonces esta funcion volvera a pedir
    que se ingrese de nuevo un caracter hasta romper el ciclo

    Parametros:
    ------------
        str : lista
            Variable que recibe la cadena de caracteres
    Retorna:
    ------------
        Retorna letra como str
    '''
    
    #Mientras el tamaño de letra es diferente de uno entonces tendra que volver a ingresar un caracter
    while len(letra) != 1:
        letra = input('Ingrese una letra por favor: ')
    return letra

def imprimir_tamaño_letras(letras):
    '''
    Funcion que imprimira el numero de letras que el jugador debera adivinar

    Parametros:
    ------------
        letras : lista.
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    #En este for segun el numero de letras que hay que adivinar se imprimira el caracter '-' para que el jugador sepa cuantas letras debe adivinar
    for i in range(len(letras)):
        print("- ",end="")
    #imprimimos un salto de linea
    print("")

def llenar_lista_letras(letras):
    '''
    Funcion que llenara la lista letras con el caracter '-' segun el numero de letras existentes

    Parametros:
    ------------
        letras : lista.
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    #For que sirve para agregar el caracter '-' a la lista letras segun el numero de letras de la palabra escogida al azar
    for i in range(len(letras)):
        letras_correctas.append("-")
def dibujo_letra_equivocada(numero_intentos):
    '''
    Imprime el muñeco del ahorcado en rojo segun el numero de fallos al tratar de adiviar una letra

    Parametros:
    ------------
        numero_intentos : int.
    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
    if(numero_intentos==1):
        print(chr(27)+"[1;37m") #blanco
        print("   ┌-------------------------")
        print("   |                        |")
        print("   |                        |")
        print("   |                      █████")
        print("   |                     ███████")
        print("   |                      █████")
        print("   |                        █")
        print("   |                  █▀▀▀▀▀█▀▀▀▀▀█")
        print("   |                  █     █     █")
        print("   |                        █      ")
        print("   |                        █      ")
        print("   |                       █ █     ")
        print("   |                      █   █")
        print(chr(27)+"[1;31m",end="") #rojo
        print("   |                     █     █")
        print("   |                   ▀▀▀     ▀▀▀")
        print("███████")
        print("███████")
    if(numero_intentos==2):
        print(chr(27)+"[1;37m") #blanco
        print("   ┌-------------------------")
        print("   |                        |")
        print("   |                        |")
        print("   |                      █████")
        print("   |                     ███████")
        print("   |                      █████")
        print("   |                        █")
        print("   |                  █▀▀▀▀▀█▀▀▀▀▀█")
        print("   |                  █     █     █")
        print("   |                        █      ")
        print("   |                        █      ")
        print(chr(27)+"[1;31m",end="") #rojo
        print("   |                       █ █     ")
        print("   |                      █   █")
        print("   |                     █     █")
        print("   |                   ▀▀▀     ▀▀▀")
        print("███████")
        print("███████")
    if(numero_intentos==3):
        print(chr(27)+"[1;37m") #blanco
        print("   ┌-------------------------")
        print("   |                        |")
        print("   |                        |")
        print("   |                      █████")
        print("   |                     ███████")
        print("   |                      █████")
        print("   |                        █")
        print("   |                  █▀▀▀▀▀█▀▀▀▀▀█")
        print("   |                  █     █     █")
        print(chr(27)+"[1;31m",end="") #rojo
        print("   |                        █      ")
        print("   |                        █      ")
        print("   |                       █ █     ")
        print("   |                      █   █")
        print("   |                     █     █")
        print("   |                   ▀▀▀     ▀▀▀")
        print("███████")
        print("███████")
    if(numero_intentos==4):
        print(chr(27)+"[1;37m") #blanco
        print("   ┌-------------------------")
        print("   |                        |")
        print("   |                        |")
        print("   |                      █████")
        print("   |                     ███████")
        print("   |                      █████")
        print("   |                        █")
        print(chr(27)+"[1;31m",end="") #rojo
        print("   |                  █▀▀▀▀▀█▀▀▀▀▀█")
        print("   |                  █     █     █")
        print("   |                        █      ")
        print("   |                        █      ")
        print("   |                       █ █     ")
        print("   |                      █   █")
        print("   |                     █     █")
        print("   |                   ▀▀▀     ▀▀▀")
        print("███████")
        print("███████")
    if(numero_intentos==5):
        print(chr(27)+"[1;37m") #blanco
        print("   ┌-------------------------")
        print("   |                        |")
        print("   |                        |")
        print("   |                      █████")
        print("   |                     ███████")
        print(chr(27)+"[1;31m",end="") #rojo
        print("   |                      █████")
        print("   |                        █")
        print("   |                  █▀▀▀▀▀█▀▀▀▀▀█")
        print("   |                  █     █     █")
        print("   |                        █      ")
        print("   |                        █      ")
        print("   |                       █ █     ")
        print("   |                      █   █")
        print("   |                     █     █")
        print("   |                   ▀▀▀     ▀▀▀")
        print("███████")
        print("███████")
    if(numero_intentos==6):
        print(chr(27)+"[1;31m") #rojo
        print("   ┌-------------------------")
        print("   |                        |")
        print("   |                        |")
        print("   |                      █████")
        print("   |                     ███████")
        print("   |                      █████")
        print("   |                        █")
        print("   |                  █▀▀▀▀▀█▀▀▀▀▀█")
        print("   |                  █     █     █")
        print("   |                        █      ")
        print("   |                        █      ")
        print("   |                       █ █     ")
        print("   |                      █   █")
        print("   |                     █     █")
        print("   |                   ▀▀▀     ▀▀▀")
        print("███████")
        print("███████")

        print("")
        print("█████████     ███████████    ███████████      ██████████     ██████████████   ██████████████    ██████████████    ███████████")
        print("██       ██   ██             ██         ██    ██       ██          ██         ██                      ██          ██")
        print("██        ██  ██             ██          ██   ██        ██         ██         ██                      ██          ██")
        print("██      ██    ██             ██         ██    ██         ██        ██         ██                      ██          ██")
        print("████████      ███████████    ████████████     ██         ██        ██         ██████████████          ██          ███████████")
        print("██            ██             ██    ██         ██         ██        ██                     ██          ██          ██")
        print("██            ██             ██     ██        ██         ██        ██                     ██          ██          ██")
        print("██            ██             ██      ██       ██       ██          ██                     ██          ██          ██")
        print("██            ███████████    ██       ██      ██████████     ██████████████   ██████████████          ██          ███████████")
        sys.exit()

if __name__ == '__main__':
    #esta servira para ingresar el nombre del jugador
    nombre_jugador = ""

    #las 3 siguientes listas son donde guardaremos las palabras que usaremos para el juego
    categoria_frutas = ["manzana","naranja","platano","cerezas","pera","granadilla","papaya","frutilla","kiwi","sandia"]
    categoria_instrumentos = ["guitarra","trompeta","saxofon","acordeon","arpa","flauta","piano","violin","tambor","xilofono"]
    categoria_colores = ["morado","amarillo","azul","marron","cafe","celeste","cian","fuxia","gris","purpura"]

    #esta funcion limpia la pantalla
    os.system("cls")
    #Imprime la bienvenida en color amarillo
    print(chr(27)+"[1;33m"+"BIENVENIDO(S) AL JUEGO DEL AHORCADO!") 
    #imprime el dibujo que aparecera al inicio del juego
    dibujo_presentacion_del_juego()
    #imprime el maximo de jugadores en color rojo
    print(chr(27)+"[1;31m"+"(MAXIMO 1 JUGADOR))")
     #con esta linea de ahora en adelante se imprimira las letras en color cian
    print(chr(27)+"[;36m")
    #en la variable "nombre_jugador" usaremos una funcion donde ingresaremos una cadena de caracteres la cual sera el nombre del jugador
    nombre_jugador = ingreso_nombre_de_jugadores(nombre_jugador)
    imprimir_menu()
    #en la variable opcionMenu la igualaremos a la funcion donde se ingresar un numero entero y este sea validado
    opcionMenu=validacion_de_la_opcion_menu()

    #en este ciclo repetitivo preguntamos si es que la variable opcionMenu(numero entero) es menor a 1 o mayor a 3 entonces la volveremos a ingresar hasta que rompa el ciclo repetitivo
    while(opcionMenu<1 or opcionMenu>3):
        opcionMenu=validacion_de_la_opcion_menu()

    #este print sirve para pintar las letras de color amarillo
    print(chr(27)+"[1;33m") 
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    
    #si el jugador elige jugar con frutas entonces
    if opcionMenu==1:
        #empezaremos con 0 en el numero de intentos para luego sumarle 1 hasta llegar al 6
        numero_intentos=0 
        #aqui es donde el programa elegira una de las 10 palabras que se encuentren dentro de la categoria frutas
        numero = random.randint(0, 9)
        #en la variable "palabra" es donde guardaremos la palabra escogida al azar por el programa que esta dentro de la categoria frutas
        palabra=categoria_frutas[numero]
        #declaramos la lista "letras" la cual usaremos en el siguiente for
        letras=[]

        #en este for usaremos la funcion letra donde separara la variable palabra en letras y una vez este separada cada una
        #sera guardada en la lista letras con la ayuda de la funcion .append()
        for letra in palabra: 
            letras.append(letra)
        
        print("ADIVINA LA PALABRA:")
        #volvemos a imprimir el dibujo del muñeco del ahorcado en blanco para indicar que ha empezado el juego
        dibujo_presentacion_del_juego()
        #print para imprimir de ahora en adelante en color amarillo
        print(chr(27)+"[1;33m") 

        #Segun el numero de letras imprimira el caracter ´-´
        imprimir_tamaño_letras(letras)
        
        #declaramos la variable letras_correctas como lista en donde cada vez que se acierte una letra sera agregada a esta lista
        letras_correctas=[]
        
        #llenara la lista letras con el caracter '-' segun el numero de letras existentes
        llenar_lista_letras(letras)
            
        #aqui decimos que mientras el numero de intentos sea menor o igual a 6 entonces
        while numero_intentos<=6:
            #aqui ingresamos la letra pero usamos la funcion validar_letra_ingresada_por_el_usuario
            #para que solo pueda ingresar una letra y encaso de ingresar mas de dos caracteres el programa
            #volvera a pedir que ingrese una letra
            letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                                                
            #imprimimos salto de linea
            print("")

            #En este for ponemos un condicional if donde la letra que ingresó el jugador se encuentra dentro de la lista "letras" en donde esta la palabra
            #a adivinar entonces lo que se ingreso se guardara en la lista letras correctas reemplazando el caracter '-' por la letra que ingreso el jugador
            #e imprimimos la lista "letras_correctas"
            for i in range(len(letras)):
                if(letraJugador==letras[i]):
                    letras_correctas[i]=letraJugador
                    print(letras_correctas)
                    
                #una vez que el usuario haya ingresado las letras y todas sean correctas entonces imprimiremos el mensaje ganador siempre y cuando el numero de
                #intentos sea menos o igual a 6 y usaremos el comando sys.exit() para termianr la ejecucion del programa
                if(letras_correctas==letras):
                    mensaje_ganador()
                    sys.exit()
                
                #si el jugador ingresa una letra que no este en la palabra para adivinar entonces aumentaremos 1 mas al numero de intentos y:
                if(letraJugador not in letras):
                    numero_intentos=numero_intentos+1
                    #segun el numero de intentos se imprimira un muñeco que dependiendo del fallo se imprimira en rojo en ciertas partes del cuerpo
                    if(numero_intentos==1 or numero_intentos==2 or numero_intentos==3 or numero_intentos==4 or numero_intentos==5 ):
                        dibujo_letra_equivocada(numero_intentos)
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    
                    #si el numero de intentos es 6 se imprimira el dibujo del muñeco del ahorcado en rojo y un mensaje que dice "perdiste"
                    #y se terminara la ejecucion del programa con el comando sys.exit()
                    elif(numero_intentos==6):
                        dibujo_letra_equivocada(numero_intentos)
    #si el jugador elige jugar con instrumentos musicales entonces
    if opcionMenu==2: 
        #empezaremos con 0 en el numero de intentos para luego sumarle 1 hasta llegar al 6
        numero_intentos=0
        #aqui es donde el programa elegira una de las 10 palabras que se encuentren dentro de la categoria de instrumentos musicales
        numero = random.randint(0, 9)
        palabra=categoria_instrumentos[numero]#en la variable "palabra" es donde guardaremos la palabra escogida al azar por el programa que esta dentro de la categoria instrumentos musicales
        letras=[]#declaramos la lista "letras" la cual usaremos en el siguiente for
        
        #en este for usaremos la funcion letra donde separara la variable palabra en letras y una vez este separada cada una
        #sera guardada en la lista letras con la ayuda de la funcion .append()
        for letra in palabra:
            letras.append(letra)
        
        print("ADIVINA LA PALABRA:")
        #volvemos a imprimir el dibujo del muñeco del ahorcado en blanco para indicar que ha empezado el juego
        dibujo_presentacion_del_juego()
        #print para imprimir de ahora en adelante en color amarillo
        print(chr(27)+"[1;33m") 
        #Segun el numero de letras imprimira el caracter ´-´
        imprimir_tamaño_letras(letras)
        #declaramos la variable letras_correctas como lista en donde cada vez que se acierte una letra sera agregada a esta lista
        letras_correctas=[]
        #llenara la lista letras con el caracter '-' segun el numero de letras existentes
        llenar_lista_letras(letras)
        
        #aqui decimos que mientras el numero de intentos sea menor o igual a 6 entonces
        while numero_intentos<=6:
            #aqui ingresamos la letra pero usamos la funcion validar_letra_ingresada_por_el_usuario
            #para que solo pueda ingresar una letra y encaso de ingresar mas de dos caracteres el programa
            #volvera a pedir que ingrese una letra
            letraJugador=validar_letra_ingresada_por_el_usuario('aa')
            #imprimimos salto de linea
            print("")

            #En este for ponemos un condicional if donde la letra que ingresó el jugador se encuentra dentro de la lista "letras" en donde esta la palabra
            #a adivinar entonces lo que se ingreso se guardara en la lista letras correctas reemplazando el caracter '-' por la letra que ingreso el jugador
            #e imprimimos la lista "letras_correctas"
            for i in range(len(letras)):
                if(letraJugador==letras[i]):
                    letras_correctas[i]=letraJugador
                    print(letras_correctas)
                    
                #una vez que el usuario haya ingresado las letras y todas sean correctas entonces imprimiremos el mensaje ganador siempre y cuando el numero de
                #intentos sea menos o igual a 6 y usaremos el comando sys.exit() para termianr la ejecucion del programa
                if(letras_correctas==letras):
                    mensaje_ganador()
                    sys.exit()
                #si el jugador ingresa una letra que no este en la palabra para adivinar entonces aumentaremos 1 mas al numero de intentos y:
                if(letraJugador not in letras):
                    numero_intentos=numero_intentos+1
                    #segun el numero de intentos se imprimira un muñeco que dependiendo del fallo se imprimira en rojo en ciertas partes del cuerpo
                    if(numero_intentos==1 or numero_intentos==2 or numero_intentos==3 or numero_intentos==4 or numero_intentos==5):
                        dibujo_letra_equivocada(numero_intentos)
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    elif(numero_intentos==6):
                        dibujo_letra_equivocada(numero_intentos)
    #si el jugador elige jugar con colores entonces
    if opcionMenu==3:
        #empezaremos con 0 en el numero de intentos para luego sumarle 1 hasta llegar al 6
        numero_intentos=0
        #aqui es donde el programa elegira una de las 10 palabras que se encuentren dentro de la categoria colores
        numero = random.randint(0, 9)
        #en la variable "palabra" es donde guardaremos la palabra escogida al azar por el programa que esta dentro de la categoria colores
        palabra=categoria_colores[numero]
        #declaramos la lista "letras" la cual usaremos en el siguiente for
        letras=[]
        
        #en este for usaremos la funcion letra donde separara la variable palabra en letras y una vez este separada cada una
        #sera guardada en la lista letras con la ayuda de la funcion .append()
        for letra in palabra:
            letras.append(letra)
        
        print("ADIVINA LA PALABRA:")
        #volvemos a imprimir el dibujo del muñeco del ahorcado en blanco para indicar que ha empezado el juego
        dibujo_presentacion_del_juego()
        #print para imprimir de ahora en adelante en color amarillo
        print(chr(27)+"[1;33m") 
        #Segun el numero de letras imprimira el caracter ´-´
        imprimir_tamaño_letras(letras)
        
        #declaramos la variable letras_correctas como lista en donde cada vez que se acierte una letra sera agregada a esta lista
        letras_correctas=[]
        #Para este for segun el tamaño de la lista(letras) donde es el numero de letras que tiene la palabra
        #llenara la lista letras con el caracter '-' segun el numero de letras existentes
        llenar_lista_letras(letras)
        #aqui decimos que mientras el numero de intentos sea menor o igual a 6 entonces
        while numero_intentos<=6:
            #aqui ingresamos la letra pero usamos la funcion validar_letra_ingresada_por_el_usuario
            #para que solo pueda ingresar una letra y encaso de ingresar mas de dos caracteres el programa
            #volvera a pedir que ingrese una letra
            letraJugador=validar_letra_ingresada_por_el_usuario('aa')
            #imprimimos salto de linea
            print("")

            #En este for ponemos un condicional if donde la letra que ingresó el jugador se encuentra dentro de la lista "letras" en donde esta la palabra
            #a adivinar entonces lo que se ingreso se guardara en la lista letras correctas reemplazando el caracter '-' por la letra que ingreso el jugador
            #e imprimimos la lista "letras_correctas"
            for i in range(len(letras)):
                if(letraJugador==letras[i]):
                    letras_correctas[i]=letraJugador
                    print(letras_correctas)
                    
                #una vez que el usuario haya ingresado las letras y todas sean correctas entonces imprimiremos el mensaje ganador siempre y cuando el numero de
                #intentos sea menos o igual a 6 y usaremos el comando sys.exit() para termianr la ejecucion del programa
                if(letras_correctas==letras):
                    mensaje_ganador()
                    sys.exit()
                #si el jugador ingresa una letra que no este en la palabra para adivinar entonces aumentaremos 1 mas al numero de intentos y:
                if(letraJugador not in letras):
                    numero_intentos=numero_intentos+1
                    #segun el numero de intentos se imprimira un muñeco que dependiendo del fallo se imprimira en rojo en ciertas partes del cuerpo
                    if(numero_intentos==1 or numero_intentos==2 or numero_intentos==3 or numero_intentos==4 or numero_intentos==5):
                        dibujo_letra_equivocada(numero_intentos)
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    elif(numero_intentos==6):
                        dibujo_letra_equivocada(numero_intentos)      
        print("")  
        #imprimimos la lista letras para ver como termino el juego
        print(letras)
