import os
import time
from colorama import Fore, Style

#variables
verde = Fore.GREEN
rojo = Fore.RED
morado = Fore.LIGHTMAGENTA_EX
resetear = Style.RESET_ALL
#Borrar la pantalla para empezar
os.system("cls")

#Inicio De la historia
print(Style.NORMAL + "Tokio: 3:59a.m lunes, 13 de marzo ")
time.sleep(4)
os.system('cls')
print(Style.BRIGHT + "3:59a.m")
time.sleep(1)
################################################################################################################################
os.system('cls')
time.sleep(1)
print(Style.BRIGHT + "3:59a.m ")
time.sleep(1)
################################################################################################################################
os.system('cls')
time.sleep(1)
print(Style.BRIGHT + "4:00a.m ")
time.sleep(1)
################################################################################################################################
os.system('cls')
time.sleep(1)
print(Style.NORMAL + "X: escuchas la alarma de tu telefono y te despiertas para prepararte para ir al instituto")
time.sleep(5)
os.system('cls')
################################################################################################################################
print(Style.BRIGHT + "5:00a.m ")
time.sleep(2)
os.system('cls')
################################################################################################################################
input("(Esta es tu primera elección segun lo que eligas pasara una cosa en tu historia o otra.\nPara elegir una opcion mira el numero o letra que tiene a su izquierda y escribelo, despues, apreta enter)\napreta enter para continuar")
time.sleep(2)
os.system("cls")
################################################################################################################################
while True:
    input1 = input("ir al instituto?\n\ny)ir al instituto\nn)no ir al instituto\n>>")

    if input1 == ("y"):
        os.system('cls')
        os.system('python historia2/si.py')
    

    elif input1 == ("n"):{
    os.system('python historia2/no.py')
    }

    else:
     os.system("cls")
     input(Fore.LIGHTMAGENTA_EX + "esta opcion no esta disponible...\napreta enter para continuar" + Style.RESET_ALL)
     os.system("cls")