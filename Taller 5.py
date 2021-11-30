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


