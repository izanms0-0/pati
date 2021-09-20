import os
import time
from colorama import *
import sys

os.system('cls')
done = 'true'
input1  = input(Fore.LIGHTRED_EX + "estas seguro de salir? de ser asi introduce la 'y' de lo contrario pulsa la 'n'>>")
#---------------------------------------------------------------------------
def animate():
        done == 'true'
        sys.stdout.write('\rloading .')
        time.sleep(0.1)
        sys.stdout.write('\rloading ..')
        time.sleep(0.1)
        sys.stdout.write('\rloading ...')
        time.sleep(0.1)
        sys.stdout.write('\rloading ')
        time.sleep(0.1)
        sys.stdout.write('\rDone!     ')

animate()
#---------------------------------------------------------------------------
init()
import os
if input1=="y":
    print(animate)
    os.system('exit')





elif input1=="n":{
    os.system('inicio.exe')
}

else:
    print("introduce una letra valida porfavor \n apreta enter para continuar")
    time.sleep(2)
    os.system('python exit.py')