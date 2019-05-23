import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('1. dataFifa.csv')

age = np.array(df['Age'])
overall = np.array(df['Overall'])


# print(len(age))
age1 = []
age2 = []
age3 = []
age4 = []
overall1 = []
overall2 = []
overall3 = []
overall4 = []

for i in range(len(age)):
    if age[i] > 25 and overall[i] > 85:
        age1.append(age[i])
        overall1.append(overall[i])
    elif age[i] > 25 and overall[i] <= 85:
        age2.append(age[i])
        overall2.append(overall[i])
    elif age[i] <= 25 and overall[i] > 85:
        age3.append(age[i])
        overall3.append(overall[i])
    else:
        age4.append(age[i])
        overall4.append(overall[i])



plt.figure('BOLA')
plt.subplot(111)
plt.title('FIFA 2019')
plt.xlabel('Umur')
plt.ylabel('Overall')
plt.xticks(rotation=90)               # atur rotasi dari value x dan y
plt.yticks(rotation=0)
plt.scatter(age1, overall1, color='r', marker='.')
plt.scatter(age2, overall2, color='g', marker='.')
plt.scatter(age3, overall3, color='b', marker='.')
plt.scatter(age4, overall4, color='y', marker='.')



# plt.grid(True)

plt.legend(
    ['Aged Talented', 'Aged NoTalented ', 'Young Talented', 'Young RAW'],
    scatterpoints=1,
    loc='upper right',
    ncol=1,
    fontsize=6,
   )


plt.tight_layout()








plt.show()


