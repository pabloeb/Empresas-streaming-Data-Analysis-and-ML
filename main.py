
# REQUERIMIENTOS API:   ---------------------------------------------------------------------------------------------

# Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

# Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

# --------------------------------------------------------------------------------------------------------------------

from fastapi import FastAPI,Query,routing
import pandas as pd
from fastapi.responses import RedirectResponse
import numpy as np

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from typing import Union


#instanciar el objeto app de FastAPI
app = FastAPI()

#Esta función devuelve la película más larga en función de las variables seleccionadas por el usuari (año, tipo de duración y plataforma)

""" # Código anulado por ser una versión superada- Fucionalmente correcto
@app.get("/")
def get_max_duration(year:int | None=None, platform : str = Query(None, enum=["Netflix", "Hulu", "Amazon","Disney"]), duration_type:str = Query(None, enum=["minutes", "season"])):
    
    #si el usuario introduce un valo diferente a los años entre 1920 y 2021 devuelve un mensaje de reingresar datos
    
    if year is not None and year not in range(1920, 2022):
        return "Por favor ingrse un añ válido entre 1920 y 2021."
    
           
    else:
        dataframe = pd.read_csv("df_result.csv")
        if year == None and platform == None:
            df_filtrado = dataframe.loc[dataframe['duration_int'] == dataframe['duration_int'].max()]
            return f"La película con mayor duración es : {df_filtrado['title'].values[0]} con una duración de {df_filtrado['duration_int'].values[0]} minutos"


        if year != None and platform == None:
            df_filtrado = dataframe.loc[dataframe['release_year'] == year]
            df_filtrado = df_filtrado.sort_values(by='duration_int', ascending=False)
            titulo = df_filtrado.iloc[0,2]
            duracion =df_filtrado.iloc[0,11]
            return f"La película con mayor duración es : {titulo} con una duración de {duracion} minutos"
        
        if year == None and platform != None:
            nombres =["Hulu","Netflix","Disney","Amazon"]
            for i,e in enumerate(nombres):
                if e == platform:
                    a = e[0].lower()
                    df_filtrado = dataframe[dataframe['id'].str.startswith(a)]
                    df_filtrado = df_filtrado.sort_values(by=["duration_int"], ascending =False)
                    titulo = df_filtrado.iloc[0,2]
                    duracion = df_filtrado.iloc[0,11]
                    return f"La película con mayor duración es : {titulo} con una duración de {duracion} minutos"
            
        if year != None and platform != None:
             nombres =["Hulu","Netflix","Disney","Amazon"]
             for i,e in enumerate(nombres):
                if e == platform:
                    a = e[0].lower()
                    df_filtrado = dataframe[dataframe['id'].str.startswith(a)]
                    df_filtrado = df_filtrado[df_filtrado["release_year"]==year]
                    df_filtrado = df_filtrado.sort_values(by=["duration_int"], ascending =False)
                    titulo = df_filtrado.iloc[0,2]
                    duracion = df_filtrado.iloc[0,11]
                    return f"La película con mayor duración es : {titulo} con una duración de {duracion} minutos"
"""

@app.get("/consulta1")
def get_max_duration(
    year: Union[int, None] = None, 
    platform: str = Query(None, enum=["Netflix", "Hulu", "Amazon","Disney"]), 
    duration_type: str = Query(None, enum=["min", "season"])):

    if year is not None and year not in range(1920, 2022):
        return f"Por favor ingrese un año válido entre 1920 y 2021."
        
    else:
        dataframe = pd.read_csv("df_result.csv")
        nombres =["Hulu","Netflix","Disney","Amazon"]
        if platform in nombres:
            for i,e in enumerate(nombres):
                if e == platform:
                    a = e[0].lower()
                    df_filtrado = dataframe[dataframe['id'].str.startswith(a)]
        else:
            df_filtrado = dataframe

        if year != None:
            df_filtrado = df_filtrado[df_filtrado['release_year'] == year]

        if duration_type != None:
            df_filtrado = df_filtrado[df_filtrado['duration_type'] == duration_type] 
            
            
    df_filtrado = df_filtrado.sort_values(by=["duration_int"], ascending=False)
    titulo = df_filtrado.iloc[0,2]
    resultado = df_filtrado.duration_int.max()
    return f" La pelicula de mayor duración es {titulo} con {resultado} {duration_type}"


#Esta función devuelve la cantidad de películas por plataforma, año y score.
@app.get("/consulta2")
def get_score_count(year: Union[int, None] = None, 
    platform: str = Query(None, enum=["Netflix", "Hulu", "Amazon","Disney"]), 
    scored: float = Query(None, enum=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])):

    if year is not None and year not in range(1920, 2022):
        return "Por favor ingrse un añ válido entre 1920 y 2021."
        
    else:
        dataframe = pd.read_csv("df_result.csv")
        nombres =["Hulu","Netflix","Disney","Amazon"]
        if platform in nombres:
            for i,e in enumerate(nombres):
                if e == platform:
                    a = e[0].lower()
                    df_filtrado = dataframe[dataframe['id'].str.startswith(a)]
        else:
            df_filtrado = dataframe

        if year != None:
            df_filtrado = df_filtrado[df_filtrado['release_year'] == year]

        if scored != None:
            df_filtrado = df_filtrado[df_filtrado['promedio_raiting'] > scored] 
    
        resultado = df_filtrado.id.value_counts().sum()
        return f" La cantidad total de películas para las variables solicitadas es igual a {resultado}"
    

# Esta función devuelve la cantidad de películas por plataforma

@app.get("/consulta3")
def get_count_platform(platform : str = Query(None, enum=["Netflix", "Hulu", "Amazon","Disney"])):
       
    dataframe = pd.read_csv("df_result.csv")
    nombres =["Hulu","Netflix","Disney","Amazon"]
    if platform in nombres:
        for i,e in enumerate(nombres):
            if e == platform:
                a = e[0].lower()
                df_filtrado = dataframe[dataframe['id'].str.startswith(a)]
    else:
        df_filtrado = dataframe

       
    resultado = df_filtrado.id.value_counts().sum()
    return f" La cantidad total de películas para la plataforma solicitada es igual a {resultado}"


app.mount("/portada", StaticFiles(directory="portada"), name="portada")

@app.get("/", response_class=HTMLResponse)
async def read_root():

    html_content = """
    <html>
        <head>
            <title>FastAPI</title>
        </head>
        <body>
            <a href="/docs">
                <img src="/portada/portada.png" alt="portada">
            </a>
        </body>
    </html>
    """
    return html_content

   

   