#Importaciones 
import os
import time
from colorama import *
#codigo
def menu():
    
	os.system('cls')
	print ("Selecciona una opción")
	print ("\t1 - Roger")
	print ("\t2 - Lily")
	print ("\t3 - Elige tu un nombre")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		os.system('python jugador1.py')
	elif opcionMenu=="2":
		os.system('python jugador2.py')
	elif opcionMenu=="3":
		os.system('python jugador3.py')
	elif opcionMenu=="9":
		os.system('python exit.py')
	else:
		print ()
		input(Fore.MAGENTA + "No has pulsado ninguna opción correcta...\npulsa una tecla para continuar" + Fore.RESET)