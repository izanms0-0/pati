import os
import time
from colorama import *

os.system('cls')
time.sleep(3)
print("X: te levantas de la cama y te preparas para ir al instituto, te duchas, te vistes, desayunas y terminas de colocar las cosas en la mochila")
time.sleep(3)
os.system("cls")
print(Style.BRIGHT + "6:00a.m")
time.sleep(1)
################################################################################################################################
os.system('cls')
time.sleep(1)
print(Style.BRIGHT + "6:00a.m ")
time.sleep(1)
################################################################################################################################
os.system('cls')
time.sleep(1)
print(Style.BRIGHT + "6:00a.m ")
time.sleep(1)
os.system('cls')
print("Terminas de prepararte y te faltan dos horas para que empiezen las clases")
time.sleep(3)
os.system('cls')

while True:
    input1=input('ir al instituto o esperar un rato para salir?\n1-)Salir\n1-)Quedarse >>')
    if input1==("1"):{
    os.system('python historia2/op1o.py')
    }

    elif input1==("2"):{
    os.system('python historia2/op1x.py')
    }