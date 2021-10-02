import os
import time
from tqdm import tqdm

tareas = 100
os.system("cls")

fichero = open("nom.py", 'w')
while True:
    
    
    input1 = input('quieres elegir el nombre del personaje? y/n >>')
    if input1=="y":{
        os.system('cls')
    }

    elif input1=="n":{
    os.system('python inicio1.py')
    }

    else:{
    input('Esa opcion no esta en la lista...\npulsa enter para continuar')
    }
    break
#####################
nombre = input('Cómo quieres que se llame el persnaje?  >>')

fichero.write("def nombre1(arg):" + f"\n    print('{nombre}')")
fichero.close()
time.sleep(2)
for i in tqdm(range(tareas),  
              desc ="Cargando nombre..."): 
    time.sleep(0.001)
    os.system('python historia3/h3.py')