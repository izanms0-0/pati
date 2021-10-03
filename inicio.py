import os
import time
from colorama import *
#########################################################
os.system('cls')
finales = Fore.GREEN + "0/5" + Style.RESET_ALL
os.system('cls')
print("Bienvenid@ ;)")
time.sleep(2)
os.system('cls')
print("en esta pantalla apareceran los finales que tienes hechos con comparacion a los que hay\nEX: 1/5")
time.sleep(4)
os.system('cls')
print("espero que disfrutes del juego ♥")
time.sleep(3)
os.system('cls')
########################################################################
def menu():
    while True:
        input1 = input("Pulsa 1 para empezar el juego\npulsa 2 para ver los finales que te quedan\npulsa 3 para poner musica especial para el juego\n>>")
        if input1 ==("1"):
            time.sleep(1)
            os.system('python inicio1.py')
        
        elif input1 ==("2"):
            print(finales)
            time.sleep(3)
            os.system('cls')
            
        elif input1 ==("3"):
            os.system('musica.bat')
            os.system('cls')

        else:
            input("esa opcion no esta disponible...\pulsa enter para continuar")
            os.system('cls')    
#################################################
menu()
