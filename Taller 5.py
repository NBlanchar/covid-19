# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:08:13 2021

@author: nefer
"""

import pandas as pd
url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# Tratamiento de Datos
TD = data.columns
for x in range(len(TD)):
    a = 'Edad'
    b = 'Unidad de medida de edad'
    c = 'Pertenencia étnica'
    if(TD[x] != a and TD[x] != b and TD[x] != c):
        data[TD[x]] = data[TD[x]].str.upper()


# Ejercicio 1
print(f'El numero de casos de contagiados en el pais es: {data.shape[0]-1:,}')

# Ejercicio 2
Resultado = data.groupby('Nombre municipio').size().shape[0]
print(f"El numero de municipios afectados es: {Resultado:,}")

# Ejercico 3
Resultado = data.groupby('Nombre municipio').size()
print(f"Los municipios afectados son: \n {Resultado}")

# Ejercicio 4
Resultado = data[(data['Ubicación del caso'] == 'CASA')].shape[0]
print(f'El numero de personas que son atendidas en casa son: {Resultado:,}')

# Ejercicio 5
Resultado = data[(data['Recuperado'] == 'RECUPERADO')].shape[0]
print(f'El numero de personas que son atendidas en casa son: {Resultado:,}')

# Ejercicio 6
Resultado = data[(data['Recuperado'] == 'FALLECIDO')].shape[0]
print(f'El numero de personas fallecidas son: {Resultado:,}')
