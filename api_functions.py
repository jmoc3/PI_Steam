def user_data(user_id:str):
  '''
  Devuelve la cantidad de dinero gastado por el usuario mas el 
  porcentaje de recomendacion y la cantidad de items
  '''
  return "{'Usuario X':usuariorandom, 'Dinero gastado':200, '% de recomendacion':20%,'cantidad de items':5}"

def user_for_genre(genere:str):
  '''
  Devuelve el usuario con mas horas jugadas para el genero dado 
  y una lista de acumulaciones de horas jugadas por año
  '''

  return "{'Usuario con más horas jugadas para Género X' : us213ndjss09sdf, 'Horas jugadas':[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}"

def best_developer_year(year:int):
  '''
  Devuelve el top 3 de desarrolladores con juegos mas recomendados por usuarios para el año dado.
  '''

  return "[{'Puesto 1' : X}, {'Puesto 2' : Y},{'Puesto 3': Z}]"

def developer_reviews_analysis(developer:str):
  '''
  Devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un analisis de sentimiento como valor positivo o negativo.
  '''

  return "{'Valve' : [Negative = 182, Positive = 278]}"