from fastapi import FastAPI
import pandas as pd
import numpy as np

#El siguente archivo corresponde "A los requerimientos y solo estas transformaciones" solicitadas
#data = pd.read_csv("data.csv")

url="https://raw.githubusercontent.com/TeusM224/csvData/main/data.csv"
data = pd.read_csv(url)

""" Ahora bien, personalmente hubiera preferido realizar otras transformaciones que permitieran
volver mas eficiente el codigo y que además correspondieran al ciclo recomendado de la data me 
explico, me hubiese gustado adicionar una columna 'plataforma', haber realizado imputaciones o 
transformaciones de acuerdo al caso, etc.
"""

#Desarrollo API

app = FastAPI(title='Proyecto Individual 1',
                description= 'Proyecto individual 1 de ingenieria de datos',
                version='1.0.1')

#Welcome
@app.get('/') 
async def index ():
    return {"message": "Hello World"}


#Query 1
@app.get('/get_word_count')
async def get_word_count(plataforma:str, palabra:str):

    data_netflix = data[data['id'].str.startswith('n', na=False)]
    data_amazon = data[data['id'].str.startswith('a', na=False)]
    data_hulu = data[data['id'].str.startswith('h', na=False)]
    data_disney = data[data['id'].str.startswith('d', na=False)]

    if (plataforma == 'amazon') or (plataforma == 'Amazon'):
        return {len(data_amazon[data_amazon.title.str.contains(palabra, case=False)])}

    elif (plataforma == 'netflix') or (plataforma == 'Netflix'):
        return {len(data_netflix[data_netflix.title.str.contains(palabra, case=False)])}

    elif (plataforma == 'hulu') or (plataforma == 'Hulu'):
        return {len(data_hulu[data_hulu.title.str.contains(palabra, case=False)])}

    elif (plataforma == 'disney') or (plataforma == 'Disney'):
        return {len(data_disney[data_disney.title.str.contains(palabra, case=False)])}
    

#Query 2
@app.get('/get_score_count')
async def get_score_count(plataforma:str, xx:int, anio:int):

    data_netflix = data[data['id'].str.startswith('n', na=False)]
    data_amazon = data[data['id'].str.startswith('a', na=False)]
    data_hulu = data[data['id'].str.startswith('h', na=False)]
    data_disney = data[data['id'].str.startswith('d', na=False)]

    if (plataforma == 'amazon') or (plataforma == 'Amazon'):
        return {len(data_amazon[(data_amazon['release_year']== anio)&(data_amazon['score']> xx)])}

    elif (plataforma == 'netflix') or (plataforma == 'Netflix'):
        return {len(data_netflix[(data_netflix['release_year']== anio)&(data_netflix['score']> xx)])}

    elif (plataforma == 'hulu') or (plataforma == 'Hulu'):
        return {len(data_hulu[(data_hulu['release_year']== anio)&(data_hulu['score']> xx)])}

    elif (plataforma == 'disney') or (plataforma == 'Disney'):
        return {len(data_disney[(data_disney['release_year']== anio)&(data_disney['score']> xx)])}


#Query3
@app.get('/get_second_score')
def get_second_score(plataforma):
    data_netflix = data[data['id'].str.startswith('n', na=False)]
    data_amazon = data[data['id'].str.startswith('a', na=False)]
    data_hulu = data[data['id'].str.startswith('h', na=False)]
    data_disney = data[data['id'].str.startswith('d', na=False)]

    if (plataforma == 'amazon') or (plataforma == 'Amazon'):
        return{(data_amazon.sort_values(['score','title'], ascending=[False,True]).loc[(data_amazon['type'] == 'movie'), :].iloc[1][['title','score']].tolist())[0]}
    
    elif (plataforma == 'netflix') or (plataforma == 'Netflix'):
        return{(data_netflix.sort_values(by=['score','title'], ascending=[False,True]).loc[(data_netflix['type']== 'movie'), :].iloc[1][['title','score']].tolist())[0]}

    elif (plataforma == 'hulu') or (plataforma == 'Hulu'):
        return {(data_hulu.sort_values(by=['score','title'], ascending=[False,True]).loc[(data_hulu['type']== 'movie'), :].iloc[1][['title','score']])[0]}

    elif (plataforma == 'disney') or (plataforma == 'Disney'):
        return {(data_disney.sort_values(by=['score','title'], ascending=[False,True]).loc[(data_disney['type']== 'movie'), :].iloc[1][['title','score']])[0]}


#Query4
@app.get('/get_max_duration')
async def get_max_duration(plataforma:str, tipo_duracion:str, anio:int):

    data_netflix = data[data['id'].str.startswith('n', na=False)]
    data_amazon = data[data['id'].str.startswith('a', na=False)]
    data_hulu = data[data['id'].str.startswith('h', na=False)]
    data_disney = data[data['id'].str.startswith('d', na=False)]

    if (plataforma == 'amazon') or (plataforma == 'Amazon'):
        return {(data_amazon[(data_amazon['release_year'] == anio)&(data_amazon['duration_type']== tipo_duracion)]['duration_int'].max())}

    elif (plataforma == 'netflix') or (plataforma == 'Netflix'):
        return {(data_netflix[(data_netflix['release_year'] == anio)&(data_netflix['duration_type']== tipo_duracion)]['duration_int'].max())}

    elif (plataforma == 'hulu') or (plataforma == 'Hulu'):
        return {(data_hulu[(data_hulu['release_year'] == anio)&(data_hulu['duration_type']== tipo_duracion)]['duration_int'].max())}

    elif (plataforma == 'disney') or (plataforma == 'Disney'):
        return {(data_disney[(data_disney['release_year'] == anio)&(data_disney['duration_type']== tipo_duracion)]['duration_int'].max())}


#Query5
@app.get('/get_rating_count')
async def get_rating_count(categoria:str):
    
    return {data[['rating']].loc[(data['rating']==categoria), :].value_counts().tolist()[0]}
