import os 
import time
import colorama

os.system('cls')

#VARIABLES GLOBALES

timepo3 = time.sleep(3)
tiempo2 = time.sleep(2)
tiempo1 = time.sleep(1)
cls = os.system('cls')
rojo = Fore.RED
verde = Fore.GREEN
rosa = Fore.MAGENTA
resetear = Style.RESET_ALL

#Codigo
print("X: Cojes tu mochila y sales de tu casa...")
time.sleep(3)
os.system('cls')
print("7:00")
time.sleep(0.7)
os.system('cls')
print("7:00")
time.sleep(0.7)
os.system('cls')
print("7:00")
time.sleep("7:00")
os.system('cls')
print("X: llegas a las puertas de tu instituto y estan cerradas")
time.sleep(3)
os.system('cls')
#Menu 
def menu():
    print("1-) Esperar")
    print("")
    print("2-) ir a un bar")
    print("\n >>")
    
while True:
    input1 = input("Que quieres hacer?\n\n")
    menu()
    if input1==("1"):{
        os.system('cls')
        os.system('python esperar.py')
    }
    
    elif input1==("2"):{
        os.system('cls')
        time.sleep(1.3)
        break
    }
        
    else:
        input('Esa opcion no esta en la lista...\nPulsa enter para continuar')
break
##############################################################################################################################################

print("X: caminas hasta un bar a la vuelta de la esquina...")
time.sleep(2)
cls
print("7:15")
tiempo2
cls
