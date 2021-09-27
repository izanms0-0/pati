import os
import time
from colorama import *

os.system('cls')

def menu():
    init()
    print(Fore.WHITE + "Roger es un chico de italia, Positano con 14 años. " + Fore.GREEN + "\n\nPuntos fuertes: \nOptimista\nComprensivo\nAmable" + Style.RESET_ALL)
    print(Fore.RED + "\nPuntos Debiles:\nManipulable\nPerezoso\nPoca fuerza física\n" + Style.RESET_ALL)

        
while True:
    os.system('cls')
    menu()
    color = Fore.GREEN
    reset = Style.RESET_ALL
    input1 = input(Fore.WHITE + 'quieres elegir a este personaje para el juego y/n? >>' + reset)
    
    if input1=="y":{
        os.system('python h1.py')
    }
    
    elif input1=="Y":{
        os.system('python h1.py')
    }
        
    elif input1=="n":{
        os.system('python inicio.py')
    }
    
    elif input1=="N":{
        os.system('python inicio.py')
    }
    
    else:
        print("")
        os.system('cls')
        input(Fore.LIGHTMAGENTA_EX + "esa opcion no esta disponible elige algo que este en la lista...\nPulsa enter para volver a elegir" + reset)