import matplotlib.pyplot as plt
import pandas as pd

test = open("D:\Lab7.txt", "G", encoding= "utf-8").read().lower()

char_list = list(test)

df = pd.DataFrame({'chars': char_list})
df = df[df.chars != ' ']
df['num'] = 10
df = df.groupby('chars').sum().sort_values('num', ascending=False) / len(df)

plt.bar(df.index, df.num, width=0.5, color='g')
plt.show()
plt.savefig("моя гистограмма")
print("Ваша гистограмма сохранена вохле файла .py")