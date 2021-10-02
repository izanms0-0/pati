import os
import time
from tqdm import *
tareas = 100

os.system('pip install colorama')
os.system('pip install tqdm')
os.system('cls')
from colorama import *

init()

time.sleep(2)

print(Fore.GREEN + "terminando de instalar el juego..." + Style.RESET_ALL)
for i in tqdm(range(tareas),  
              desc ="cargando juego.."): 
    time.sleep(0.002) 
    
os.system('cls')
print(Fore.GREEN + "juego instalado disfruta ;)" + Style.RESET_ALL)
time.sleep(4)

os.system('python inicio.py')