import pandas as pd

game_item = pd.read_parquet('./clean_datasets/game_items.parquet')
all_dfs = pd.read_parquet('./clean_datasets/all_dfs.parquet')

def developer(developer:str):
  '''
  Devuelve la cantidad de items y el porcentaje de contenido Free por año
  segun empresa desarrolladora.
  '''
  df = game_item[game_item['developer']==developer]
  items = df.groupby('release_date')['developer'].count().reset_index()
  free = df[df['price']==0].groupby('release_date')['developer'].count().reset_index()
  
  
  rows = []
  merge = pd.merge(free,items,on='release_date')
  for x in items.itertuples():
    if x.release_date in list(merge['release_date']):
      free_content = round((merge[merge['release_date']==x.release_date]['developer_x']/x.developer)*100,2).item()
    else:
      free_content = 0
    
    rows.append({"Año":x.release_date,"Cantidad de items":x.developer,"Contenido Free":f"{free_content}%"})
  res = {
    developer:rows
  }
  return res

def user_data(user_id:str):
  '''
  Devuelve la cantidad de dinero gastado por el usuario mas el 
  porcentaje de recomendacion y la cantidad de items
  '''
  df = all_dfs[all_dfs['user_id']==user_id]
  money = df['price'].sum()
  items = len(df)

  user_reviews = df[df['user_id']==user_id]
  recommendation = (user_reviews['recommend'].sum()/len(user_reviews))*100

  res = {
    "Usuario X": user_id,
    "Dinero gastado": round(money,2),
    "% de recomendacion": f"{round(recommendation,2)}%",
    "Cantidad de items": items
  }

  return  res

def user_for_genre(genre:str):
  '''
  Devuelve el usuario con mas horas jugadas para el genero dado 
  y una lista de acumulaciones de horas jugadas por año
  '''
  df = game_item[game_item['genres']==genre]

  user = df.groupby('user_id')['playtime_forever'].sum().sort_values(ascending=False).index[0]
  hours = df[df['user_id']==user].groupby('release_date')['playtime_forever'].sum()

  year = []
  for i,x in enumerate(hours):
    if x!=0:
      year.append({"Año":hours.index[i].item(),"Horas":int(x)})

  res = {
    f"Usuario con mas horas jugadas para Genero {genre}":user,
    "Horas Jugadas": year
  }
  return res

def best_developer_year(year:int):
  '''
  Devuelve el top 3 de desarrolladores con juegos mas recomendados por usuarios para el año dado.
  '''
  df = all_dfs[pd.to_datetime(all_dfs['posted']).dt.year == int(year)].copy()
  df['posted'] = pd.to_datetime(df['posted']).dt.year
  recommendation = df.groupby('developer')['recommend'].sum().sort_values(ascending=False)[:3]
  
  res = {
    "Año":year,
    "Res":[
      {"Puesto 1":recommendation.index[0]},
      {"Puesto 2":recommendation.index[1]},
      {"Puesto 3":recommendation.index[2]}
    ]
  }
  return res

def developer_reviews_analysis(developer:str):
  '''
  Devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un analisis de sentimiento como valor positivo o negativo.
  '''
  df = all_dfs[all_dfs['developer']==developer].copy()
  sentiments = df['sentiment'].value_counts()
  res = {
    developer:{
      "Negative":sentiments.values[2].item(), 
      "Positive":sentiments.values[0].item()
    }
  }
  return res

import ast

games_similarities = pd.read_csv('./clean_datasets/games_similarities.csv') 
games_similarities.set_index('Unnamed: 0', inplace=True)
 
def game_recommendation(product_id:int):
  return ast.literal_eval(games_similarities.to_dict()['0'][product_id]) 