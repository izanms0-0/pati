import os
import time

finales = "0/5"
os.system('cls')
print("Bienvenid@ ;)")
time.sleep(2)
os.system('cls')
print("en esta pantalla apareceran los finales que tienes echos con comparacion a los que hay\nEX: 1/5")
time.sleep(4)
os.system('cls')
print("espero que disfrutes del juego ♥")
time.sleep(3)
os.system('cls')
print(finales)
time.sleep(2)
os.system('cls')
while True:
    input1 = input("Pulsa enter para empezar el juego o pulsa 1 para ver los finales que te quedan")
    if input1 ==("1"):{
    print(finales)
    }

    else:{
    input("esa opcion no esta disponible...\pulsa enter para continuar")
    }
    break


os.system('python inicio1.py')