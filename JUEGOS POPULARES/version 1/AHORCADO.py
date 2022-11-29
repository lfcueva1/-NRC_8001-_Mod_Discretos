import os
import time
import random
import sys
def dibujo_presentacion_del_juego():
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
    print(chr(27)+"[1;31m") #rojo
    print("   |                     █     █")
    print("   |                   ▀▀▀     ▀▀▀")
    print("███████")
    print("███████")
def dibujo_fallo_intento_dos():
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
    print(chr(27)+"[1;31m") #rojo
    print("   |                       █ █     ")
    print("   |                      █   █")
    print("   |                     █     █")
    print("   |                   ▀▀▀     ▀▀▀")
    print("███████")
    print("███████")

def dibujo_fallo_intento_tres():
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
    print(chr(27)+"[1;31m") #rojo
    print("   |                        █      ")
    print("   |                        █      ")
    print("   |                       █ █     ")
    print("   |                      █   █")
    print("   |                     █     █")
    print("   |                   ▀▀▀     ▀▀▀")
    print("███████")
    print("███████")

def dibujo_fallo_intento_cuatro():
    print(chr(27)+"[1;37m") #blanco
    print("   ┌-------------------------")
    print("   |                        |")
    print("   |                        |")
    print("   |                      █████")
    print("   |                     ███████")
    print("   |                      █████")
    print("   |                        █")
    print(chr(27)+"[1;31m") #rojo
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
    print(chr(27)+"[1;37m") #blanco
    print("   ┌-------------------------")
    print("   |                        |")
    print("   |                        |")
    print("   |                      █████")
    print("   |                     ███████")
    print(chr(27)+"[1;31m") #rojo
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
    print(chr(27)+"[;36m") 
    nombreJugador=input("Ingrese nombre del jugador:")
    os.system("cls")
    return nombreJugador

def validacion_de_la_opcion_menu():
    while True:
        try:
            categoria=int(input("Elija una opcion: "))
            break
        except ValueError:
            print("No ha ingresado un numero entero.")
    return categoria

def validar_letra_ingresada_por_el_usuario(letra):

    while len(letra) != 1:
        letra = input('Ingrese una letra por favor: ')

    return letra


nombre_jugador = ""
numero_intentos = 0
categoria_frutas = ["manzana","naranja","platano","cerezas"]
categoria_instrumentos = ["guitarra","trompeta","saxofon","acordeon"]
categoria_colores = ["morado","amarillo","azul","marron"]
os.system("cls")
print(chr(27)+"[1;33m"+"BIENVENIDO(S) AL JUEGO DEL AHORCADO!") 
dibujo_presentacion_del_juego()
print(chr(27)+"[1;31m"+"(MAXIMO 1 JUGADOR))") 
print(chr(27)+"[;36m") 
nombre_jugador = ingreso_nombre_de_jugadores(nombre_jugador)
print("\x1b[1;33m"+"EMPEZANDO EL JUEGO...") 
time.sleep(1)
print(chr(27)+"[1;32m"+"",nombre_jugador,",Con que categoria de palabras desea jugar?") #verde
print("\033[;36m")#cian
print("1. Frutas")
print("2. Instrumentos musicales")
print("3. colores")
opcionMenu=validacion_de_la_opcion_menu()
while(opcionMenu<1 or opcionMenu>3):
    opcionMenu=validacion_de_la_opcion_menu()


print(chr(27)+"[1;33m") #amarillo
print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
if opcionMenu==1:
    numero_intentos=0
    numero = random.randint(0, 3)
    palabra=categoria_frutas[numero]
    letras=[]
    for letra in palabra:
        letras.append(letra)
    
    print("ADIVINA LA PALABRA:")
    dibujo_presentacion_del_juego()
    print(chr(27)+"[1;33m") #amarillo
    for i in range(len(letras)):
        print("- ",end="")

    print("")
    letras_correctas=[]
    for i in range(len(letras)):
        letras_correctas.append("-")
    while numero_intentos<=6:
        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
        print("")
        for i in range(len(letras)):
            if(letraJugador==letras[i]):
                letras_correctas[i]=letraJugador
                print(letras_correctas)
                

            if(letras_correctas==letras):
                mensaje_ganador()
                sys.exit()
                
            if(letraJugador not in letras):
                numero_intentos=numero_intentos+1
                if(numero_intentos==1):
                    dibujo_fallo_intento_uno()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==2):
                    dibujo_fallo_intento_dos()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==3):
                    dibujo_fallo_intento_tres()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==4):
                    dibujo_fallo_intento_cuatro()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==5):
                    dibujo_fallo_intento_cinco()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==6):
                    dibujo_fallo_intento_seis()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    sys.exit()
if opcionMenu==2:
    numero_intentos=0
    numero = random.randint(0, 3)
    palabra=categoria_instrumentos[numero]
    letras=[]
    for letra in palabra:
        letras.append(letra)
    
    print("ADIVINA LA PALABRA:")
    dibujo_presentacion_del_juego()
    print(chr(27)+"[1;33m") #amarillo
    for i in range(len(letras)):
        print("- ",end="")

    print("")
    letras_correctas=[]
    for i in range(len(letras)):
        letras_correctas.append("-")
    while numero_intentos<=6:
        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
        print("")
        for i in range(len(letras)):
            if(letraJugador==letras[i]):
                letras_correctas[i]=letraJugador
                print(letras_correctas)
                

            if(letras_correctas==letras):
                mensaje_ganador()
                sys.exit()
                
            if(letraJugador not in letras):
                numero_intentos=numero_intentos+1
                if(numero_intentos==1):
                    dibujo_fallo_intento_uno()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==2):
                    dibujo_fallo_intento_dos()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==3):
                    dibujo_fallo_intento_tres()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==4):
                    dibujo_fallo_intento_cuatro()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==5):
                    dibujo_fallo_intento_cinco()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==6):
                    dibujo_fallo_intento_seis()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    sys.exit()
if opcionMenu==3:
    numero_intentos=0
    numero = random.randint(0, 3)
    palabra=categoria_colores[numero]
    letras=[]
    for letra in palabra:
        letras.append(letra)
    
    print("ADIVINA LA PALABRA:")
    dibujo_presentacion_del_juego()
    print(chr(27)+"[1;33m") #amarillo
    for i in range(len(letras)):
        print("- ",end="")

    print("")
    letras_correctas=[]
    for i in range(len(letras)):
        letras_correctas.append("-")
    while numero_intentos<=6:
        letraJugador=validar_letra_ingresada_por_el_usuario('aa')
        print("")
        for i in range(len(letras)):
            if(letraJugador==letras[i]):
                letras_correctas[i]=letraJugador
                print(letras_correctas)
                

            if(letras_correctas==letras):
                mensaje_ganador()
                sys.exit()
                
            if(letraJugador not in letras):
                numero_intentos=numero_intentos+1
                if(numero_intentos==1):
                    dibujo_fallo_intento_uno()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==2):
                    dibujo_fallo_intento_dos()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==3):
                    dibujo_fallo_intento_tres()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==4):
                    dibujo_fallo_intento_cuatro()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==5):
                    dibujo_fallo_intento_cinco()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                elif(numero_intentos==6):
                    dibujo_fallo_intento_seis()
                    letraJugador=validar_letra_ingresada_por_el_usuario('aa')
                    sys.exit()
    print("")           
    print(letras)
    
