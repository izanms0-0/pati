import os 
import time
import colorama

os.system('cls')

#VARIABLES GLOBALES

rojo = Fore.RED
verde = Fore.GREEN
rosa = Fore.MAGENTA
resetear = Style.RESET_ALL

#Codigo
print("Cojes tu mochila y sales de tu casa...")
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
print("llegas a las puertas de tu instituto y estan cerradas")
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
        break
    }
        
    else:
        input('Esa opcion no esta en la lista...\nPulsa enter para continuar')
break
