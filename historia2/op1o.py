import os 
import time
from colorama import *

os.system('cls')

#VARIABLES GLOBALES

rojo = Fore.RED
verde = Fore.GREEN
rosa = Fore.MAGENTA
resetear = Style.RESET_ALL

#Codigo
print("X: Cojes tu mochila y sales de tu casa...")
time.sleep(3)
os.system('cls')
print(Style.BRIGHT + "7:00a.m")
time.sleep(1)
################################################################################################################################
os.system('cls')
time.sleep(1)
print(Style.BRIGHT + "7:00a.m ")
time.sleep(1)
################################################################################################################################
os.system('cls')
time.sleep(1)
print(Style.BRIGHT + "7:00a.m ")
time.sleep(1)
os.system('cls')
print("X: llegas a las puertas de tu instituto y estan cerradas")
time.sleep(2.5)
os.system('cls')
#Menu 
def menu():
    """
    Funcion de reseteo
    """
    while True:
        input1 = input("Que quieres hacer?\n" + "\n1-) Esperar" + "\n2-) ir a un bar" + "\n\n>>")

        if input1==("1"):
            os.system('cls')
            os.system('python esperar.py')
    
    
        elif input1==("2"):
            os.system('cls')
            time.sleep(1.3)
        
        else:
            input(Fore.LIGHTMAGENTA_EX + 'Esa opcion no esta en la lista...\nPulsa enter para continuar' + Style.RESET_ALL)  
        break    
##############################################################################################################################################

menu()

print("X: caminas hasta un bar a la vuelta de la esquina...")
time.sleep(2)
os.system('cls')
print("7:15")
time.sleep()
os.system('cls')
print("X: Entras al bar y te sientas")
time.sleep(3)
os.system('cls')
print("X: Pocos segundos despues viene un mesero y te pregunta...")
time.sleep(3)
os.system('cls')
def  menu1():
    input("Quieres pedir algo?")
    print("")
    print("")