import os
from colorama import *
os.system('cls')
input1 = input("estas segura de que quieres salir ?\ny/n >>")

if input1=="y":{
    os.system('python x.py')
}
elif input1=="Y":{
     os.system('python x.py')
}
elif input1=="n":{
     os.system('python inicio1.py')
}
elif input1=="N":{
    os.system('python inicio1.py')
}

else: 
    input("esa opcion no existe...\npulsa enter para continuar")