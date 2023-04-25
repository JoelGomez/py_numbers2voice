"""
convierte texto a voz, esto nos puede servir para el bingo
guarda la lista final en el archivo salidas.txt para su 
posterior estudio estadistico
"""

import pyttsx3
import numpy as np

engine = pyttsx3.init()
nums = []
contador = 0
char_nums = ''

while len(nums) < 75:
    val = str(np.random.randint(1,76))
    if val not in nums:
        nums.append(val)
        contador += 1
    else:
        continue

    engine.say(val)
    print(contador, val)
    engine.runAndWait()


file = open('salidas.csv','a',encoding=None)
char_nums = ",".join(nums)
file.write('\n' + char_nums)
file.close()
