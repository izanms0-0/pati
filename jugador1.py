import os
import time 
os.system('cls')
#vaiables

print('Roger es un chico de italia concretamente de positano\n \n puntos positivos: \n amable \n buen carisma  \n optimista \n \n puntos debiles: \n sarcasmo. \n manipulable. \n sensible a situaciones muy arriesgadas.')

time.sleep(1)

input1 = input ('estas seguro de que quieres salir? de ser asi apreta "y" de lo contrario apreta "n" >>')

if input1=='y':{
    os.system('inicio.exe')
}

elif input1=='n':{
    os.system('python jugador1.py')
}

else:
    
    input("No has pulsado ninguna opción correcta...\npulsa enter para continuar")
    time.sleep(1)
    
os.system('python jugador1.py')