import os
import time
import sys
os.system("cls")
def dibujo_presentacion_del_juego():
    print("\033[1;36m")
    print("        █████           █████")
    print("       ██    ██       ██     ██")
    print("      ██      ████████        ██")
    print("       ██    ██       ██     ██")
    print("         ████           █████")
    print(chr(27)+"[1;37m"+"       ███         ███",chr(27)+"[1;36m"+"    ██") 
    print("\033[1;31m",end="")
    print("    ███ ",chr(27)+"[1;36m"+"                ██")
    print("\033[1;36m",end="")
    print("       ███████████       ██")
    print("            ██           ██")
    print("            ██           ██")

def elegir_movimiento_del_raton():
    while True:
        try:
            movimiento_raton=int(input("Elija una opcion: "))
            break
        except ValueError:
            print("No ha ingresado un numero entero.")
    return movimiento_raton

def imprimir_mapa(mapa):
    for i in range (8):
        for j in range(11):
            if(mapa[i][j]==1):
                print(chr(27)+"[1;37m"+"█",end="")#blanco
            elif(mapa[i][j]==2):
                print(chr(27)+"[1;32m"+"█",end="") 
            else:
                print(chr(27)+"[1;35m"+"█",end="")#morado
        print("")

def movimiento_del_raton_arriba(mapa):
    raton = 2
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == raton:
                print(i,j)
                a=i
                b=j
                
    if(mapa[a-1][b]==1):
        mapa[a-1][b]=2
        mapa[a][b]=1

def movimiento_del_raton_abajo(mapa):
    raton = 2
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == raton:
                print(i,j)
                a=i
                b=j
                
    if(mapa[a+1][b]==1):
        mapa[a+1][b]=2
        mapa[a][b]=1

def movimiento_del_raton_izquierda(mapa):
    raton = 2
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == raton:
                print(i,j)
                a=i
                b=j
                
    if(mapa[a][b-1]==1):
        mapa[a][b-1]=2
        mapa[a][b]=1

def movimiento_del_raton_derecha(mapa):
    raton = 2
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == raton:
                print(i,j)
                a=i
                b=j
                
    if(mapa[a][b+1]==1):
        mapa[a][b+1]=2
        mapa[a][b]=1     

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

mapa = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0], 
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

final_laberinto=False
print(chr(27)+"[1;33m"+"BIENVENIDO AL JUEGO DE RATON EN EL LABERINTO") 
dibujo_presentacion_del_juego()
print("")
print(chr(27)+"[1;32m"+"PRESIONE UNA TECLA PARA CONTINUAR") 
os.system("pause")
print(chr(27)+"[1;37m"+"EMPEZANDO EL JUEGO")
time.sleep(1)
os.system("cls")

for i in range (8): #borrar despues
    for j in range(11):
        print(mapa[i][j]," ",end="")
    print("")

print("Ustes es: ",chr(27)+"[1;32m"+"█")
imprimir_mapa(mapa)
while(final_laberinto==False):
    print(chr(27)+"[1;33m"+"Hacia donde quieres mover el raton?")
    print("\033[;36m")#cian
    print("1. Arriba")
    print("2. Abajo")
    print("3. Izquierda")
    print("4. Derecha")

    mov_raton=elegir_movimiento_del_raton()
    while (mov_raton<1 or mov_raton>4):
        mov_raton=elegir_movimiento_del_raton()
        
    if(mov_raton==1):
        os.system("cls")
        movimiento_del_raton_arriba(mapa)
        imprimir_mapa(mapa)
        if(mapa[6][10]==2):
            mensaje_ganador()
            sys.exit()
    if(mov_raton==2):
        os.system("cls")
        movimiento_del_raton_abajo(mapa)
        imprimir_mapa(mapa)
        if(mapa[6][10]==2):
            mensaje_ganador()
            sys.exit()
    if(mov_raton==3):
        os.system("cls")
        movimiento_del_raton_izquierda(mapa)
        imprimir_mapa(mapa)
        if(mapa[6][10]==2):
            mensaje_ganador()
            sys.exit()
    if(mov_raton==4):
        os.system("cls")
        movimiento_del_raton_derecha(mapa)
        imprimir_mapa(mapa)
        if(mapa[6][10]==2):
            mensaje_ganador()
            sys.exit()

