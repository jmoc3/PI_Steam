# Proyecto individual I - Recommendation System

  Este proyecto es uno de los suministrados por el Bootcamp SoyHenry, basado en el contexto de ser un Data Scientist para la empresa Steam, cuyos requerimientos se constituyen en:
  - Realizar el respectivo tratamiento de datos junto a un analisis sentimental segun las criticas de los usuarios hacia los videojuegos.
    ###### Criterio para el analisis: Debe tomar el valor '`0`' si es un comentario negativo, '`1`' si es neutral y '`2`' si es positivo. De no ser posible este análisis por estar ausente la reseña escrita, debe tomar el valor de `1`.
  - Realizar una API con un conjunto de endpoint que retornen informacion relevante respecto a los datasets suministrados. 

    - **def developer( `developer`: str ):** Devuelve la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora. 
    - **def user_data( `user_id`: str ):** Devuelve la cantidad de dinero gastado por el usuario y el porcentaje de recomendación.
    - **def user_for_genre( `genre`: str ):** Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
    - **def best_developer_year( `year`: int):** Devuelve el top 3 de desarrolladores con juegos mas recomendados por usuarios para el año dado.
    - **def developer_reviews_analysis( `developer`: str):** Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

  - Realizar un Modelo de Machine learning que retorne una lista de 5 juegos similares a uno suministrado en un endpoint.

    - **def game_recommendation( `product_id`: int):** Ingresando el id de producto, devuelve una lista con 5 juegos recomendados similares al ingresado.


     ###### PDT: Debido a la capacidad limite que tiene git para el tamaño de los archivos, los datasets que se trabajaron no se pudieron subir ya que tenian millones de registros, sin embargo google drive no posee los mismos problemas : [Archivos](https://drive.google.com/drive/folders/1kC1Wvr1krTd1S6-yIKwHvbZWdgorL9ul?usp=drive_link)

## Orden de ejecucion en caso de clonacion del repo

  1) **PI**: Desarrollo del `EDA` donde se tratan datos duplicados, nulos y irrelevantes para un mayor rendimiento en el codigo, un mejor tratamiento de los datos y por supuesto una mejor lectura de los mismos.
  2) **Recommendation_System**: Realizacion de un `WebScraping` por videojuego para el contenido necesario que analizara el modelo mediante un `Content-Based Filtering` (Item-Item)
  3) **main**: Archivo de la `API` donde se configuran las rutas http y se pone en marcha las funciones requeridas por la empresa. Para su uso clonar el repo, descargar la carpeta de los archivos, correr los notebooks y por ultimo ejecutar en la `terminal`:
  ***
  ~~~  
  uvicorn app:app --reload
  ~~~
  ***

## Uso de la API 

 Todos los servicios descritos que ofrece la api se encuentran disponibles actualmente en la nube gracias a [Render](https://render.com/), pueden encontrar la api yendo al siguiente link : [https://steam-api-v1hv.onrender.com/docs](https://steam-api-v1hv.onrender.com/docs). Algunos parametros de entrada que pueden utilizar para probar las funciones y ver sus respuestas son los siguiente:

 - ***developer* :** Valve, Days of Wonder
 - ***user_data* :** 54678907652, Shredderman962
 - ***user_for_genre* :** Adventure, Strategy
 - ***best_developer_year* :** 2012, 2013
 - ***developer_reviews_analysis* :** Re-Logic, Bohemia Interactive
 - ***game_recommendation* :** 431240 ('Golf With Your Friends'), 12110 ('Grand Theft Auto: Vice City')

  ## Tecnologias

  - Python<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width=20 align="center" style="margin-left:10px" alt="Python icon">
  - Pandas<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/225px-Pandas_mark.svg.png" width=20 align="center" style="margin-left:10px" alt="Python icon">
  - Numpy<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1200px-NumPy_logo_2020.svg.png" width=60 align="center" style="margin-left:10px" alt="Python icon">
  - Requests<image src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Requests-logo.png" width=20 align="center" style="margin-left:10px" alt="Python icon">
  - BeautifulSoup<image src="https://funthon.files.wordpress.com/2017/05/bs.png?w=772" width=80 align="center" style="margin-left:10px" alt="Python icon">
  - Nltk<image src="https://miro.medium.com/v2/resize:fit:592/1*YM2HXc7f4v02pZBEO8h-qw.png" width=20 align="center" style="margin-left:10px" alt="Python icon">
  - Sklearn<image src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/2560px-Scikit_learn_logo_small.svg.png" width=20 align="center" style="margin-left:10px" alt="Python icon">
  - FastAPI<image src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width=60 align="center" style="margin-left:10px" alt="Python icon">
  - Conda<image src="https://docs.crc.nd.edu/_images/conda.png" width=50 align="center" style="margin-left:10px" alt="Python icon">
  - Uvicorn<image src="https://www.uvicorn.org/uvicorn.png" width=20 align="center" style="margin-left:10px" alt="Python icon">

