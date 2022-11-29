import random
import os
os.system("cls")
def ingreso_numero_de_jugadores():
    while True:
        try:
            numJugadores=int(input("Ingrese un numero entero: "))
            break
        except ValueError:
            print("No ha ingresado un numero entero.")
    return numJugadores

def ingreso_nombre_de_jugadores(nombresJugadores,nJugadores):
    
    for i in range(nJugadores):
        print(chr(27)+"[1;37m"+"JUGADOR ",i+1) 
        print(chr(27)+"[;36m") 
        nombres=input("Ingrese nombre del jugador:")
        nombresJugadores.append(nombres)
        
    os.system("cls")

def generacion_de_cartones(carton1,carton2,carton3,carton4,nJugadores):
    if(nJugadores==1):
        while len(carton1) < 26:
            numero = random.randint(1, 99)
            if numero not in carton1:
                carton1.append(numero)
        carton1[13]=0
        
    if(nJugadores==2):
        while len(carton1) < 26:
            numero = random.randint(1, 99)
            if numero not in carton1:
                carton1.append(numero)
        while len(carton2) < 26:
            numero = random.randint(1, 99)
            if numero not in carton2:
                carton2.append(numero)
        carton1[13]=0
        carton2[13]=0
        
    if(nJugadores==3):
        while len(carton1) < 26:
            numero = random.randint(1, 99)
            if numero not in carton1:
                carton1.append(numero)
        while len(carton2) < 26:
            numero = random.randint(1, 99)
            if numero not in carton2:
                carton2.append(numero)
        while len(carton3) < 26:
            numero = random.randint(1, 99)
            if numero not in carton3:
                carton3.append(numero)
        carton1[13]=0
        carton2[13]=0
        carton3[13]=0
        
    
    if(nJugadores==4):
        while len(carton1) < 26:
            numero = random.randint(1, 99)
            if numero not in carton1:
                carton1.append(numero)
        while len(carton2) < 26:
            numero = random.randint(1, 99)
            if numero not in carton2:
                carton2.append(numero)
        while len(carton3) < 26:
            numero = random.randint(1, 99)
            if numero not in carton3:
                carton3.append(numero)
        while len(carton4) < 26:
            numero = random.randint(1, 99)
            if numero not in carton4:
                carton4.append(numero)
        carton1[13]=0
        carton2[13]=0
        carton3[13]=0
        carton4[13]=0

def imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores):
    if (nJugadores==1):
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton1)):
            print(carton1[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

    if (nJugadores==2):
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton1)):
            print(carton1[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton2)):
            print(carton2[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

    if (nJugadores==3):
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")
        print(chr(27)+"[1;36m")
        for i in range(1,len(carton1)):
            print(carton1[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton2)):
            print(carton2[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[2],":")
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton3)):
            print(carton3[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

    if (nJugadores==4):
        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[0],":")
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton1)):
            print(carton1[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[1],":")
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton2)):
            print(carton2[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[2],":")
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton3)):
            print(carton3[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

        print(chr(27)+"[1;37m"+"CARTON DE ",nombresJugadores[3],":")
        print(chr(27)+"[1;36m") 
        for i in range(1,len(carton4)):
            print(carton4[i]," ",end="")
            if(i%5==0):
                print("")
        print("")

def bombo_generando_numeros(bombo):
    while len(bombo) < 100:
            numero = random.randint(1, 99)
            if numero not in bombo:
                bombo.append(numero)
                return numero

def imprimir_BINGO():
    print(chr(27)+"[1;33m") 
    print("||||||||      ||||||||||   ||       ||    ||||||||||   ||||||||||")
    print("||     ||         ||       ||||     ||    ||           ||      ||")
    print("||      ||        ||       || ||    ||    ||           ||      ||")
    print("||||||||          ||       ||  ||   ||    ||    ||||   ||      ||")
    print("||      ||        ||       ||   ||  ||    ||      ||   ||      ||")
    print("||     ||         ||       ||    || ||    ||      ||   ||      ||")
    print("||||||||      ||||||||||   ||     ||||    ||||||||||   ||||||||||")


carton1=[]
carton2=[]
carton3=[]
carton4=[]
bombo=[]
nombresJugadores=[]
print(chr(27)+"[1;33m"+"BIENVENIDO(S) AL JUEGO DEL BINGO!") 
print(chr(27)+"[1;31m"+"(MAXIMO 4 JUGADORES))") 
print(chr(27)+"[;36m") 

nJugadores=ingreso_numero_de_jugadores()
while nJugadores<1 or nJugadores>4:
    nJugadores=ingreso_numero_de_jugadores()

ingreso_nombre_de_jugadores(nombresJugadores,nJugadores)
generacion_de_cartones(carton1,carton2,carton3,carton4,nJugadores)
os.system("cls")
imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)

os.system("Pause")
print(chr(27)+"[1;32m"+"EMPEZANDO EL JUEGO...") 
os.system("Pause")
numeroDeBolas=0
while (numeroDeBolas<=99):
    x=bombo_generando_numeros(bombo)
    print(chr(27)+"[1;31m"+"EMPEZANDO EL JUEGO...") 
    print(chr(27)+"[1;31m"+"EL BOMBO HA ARROJADO EL NUMERO: ",x) 
    if(nJugadores==1):
        if(x in carton1):
            carton1[carton1.index(x)]=0
        imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton1[1]==0 and carton1[6]==0 and carton1[11]==0 and carton1[16]==0 and carton1[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[2]==0 and carton1[7]==0 and carton1[12]==0 and carton1[17]==0 and carton1[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[3]==0 and carton1[8]==0 and carton1[18]==0 and carton1[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[4]==0 and carton1[9]==0 and carton1[14]==0 and carton1[19]==0 and carton1[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[5]==0 and carton1[10]==0 and carton1[15]==0 and carton1[20]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[1]==0 and carton1[2]==0 and carton1[3]==0 and carton1[4]==0 and carton1[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[6]==0 and carton1[7]==0 and carton1[8]==0 and carton1[9]==0 and carton1[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[11]==0 and carton1[12]==0  and carton1[14]==0 and carton1[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[16]==0 and carton1[17]==0 and carton1[18]==0 and carton1[19]==0 and carton1[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[21]==0 and carton1[22]==0 and carton1[23]==0 and carton1[24]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[1]==0 and carton1[7]==0  and carton1[19]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[5]==0 and carton1[9]==0  and carton1[17]==0 and carton1[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break


    if(nJugadores==2):
        if(x in carton1):
            carton1[carton1.index(x)]=0
        #imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton1[1]==0 and carton1[6]==0 and carton1[11]==0 and carton1[16]==0 and carton1[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[2]==0 and carton1[7]==0 and carton1[12]==0 and carton1[17]==0 and carton1[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[3]==0 and carton1[8]==0 and carton1[18]==0 and carton1[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[4]==0 and carton1[9]==0 and carton1[14]==0 and carton1[19]==0 and carton1[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[5]==0 and carton1[10]==0 and carton1[15]==0 and carton1[20]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[1]==0 and carton1[2]==0 and carton1[3]==0 and carton1[4]==0 and carton1[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[6]==0 and carton1[7]==0 and carton1[8]==0 and carton1[9]==0 and carton1[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[11]==0 and carton1[12]==0  and carton1[14]==0 and carton1[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[16]==0 and carton1[17]==0 and carton1[18]==0 and carton1[19]==0 and carton1[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[21]==0 and carton1[22]==0 and carton1[23]==0 and carton1[24]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[1]==0 and carton1[7]==0  and carton1[19]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[5]==0 and carton1[9]==0  and carton1[17]==0 and carton1[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        if(x in carton2):
            carton2[carton2.index(x)]=0
        imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton2[1]==0 and carton2[6]==0 and carton2[11]==0 and carton2[16]==0 and carton2[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[2]==0 and carton2[7]==0 and carton2[12]==0 and carton2[17]==0 and carton2[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[3]==0 and carton2[8]==0 and carton2[18]==0 and carton2[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[4]==0 and carton2[9]==0 and carton2[14]==0 and carton2[19]==0 and carton2[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[5]==0 and carton2[10]==0 and carton2[15]==0 and carton2[20]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[1]==0 and carton2[2]==0 and carton2[3]==0 and carton2[4]==0 and carton2[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[6]==0 and carton2[7]==0 and carton2[8]==0 and carton2[9]==0 and carton2[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[11]==0 and carton2[12]==0  and carton2[14]==0 and carton2[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[16]==0 and carton2[17]==0 and carton2[18]==0 and carton2[19]==0 and carton2[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[21]==0 and carton2[22]==0 and carton2[23]==0 and carton2[24]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[1]==0 and carton2[7]==0  and carton2[19]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[5]==0 and carton2[9]==0  and carton2[17]==0 and carton2[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
    if(nJugadores==3):
        if(x in carton1):
            carton1[carton1.index(x)]=0
        #imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton1[1]==0 and carton1[6]==0 and carton1[11]==0 and carton1[16]==0 and carton1[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[2]==0 and carton1[7]==0 and carton1[12]==0 and carton1[17]==0 and carton1[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[3]==0 and carton1[8]==0 and carton1[18]==0 and carton1[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[4]==0 and carton1[9]==0 and carton1[14]==0 and carton1[19]==0 and carton1[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[5]==0 and carton1[10]==0 and carton1[15]==0 and carton1[20]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[1]==0 and carton1[2]==0 and carton1[3]==0 and carton1[4]==0 and carton1[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[6]==0 and carton1[7]==0 and carton1[8]==0 and carton1[9]==0 and carton1[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[11]==0 and carton1[12]==0  and carton1[14]==0 and carton1[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[16]==0 and carton1[17]==0 and carton1[18]==0 and carton1[19]==0 and carton1[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[21]==0 and carton1[22]==0 and carton1[23]==0 and carton1[24]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[1]==0 and carton1[7]==0  and carton1[19]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[5]==0 and carton1[9]==0  and carton1[17]==0 and carton1[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        if(x in carton2):
            carton2[carton2.index(x)]=0
        #imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton2[1]==0 and carton2[6]==0 and carton2[11]==0 and carton2[16]==0 and carton2[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[2]==0 and carton2[7]==0 and carton2[12]==0 and carton2[17]==0 and carton2[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[3]==0 and carton2[8]==0 and carton2[18]==0 and carton2[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[4]==0 and carton2[9]==0 and carton2[14]==0 and carton2[19]==0 and carton2[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[5]==0 and carton2[10]==0 and carton2[15]==0 and carton2[20]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[1]==0 and carton2[2]==0 and carton2[3]==0 and carton2[4]==0 and carton2[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[6]==0 and carton2[7]==0 and carton2[8]==0 and carton2[9]==0 and carton2[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[11]==0 and carton2[12]==0  and carton2[14]==0 and carton2[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[16]==0 and carton2[17]==0 and carton2[18]==0 and carton2[19]==0 and carton2[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[21]==0 and carton2[22]==0 and carton2[23]==0 and carton2[24]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[1]==0 and carton2[7]==0  and carton2[19]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[5]==0 and carton2[9]==0  and carton2[17]==0 and carton2[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        if(x in carton3):
            carton3[carton3.index(x)]=0
        imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton3[1]==0 and carton3[6]==0 and carton3[11]==0 and carton3[16]==0 and carton3[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[2]==0 and carton3[7]==0 and carton3[12]==0 and carton3[17]==0 and carton3[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[3]==0 and carton3[8]==0 and carton3[18]==0 and carton3[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[4]==0 and carton3[9]==0 and carton3[14]==0 and carton3[19]==0 and carton3[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[5]==0 and carton3[10]==0 and carton3[15]==0 and carton3[20]==0 and carton3[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[1]==0 and carton3[2]==0 and carton3[3]==0 and carton3[4]==0 and carton3[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[6]==0 and carton3[7]==0 and carton3[8]==0 and carton3[9]==0 and carton3[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[11]==0 and carton3[12]==0  and carton3[14]==0 and carton3[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[16]==0 and carton3[17]==0 and carton3[18]==0 and carton3[19]==0 and carton3[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[21]==0 and carton3[22]==0 and carton3[23]==0 and carton3[24]==0 and carton3[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[1]==0 and carton3[7]==0  and carton3[19]==0 and carton3[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[5]==0 and carton3[9]==0  and carton3[17]==0 and carton3[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        
    if(nJugadores==4):
        if(x in carton1):
            carton1[carton1.index(x)]=0
        #imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton1[1]==0 and carton1[6]==0 and carton1[11]==0 and carton1[16]==0 and carton1[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[2]==0 and carton1[7]==0 and carton1[12]==0 and carton1[17]==0 and carton1[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[3]==0 and carton1[8]==0 and carton1[18]==0 and carton1[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[4]==0 and carton1[9]==0 and carton1[14]==0 and carton1[19]==0 and carton1[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[5]==0 and carton1[10]==0 and carton1[15]==0 and carton1[20]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[1]==0 and carton1[2]==0 and carton1[3]==0 and carton1[4]==0 and carton1[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[6]==0 and carton1[7]==0 and carton1[8]==0 and carton1[9]==0 and carton1[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[11]==0 and carton1[12]==0  and carton1[14]==0 and carton1[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[16]==0 and carton1[17]==0 and carton1[18]==0 and carton1[19]==0 and carton1[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[21]==0 and carton1[22]==0 and carton1[23]==0 and carton1[24]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[1]==0 and carton1[7]==0  and carton1[19]==0 and carton1[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        elif(carton1[5]==0 and carton1[9]==0  and carton1[17]==0 and carton1[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[0]) 
            break
        if(x in carton2):
            carton2[carton2.index(x)]=0
        #imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton2[1]==0 and carton2[6]==0 and carton2[11]==0 and carton2[16]==0 and carton2[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[2]==0 and carton2[7]==0 and carton2[12]==0 and carton2[17]==0 and carton2[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[3]==0 and carton2[8]==0 and carton2[18]==0 and carton2[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[4]==0 and carton2[9]==0 and carton2[14]==0 and carton2[19]==0 and carton2[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[5]==0 and carton2[10]==0 and carton2[15]==0 and carton2[20]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[1]==0 and carton2[2]==0 and carton2[3]==0 and carton2[4]==0 and carton2[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[6]==0 and carton2[7]==0 and carton2[8]==0 and carton2[9]==0 and carton2[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[11]==0 and carton2[12]==0  and carton2[14]==0 and carton2[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[16]==0 and carton2[17]==0 and carton2[18]==0 and carton2[19]==0 and carton2[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[21]==0 and carton2[22]==0 and carton2[23]==0 and carton2[24]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[1]==0 and carton2[7]==0  and carton2[19]==0 and carton2[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        elif(carton2[5]==0 and carton2[9]==0  and carton2[17]==0 and carton2[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[1]) 
            break
        if(x in carton3):
            carton3[carton3.index(x)]=0
        #imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton3[1]==0 and carton3[6]==0 and carton3[11]==0 and carton3[16]==0 and carton3[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[2]==0 and carton3[7]==0 and carton3[12]==0 and carton3[17]==0 and carton3[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[3]==0 and carton3[8]==0 and carton3[18]==0 and carton3[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[4]==0 and carton3[9]==0 and carton3[14]==0 and carton3[19]==0 and carton3[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[5]==0 and carton3[10]==0 and carton3[15]==0 and carton3[20]==0 and carton3[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[1]==0 and carton3[2]==0 and carton3[3]==0 and carton3[4]==0 and carton3[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[6]==0 and carton3[7]==0 and carton3[8]==0 and carton3[9]==0 and carton3[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[11]==0 and carton3[12]==0  and carton3[14]==0 and carton3[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[16]==0 and carton3[17]==0 and carton3[18]==0 and carton3[19]==0 and carton3[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[21]==0 and carton3[22]==0 and carton3[23]==0 and carton3[24]==0 and carton3[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[1]==0 and carton3[7]==0  and carton3[19]==0 and carton3[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        elif(carton3[5]==0 and carton3[9]==0  and carton3[17]==0 and carton3[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[2]) 
            break
        if(x in carton4):
            carton4[carton4.index(x)]=0
        imprimir_cartones_de_los_jugadores(carton1,carton2,carton3,carton4,nJugadores)
        print("\x1b[1;33m"+"-------------------------")
        if(carton4[1]==0 and carton4[6]==0 and carton4[11]==0 and carton4[16]==0 and carton4[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[2]==0 and carton4[7]==0 and carton4[12]==0 and carton4[17]==0 and carton4[22]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[3]==0 and carton4[8]==0 and carton4[18]==0 and carton4[23]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[4]==0 and carton4[9]==0 and carton4[14]==0 and carton4[19]==0 and carton4[24]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[5]==0 and carton4[10]==0 and carton4[15]==0 and carton4[20]==0 and carton4[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[1]==0 and carton4[2]==0 and carton4[3]==0 and carton4[4]==0 and carton4[5]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[6]==0 and carton4[7]==0 and carton4[8]==0 and carton4[9]==0 and carton4[10]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[11]==0 and carton4[12]==0  and carton4[14]==0 and carton4[15]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[16]==0 and carton4[17]==0 and carton4[18]==0 and carton4[19]==0 and carton4[20]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[21]==0 and carton4[22]==0 and carton4[23]==0 and carton4[24]==0 and carton4[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[1]==0 and carton4[7]==0  and carton4[19]==0 and carton4[25]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        elif(carton4[5]==0 and carton4[9]==0  and carton4[17]==0 and carton4[21]==0):
            imprimir_BINGO()
            print(chr(27)+"[1;33m"+"EL GANADOR ES: ",nombresJugadores[3]) 
            break
        
        
    os.system("Pause")


print()