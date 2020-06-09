# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:46:50 2020

@author: Andres
"""

import pandas as pd
import random as random

excel = pd.read_excel("Ejercicios.xlsx")

def creador_rutina(original_db):
   
    print("Dificultades disponibles: \n.-Facil = 6\n.-Normal = 10\n.-Fuerte = 20")
    dif_range = ["6","10","20"]
    dificultad = input("Indica la dificultad: ")
    
    while dificultad not in dif_range: #para asegurar que indican un valor valido
        print("Selecciona una dificultad disponible: ")
        print("Dificultades disponibles: \n.-Facil = 6\n.-Normal = 10\n.-Fuerte = 20")
        dificultad = input("Indica la dificultad: ")
   
    dificultad = int(dificultad) #los input entran como str siempre
    
    ejercicios = original_db
    global rutina
    rutina = pd.DataFrame()
    valor_rutina = 0
    
    ejercicios["Total"] = ejercicios.sum(axis=1) #agrega columna de total
      
    while valor_rutina <= dificultad:
        
        comp = dificultad - valor_rutina
        ejercicios = ejercicios[ejercicios.Total <= comp]
        ejercicios.reset_index(inplace=True, drop=True)
        
        if ejercicios.empty == True:
            
            rutina = rutina[original_db.columns]
            print(rutina)
            
            break
                
        a = random.randint(0,len(ejercicios.index)-1)
        rutina = rutina.append(ejercicios.iloc[a , :], sort=False)
        ejercicios = ejercicios.drop([a])
        valor_rutina = rutina["Total"].sum()
        
       



creador_rutina(excel)
