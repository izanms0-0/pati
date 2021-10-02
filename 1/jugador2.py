import os
import time
from colorama import *
import tqdm

os.system('cls')

def menu():
    init()
    print(Fore.WHITE + "Lilit es una niña de Alemania, Berlín " + Fore.GREEN + "\n\nPuntos fuertes: \nAstuta\nÁgil\nManipuladora" + Style.RESET_ALL)
    print(Fore.RED + "\nPuntos Debiles:\nCobarde\nDesconfiada\nImpacienciente\n" + Style.RESET_ALL)

        
while True:
    os.system('cls')
    menu()
    color = Fore.GREEN
    reset = Style.RESET_ALL
    input1 = input(Fore.WHITE + 'quieres elegir a este personaje para el juego y/n? >>' + reset)
    
    if input1=="y":
        time.sleep(2)
        os.system('python historia2/h2.py')
    
    
    elif input1=="Y":{
        os.system('python historia2/h2.py')
    }
        
    elif input1=="n":{
        os.system('python inicio1.py')
    }
    
    elif input1=="N":{
        os.system('python inicio1.py')
    }
    
    else:
        print("")
        os.system('cls')
        input(Fore.LIGHTMAGENTA_EX + 'esa opcion no esta disponible elige algo que este en la lista...\nPulsa enter para volver a elegir' + reset)