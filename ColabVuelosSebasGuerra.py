

Link: https://colab.research.google.com/drive/1pUS0xyjv7xs7qiWzG2buhlZeBRPLwFBA?usp=sharing



info_vuelos = pd.read_csv('/content/drive/MyDrive/Vuelos/BaseDatosFinal.csv', encoding='ISO-8859-1', sep=';')

import pandas as pd

info_vuelos = pd.read_csv('/content/drive/MyDrive/Vuelos/BaseDatosFinal.csv', encoding='ISO-8859-1', sep=';')

info_vuelos

info_vuelos.shape

list(info_vuelos['Destino'].drop_duplicates().tail(5))

list(info_vuelos['Edad'].drop_duplicates())

list(info_vuelos['Origen'].drop_duplicates())

conteo_Edad = info_vuelos['Edad'].value_counts()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Edad': [25, 30, 35, 40, 45],
        'Precio_vuelo': [200, 250, 180, 300, 220],
        'Discapacidad': ['No', 'Si', 'No', 'No', 'Si']}

info_vuelos = pd.DataFrame(data)

print(info_vuelos)

sns.scatterplot(x='Edad', y='Precio_vuelo', data=info_vuelos, hue='Discapacidad')
plt.show()


import pandas as pd

data = {'Precio_vuelo': [200, 250, 180, 300, 220]}
info_vuelos = pd.DataFrame(data)

print(info_vuelos)

mean_price = info_vuelos['Precio_vuelo'].mean()
median_price = info_vuelos['Precio_vuelo'].median()


print(f'Media del precio del vuelo: {mean_price}')
print(f'Mediana del precio del vuelo: {median_price}')