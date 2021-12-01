import pandas as pd
from matplotlib import pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

question = str()
point = 0
test =  open("D:\Lab7.txt", "G", encoding= "utf-8").read().lower()
for i in test:
    if '?' in i:
        question = question + ("?")
    elif '!' in i:
        question = question + ("!")
    elif '.' in i:
        question = question + (".")
    elif '.' in i:
        question = question + ("...")

print (point)
char_list = list(question)

