import os
import time 
import colorama
os.system('cd ')
os.system('cls')
#vaiables

print('no hay propiedades en el "jugador2"!')

time.sleep(1)

input1 = input ('estas seguro de que te quieres salir? de ser asi apreta "y" de lo contrario apreta "n" >>')

if input1=='y':{
    os.system('inicio.exe')
}

elif input1=='n':{
    os.system('python jugador2.py')
}

else:
    
    input("No has pulsado ninguna opción correcta...\npulsa enter para continuar")
    time.sleep(1)
    
os.system('python jugador2.py')