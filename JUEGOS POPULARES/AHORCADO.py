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
VER.1.2
"""
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

def dibujo_fallo_intento_uno():
    '''
    Imprime el muñeco del ahorcado con los pies en rojo y lo demas en blanco

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
    print(chr(27)+"[1;31m",end="") #rojo
    print("   |                     █     █")
    print("   |                   ▀▀▀     ▀▀▀")
    print("███████")
    print("███████")
def dibujo_fallo_intento_dos():
    '''
    Imprime el muñeco del ahorcado con la cintura hacia abajo en rojo y lo demas en blanco

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
    print(chr(27)+"[1;31m",end="") #rojo
    print("   |                       █ █     ")
    print("   |                      █   █")
    print("   |                     █     █")
    print("   |                   ▀▀▀     ▀▀▀")
    print("███████")
    print("███████")

def dibujo_fallo_intento_tres():
    '''
    Imprime el muñeco del ahorcado con el torso hacia abajo en rojo y lo demas en blanco

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
    print(chr(27)+"[1;31m",end="") #rojo
    print("   |                        █      ")
    print("   |                        █      ")
    print("   |                       █ █     ")
    print("   |                      █   █")
    print("   |                     █     █")
    print("   |                   ▀▀▀     ▀▀▀")
    print("███████")
    print("███████")

def dibujo_fallo_intento_cuatro():
    '''
    Imprime el muñeco del ahorcado con el cuello hacia abajo en rojo y lo demas en blanco

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

def dibujo_fallo_intento_cinco():
    '''
    Imprime el muñeco del ahorcado con la cara hacia abajo en rojo y lo demas en blanco

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

def dibujo_fallo_intento_seis():
    '''
    Imprime el muñeco del ahorcado  en rojo e imprime en letras gigantes "PERDISTE"

    Parametros:
    ------------
        Esta funcion no tiene parametros.

    Retorna:
    ------------
        Esta funcion no retorna ningun tipo de dato.
    '''
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

def mensaje_ganador():
    '''
    Imprime en letres gigantes "GANASTE en color verde"

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

if __name__ == '__main__':
    #esta servira para ingresar el nombre del jugador
    nombre_jugador = ""

    #las 3 siguientes listas son donde guardaremos las palabras que usaremos para el juego
    categoria_frutas = ["manzana","naranja","platano","cerezas"]
    categoria_instrumentos = ["guitarra","trompeta","saxofon","acordeon"]
    categoria_colores = ["morado","amarillo","azul","marron"]

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
        #aqui es donde el programa elegira una de las 4 palabras que se encuentren dentro de la categoria frutas
        numero = random.randint(0, 3)
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

        #En este for segun el numero de letras que hay que adivinar se imprimira el caracter '-' para que el jugador sepa cuantas letras debe adivinar
        for i in range(len(letras)):
            print("- ",end="")
        #imprimimos un salto de linea
        print("")
        #declaramos la variable letras_correctas como lista en donde cada vez que se acierte una letra sera agregada a esta lista
        letras_correctas=[]
        #Para este for segun el tamaño de la lista(letras) donde es el numero de letras que tiene la palabra
        for i in range(len(letras)):
            #segun el numero de letras en la lista "letras" agregaremos el caracter '-' el cual luego sera reemplazado cada vez que 
            #el jugador acierte una letra
            letras_correctas.append("-")
            
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
                    #si el numero de intentos es 1 se imprimira el dibujo del muñeco del ahorcado con la parte inferior en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    if(numero_intentos==1):
                        dibujo_fallo_intento_uno()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 2 se imprimira el dibujo del muñeco del ahorcado con la parte de la cintura hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==2):
                        dibujo_fallo_intento_dos()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 3 se imprimira el dibujo del muñeco del ahorcado con la parte del torso hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==3):
                        dibujo_fallo_intento_tres()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 4 se imprimira el dibujo del muñeco del ahorcado con la parte del cuello hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==4):
                        dibujo_fallo_intento_cuatro()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 5 se imprimira el dibujo del muñeco del ahorcado con la parte de la cabeza hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==5):
                        dibujo_fallo_intento_cinco()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 6 se imprimira el dibujo del muñeco del ahorcado en rojo y un mensaje que dice "perdiste"
                    #y se terminara la ejecucion del programa con el comando sys.exit()
                    elif(numero_intentos==6):
                        dibujo_fallo_intento_seis()
                        sys.exit()
    #si el jugador elige jugar con instrumentos musicales entonces
    if opcionMenu==2: 
        #empezaremos con 0 en el numero de intentos para luego sumarle 1 hasta llegar al 6
        numero_intentos=0
        #aqui es donde el programa elegira una de las 4 palabras que se encuentren dentro de la categoria de instrumentos musicales
        numero = random.randint(0, 3)
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

        #En este for segun el numero de letras que hay que adivinar se imprimira el caracter '-' para que el jugador sepa cuantas letras debe adivinar
        for i in range(len(letras)):
            print("- ",end="")
        #imprimimos un salto de linea
        print("")
        #declaramos la variable letras_correctas como lista en donde cada vez que se acierte una letra sera agregada a esta lista
        letras_correctas=[]
        #Para este for segun el tamaño de la lista(letras) donde es el numero de letras que tiene la palabra
        for i in range(len(letras)):
            #segun el numero de letras en la lista "letras" agregaremos el caracter '-' el cual luego sera reemplazado cada vez que 
            #el jugador acierte una letra
            letras_correctas.append("-")
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
                    #si el numero de intentos es 1 se imprimira el dibujo del muñeco del ahorcado con la parte inferior en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    if(numero_intentos==1):
                        dibujo_fallo_intento_uno()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 2 se imprimira el dibujo del muñeco del ahorcado con la parte de la cintura hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==2):
                        dibujo_fallo_intento_dos()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 3 se imprimira el dibujo del muñeco del ahorcado con la parte del torso hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==3):
                        dibujo_fallo_intento_tres()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 4 se imprimira el dibujo del muñeco del ahorcado con la parte del cuello hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==4):
                        dibujo_fallo_intento_cuatro()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 5 se imprimira el dibujo del muñeco del ahorcado con la parte de la cabeza hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==5):
                        dibujo_fallo_intento_cinco()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 6 se imprimira el dibujo del muñeco del ahorcado en rojo y un mensaje que dice "perdiste"
                    #y se terminara la ejecucion del programa con el comando sys.exit()
                    elif(numero_intentos==6):
                        dibujo_fallo_intento_seis()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                        sys.exit()
    #si el jugador elige jugar con colores entonces
    if opcionMenu==3:
        #empezaremos con 0 en el numero de intentos para luego sumarle 1 hasta llegar al 6
        numero_intentos=0
        #aqui es donde el programa elegira una de las 4 palabras que se encuentren dentro de la categoria colores
        numero = random.randint(0, 3)
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

        #En este for segun el numero de letras que hay que adivinar se imprimira el caracter '-' para que el jugador sepa cuantas letras debe adivinar
        for i in range(len(letras)):
            print("- ",end="")
        #imprimimos un salto de linea
        print("")
        
        #declaramos la variable letras_correctas como lista en donde cada vez que se acierte una letra sera agregada a esta lista
        letras_correctas=[]
        #Para este for segun el tamaño de la lista(letras) donde es el numero de letras que tiene la palabra
        for i in range(len(letras)):
            #segun el numero de letras en la lista "letras" agregaremos el caracter '-' el cual luego sera reemplazado cada vez que 
            #el jugador acierte una letra
            letras_correctas.append("-")
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
                    #si el numero de intentos es 1 se imprimira el dibujo del muñeco del ahorcado con la parte inferior en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    if(numero_intentos==1):
                        dibujo_fallo_intento_uno()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 2 se imprimira el dibujo del muñeco del ahorcado con la parte de la cintura hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==2):
                        dibujo_fallo_intento_dos()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 3 se imprimira el dibujo del muñeco del ahorcado con la parte del torso hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==3):
                        dibujo_fallo_intento_tres()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 4 se imprimira el dibujo del muñeco del ahorcado con la parte del cuello hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==4):
                        dibujo_fallo_intento_cuatro()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 5 se imprimira el dibujo del muñeco del ahorcado con la parte de la cabeza hacia abajo en rojo y 
                    #volveremos a pedir que el usuario ingrese una letra
                    elif(numero_intentos==5):
                        dibujo_fallo_intento_cinco()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    #si el numero de intentos es 6 se imprimira el dibujo del muñeco del ahorcado en rojo y un mensaje que dice "perdiste"
                    #y se terminara la ejecucion del programa con el comando sys.exit()
                    elif(numero_intentos==6):
                        dibujo_fallo_intento_seis()
                        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                        sys.exit()
        print("")  
        #imprimimos la lista letras para ver como termino el juego
        print(letras)
