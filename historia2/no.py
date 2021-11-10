import os
import time
from colorama import *

hola 123

os.system('cls')
print("X: apagas la alarma y cierras los ojos. Minutos seguidos te duermes")
time.sleep(3)
os.system('cls')
#########################################################
print("15:30")
time.sleep(1)
os.system('cls')
time.sleep(1)
print("15:30")
time.sleep(1)
os.system('cls')
time.sleep(1)
print("15:30")
time.sleep(1)
os.system('cls')
time.sleep(1)
#########################################################
print("X: Te rujen las tripas y tienes mucha hambre, Te levantas de la cama y vas a la nevera")
time.sleep(5)
os.system('cls')

def menu():
    print("X: Abres la nevera y ves:")
    time.sleep(2)
    print("1-) Ramen")
    time.sleep(1)
    print("2-) Sushi")
    time.sleep(1)
    print("3-) Takoyaki")
    ##############################################################################

while True:
    menu()
    
    time.sleep(2)
    input1 = input("\nQue quieres comer? >>")
    
    if input1==("1"):
        print("Cojes el Ramen de la nevera lo concinas y te lo comes")
        time.sleep(3)
        break
    
    
    elif input1==("2"):
        print("Cojes el Sushi de la nevera y te lo comes")
        time.sleep(3)
        break
    
    
    elif input1==("3"):
        print("Cojes el Takoyaki lo calientas un poco y te lo comes")
        time.sleep(3)
        break
    
    else:
        input("Esa opcion no esta en la lista...\nPulsa enter para continuar")
        os.system('cls')    
#############################################################################   
os.system('cls')
print("16:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
print("16:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
print("16:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
##############################################################################

print("X: terminas de comer y te sientas\n")
    
def menu2():
    print("Que quieres hacer ahora?")
    print("1-) dormir")
    print("2-) ver la television")
    print("3-) estudiar")
    
while True:
    menu2()
    input2  = input('>>')
    if input2 == ("1"):
        print("X: te vas a la cama y pocos minutos despues te acabas durmiendo")
        time.sleep(4)
    
    elif input2 == ("2"):
        print("X: enciendes la television y te quedas ahí viendola")
        time.sleep(3)
        os.system('python 2p/')
    
    
    elif input2 == ("3"):
        print("X: vas a tu habitacion, sacas los libros y empiezas a estudiar")
        time.sleep(3)
        os.system("python 2p/")
    
    
    else:{
        input(Fore.LIGHTMAGENTA_EX + "esa opcion no esta disponible...\nPulsa enter para continuar" + Style.RESET_ALL)
    }
    break
###################################################################################################################

os.system('cls')
print("20:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
print("20:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
print("20:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
################################################################################################

print("X: te despiertas cansada y decides comer un poco de comida que te habia sobrado antes\n")
time.sleep(4)
print("X: Despues te duchas te pones el pijama y te vas a intentar dormir.")

#############################################################################################################

os.system('cls')
print("23:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
print("23:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
print("23:00")
time.sleep(1)
os.system('cls')
time.sleep(1)
input(Fore.GREEN + "Has terminado tu primer dia!\n" + Style.RESET_ALL + Fore.LIGHTWHITE_EX + 
"Apartir de mañana las cosas van a cambiar y tendras mas opciones para elegir\n" + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + 
"pulsa enter cuando estes preparada para pasar de dia ;)" + Style.RESET_ALL)
