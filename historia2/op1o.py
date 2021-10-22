import os 
import time
from colorama import *

os.system('cls')

#cajetilla para def
def menu1():
    print("Que quieres tomar?")
    print("")
    print("1-)" + Fore.RED + " Agua" + Style.RESET_ALL)
    print("2-) Zumo de naranja")
    print("3-) Granizado")
    print("4-) Nada")
    input2 = input(">>")
    
    if input2 == ("1"):
        time.sleep(0.5)
        os.system('python agua.py')
    
    elif input2 == ("2"):
        time.sleep(0.5)
        os.system('python zumo.py')
        
    elif input2 == ("3"):
        time.sleep(0.5)
        os.system("python granizado.py")
        
    elif input2 == ("4"):
        time.sleep(0.5)
        
    
    else:
        input(Fore.LIGHTMAGENTA_EX + "Esa opcion no esta en la lista...\nPulsa Enter para continuar" + Style.RESET_ALL)
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
time.sleep(0.4)
print("X: llegas a las puertas de tu instituto y estan cerradas")
time.sleep(2.5)
os.system('cls')
#Menu 
while True:
    input1 = input("Que quieres hacer?\n" + "\n1-) Esperar" + "\n2-) ir a un bar" + "\n\n>>")
    
    if input1==("1"):
        os.system('cls')
        os.system('python esperar.py')
			
    elif input1==("2"):
        os.system('cls')
        time.sleep(1.3)
        break
        
    else:
        input(Fore.LIGHTMAGENTA_EX + 'Esa opcion no esta en la lista...\nPulsa enter para continuar' + Style.RESET_ALL)  
        os.system('cls')
            
            
##############################################################################################################################################

print("X: caminas hasta un bar a la vuelta de la esquina...")
time.sleep(2)
os.system('cls')
print("X: Entras al bar y te sientas")
time.sleep(3)
os.system('cls')
print("X: Pocos segundos despues viene un mesero y te pregunta...")
time.sleep(3)
os.system('cls')

while True:
    menu1()
    break

os.system("cls")
time.sleep(0.5)
print("X: El mesero se va y al rato viene con un vaso de agua")
time.sleep(3)
os.system("cls")
while True:
        input2 = input("quieres beberte el agua ?\n1-) si\n2-) no\n>>")
        
        if input2 == ("1") or ("si"):
            time.sleep(1)
            os.system("python agua/si.py")
            
        elif input2 == ("2") or ("no"):
            time.sleep(1)
            os.system("python agua/no.py")
            
        else: 
            input(Fore.LIGHTMAGENTA_EX + "Esa opcion no esta disponible...\nPulsa enter para continuar" + Style.RESET_ALL)     