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
data['Nombre departamento'].replace('BARRANQUILLA', 'ATLANTICO', inplace = True)
data['Nombre departamento'].replace('CARTAGENA', 'BOLIVAR', inplace = True)
data['Nombre departamento'].replace('STA MARTA D.E.', 'MAGDALENA', inplace = True)
data['Nombre departamento'].replace('BOGOTA', 'CUNDINAMARCA', inplace = True)

# Ejercicio 1
print(f'El numero de casos de contagiados en el pais es: {data.shape[0]-1:,}')

# Ejercicio 2
Resultado = data.groupby('Nombre municipio').size().shape[0]
print(f"El numero de municipios afectados es: {Resultado:,}")

# Ejercico 3
Resultado = data.groupby('Nombre municipio').size()
print(f"Los municipios afectados son: \n{Resultado}")

# Ejercicio 4
Resultado = data[(data['Ubicación del caso'] == 'CASA')].shape[0]
print(f'El numero de personas que son atendidas en casa son: {Resultado:,}')

# Ejercicio 5
Resultado = data[(data['Recuperado'] == 'RECUPERADO')].shape[0]
print(f'El numero de personas que son atendidas en casa son: {Resultado:,}')

# Ejercicio 6
Resultado = data[(data['Recuperado'] == 'FALLECIDO')].shape[0]
print(f'El numero de personas fallecidas son: {Resultado:,}')

# Ejercicio 7
Resultado = data['Tipo de contagio'].value_counts()
print(f'El orden de los tipos de contagio es: \n{Resultado}')

# Ejercicio 8
Resultado = data.groupby('Nombre departamento').size().shape[0]
print(f"El numero de departamentos afectados es: {Resultado:,}")

# Ejercico 9
Resultado = data.groupby('Nombre departamento').size()
print(f"Los departamentos afectados son: \n{Resultado}")

# Ejercicio 10
Resultado = data['Estado'].value_counts()
print(f'El orden de los tipos de atención es: \n{Resultado}')

# Ejercicio 11
Resultado = data['Nombre departamento'].value_counts().head(10)
print(f'El orden de los departamentos con mas contagios es: \n{Resultado}')

# Ejercicio 12
fallecidos = data[(data['Recuperado'] == 'FALLECIDO')]
Resultado = fallecidos['Nombre departamento'].value_counts().head(10)
print(f'El orden de los departamentos con mas fallecidos es: \n{Resultado}')

# Ejercicio 13
recuperados = data[(data['Recuperado'] == 'RECUPERADO')]
Resultado = recuperados['Nombre departamento'].value_counts().head(10)
print(f'El orden de los departamentos con mas recuperados es: \n{Resultado}')

# Ejercicio 14
Resultado = data['Nombre municipio'].value_counts().head(10)
print(f'El orden de los municipios con mas contagios es: \n{Resultado}')

# Ejercicio 15
fallecidos = data[(data['Recuperado'] == 'FALLECIDO')]
Resultado = fallecidos['Nombre municipio'].value_counts().head(10)
print(f'El orden de los municipios con mas fallecidos es: \n{Resultado}')

# Ejercicio 16
recuperados = data[(data['Recuperado'] == 'RECUPERADO')]
Resultado = recuperados['Nombre departamento'].value_counts().head(10)
print(f'El orden de los municipios con mas recuperados es: \n{Resultado}')

# Ejercicio 17
Resultado = data['Nombre departamento'].value_counts()
print(f'El orden de los departamentos con mas contagios es: \n{Resultado}')

# Ejercicio 18
a = 'Sexo'
b = 'Nombre departamento'
c = 'Nombre municipio'
Resultado = data.groupby([a, b, c, ]).size()
print(f'El listado de contagiados por sexo y ciudad es: \n{Resultado}')

# Ejercicio 19
a = 'Sexo'
b = 'Nombre departamento'
c = 'Nombre municipio'
Resultado = data.groupby([a, b, c, ]).mean()
print(f'El promedio de edad en los municipios es: \n{Resultado}')

# Ejercicio 20
Resultado = data['Nombre del país'].value_counts()
print(f'El orden de contagiados segun su procedencia es: \n{Resultado}')

# Ejercicio 21
Resultado = data['Fecha de notificación'].value_counts()
print(f'las fechas donde se presentaron mas contagios so: \n{Resultado}')

# Ejercicio 30
fallecidos = data[(data['Recuperado'] == 'FALLECIDO')]
Resultado = fallecidos['Edad'].value_counts()
print(f'El orden por edad con mas fallecidos es: \n{Resultado}')
