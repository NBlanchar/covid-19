# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:08:13 2021

@author: nefer
"""

import pandas as pd
url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# Tratamiento de Datos
prueba = data.columns
for x in range(len(prueba)):
    a = 'Edad'
    b = 'Unidad de medida de edad'
    c = 'Pertenencia étnica'
    if(prueba[x] != a and prueba[x] != b and prueba[x] != c):
        data[prueba[x]] = data[prueba[x]].str.upper()


# Ejercicio 1
print(f'El numero de casos de contagiados en el pais es: {data.shape[0]-1:,}')

# Ejercicio 2
MunicipiosAfectados = data.groupby('Nombre municipio').size().shape[0]
print(f"El numero de municipios afectados es: {MunicipiosAfectados:,}")

# Ejercico 3
MunicipiosAfectados = data.groupby('Nombre municipio').size()
print(f"Los municipios afectados son: \n {MunicipiosAfectados}")

# Ejercicio 4
AtencionCasa = data[(data['Ubicación del caso'] == 'CASA')].shape[0]
print(f'El numero de personas que son atendidas en casa son: {AtencionCasa:,}')
