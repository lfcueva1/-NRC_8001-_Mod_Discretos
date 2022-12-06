"""
Extension donde llamaremos a los demas programas segun la opcion que haya elegido el jugador

Autores:
Luis Fernando Cueva Flores
Lisbeth Adali Carvajal Escobar
Erick Patricio Ramirez Ortiz

Verisión:
VER.1.3
"""
import os
import BINGO
import subprocess 
def validar_numeros_enteros():
    '''
    Funcion donde se valida si es que el numero ingresado por el jugador es entero, si lo que se ingresó no es un numero
    entero entonces el jugador tendra que volver a ingresar un numero

    Parametros:
    ------------
        Esta funcion no tiene parametros

    Retorna:
    ------------
        Una vez que el numero ingresado haya sido validado, será la variable movimiento raton la que se retornará como entero
    '''
    #mientras sea verdadero se ingresara un dato en la variable raton, si lo que se ingreso es un numero entero
    #rompera el ciclo repetitivo while sino el jugador debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            numero=int(input("Elija una opcion: "))
            break#rempemos ciclo repetitivo
        except ValueError:
            print("No ha ingresado un numero entero.")
    #retornamos la variable movimiento_raton como int
    return numero

def presentacion_de_juego():
    
    print("\033[1;36m"+"██████████████████████████████████████")#imprime las letras en color cian
    print("█Bienvendio a los juegos populares!!!█")
    print("█Selecciones un juego                █")
    print("█1. Bingo                            █")
    print("█2. Ahorcado                         █")
    print("█3. Raton en el laberinto            █")
    print("█4. Salir                            █")
    print("██████████████████████████████████████")


if __name__ == '__main__': 
    while True:
        os.system("cls")
        opcion=0
        presentacion_de_juego()
        print("\033[1;32m"+"")#color verde
        opcion=validar_numeros_enteros()
        while(opcion<1 or opcion>4):
            opcion=validar_numeros_enteros()
        if(opcion==1):
            os.system("cls")
            subprocess.call(["python", "./BINGO.py"])
            os.system("pause")
        if(opcion==2):
            os.system("cls")
            subprocess.call(["python", "./AHORCADO.py"])
            os.system("pause")
        if(opcion==3):
            os.system("cls")
            subprocess.call(["python", "./RATON_LABERINTO.py"])
            os.system("pause")
        if(opcion==4):
            break
