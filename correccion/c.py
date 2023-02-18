#Archivo de Correccion:

# Editar variables con comentario al lado:

import os
import colorama
import configparser
import time

config = configparser.ConfigParser()
config.read('c.ini')

def show_grade():
  grade = config['GRADE']['final_result']
  
  if grade == "Sobresaliente":
    return colorama.Fore.GREEN + "SOBRESALIENTE"
  elif grade == "Apto":
    return colorama.Fore.MAGENTA + "APTO"
  elif grade == "No Apto":
    return colorama.Fore.REED + "NO APTO"


ascci_art = """ 
   _____                             _                 _______                     ______ ___ ______ 
  / ____|                           (_)            _  |__   __|                   |____  / _ \____  |
 | |     ___  _ __ _ __ ___  ___ ___ _  ___  _ __ (_)    | | __ _ _ __ ___  __ _      / / | | |  / / 
 | |    / _ \| '__| '__/ _ \/ __/ __| |/ _ \| '_ \       | |/ _` | '__/ _ \/ _` |    / /| | | | / /  
 | |___| (_) | |  | | |  __/ (_| (__| | (_) | | | |_     | | (_| | | |  __/ (_| |   / / | |_| |/ /   
  \_____\___/|_|  |_|  \___|\___\___|_|\___/|_| |_(_)    |_|\__,_|_|  \___|\__,_|  /_(_) \___//_/    
  ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______  
 |______|______|______|______|______|______|______|______|______|______|______|______|______|______| 
  ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______  
 |______|______|______|______|______|______|______|______|______|______|______|______|______|______|                                                                                                                                                                                                             
"""

print(ascci_art)
print('\n')
print('\n')

print("La Profesora: " + config['TEACHER DATA']['name'] + " que imparte la asignatura: " + config['TEACHER DATA']['subject'] + " ha corregido la Tarea!!")
time.sleep(2)
print("Tu nota es la siguiente" + show_grade())
time.sleep(2)
print("GRACIAS POR REVISAR SU CALIFICACIÓN!")
