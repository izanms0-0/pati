import os
import time
from colorama import *

def menu():
    """
    funcion que muestra de nuevo el menu
    """
    os.system('cls')
    print("\n-1) Roger")
    time.sleep(1)
    print("\n-2) Lilit")
    time.sleep(1)
    print("\n-3) elige tu el nombre")
    time.sleep(1)
    print("\n-4) Salir")
    time.sleep(1)
    print("\n")
while True:
    menu()

    input1 = input("elige el nombre del jugador para continuar :3 >>")
    
    if input1=="1":{
    os.system('python jugador1.py')
    }
    elif input1=="2":{
    os.system('python jugador2.py')
    }
    elif input1=="3":{
    os.system('python jugador3.py')
    }
    elif input1=="4":{
    os.system('python exit.py')
    }
    
    else: 
        input (Fore.LIGHTMAGENTA_EX + 'esa no es una opcion valida elige una opcion en la lista...\napreta enter para continuar' + Style.RESET_ALL)