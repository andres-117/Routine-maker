# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:46:50 2020

@author: Andres
"""

import pandas as pd
import random as random

excel = pd.read_excel("Ejercicios.xlsx")

dificultad = 10

def creador_rutina(original_db):
    dificultad = 10
    ejercicios = original_db
    global rutina
    rutina = pd.DataFrame()
    valor_rutina = 0
    
    ejercicios["Total"] = ejercicios.sum(axis=1) #agrega columna de total
      
    while valor_rutina < dificultad:
        
        comp = dificultad - valor_rutina
        ejercicios = ejercicios[ejercicios.Total <= comp]
        ejercicios.reset_index(inplace=True, drop=True)
        
        if ejercicios.empty == True:
            
            rutina = rutina[excel.columns]
            print(rutina)
            
            break
                
        a = random.randint(0,len(ejercicios.index)-1)
        rutina = rutina.append(ejercicios.iloc[a , :], sort=False)
        ejercicios = ejercicios.drop([a])
        valor_rutina = rutina["Total"].sum()
        
       
creador_rutina(excel)
