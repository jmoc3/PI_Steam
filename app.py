from fastapi import FastAPI
from api_functions import developer, user_data, user_for_genre, best_developer_year,developer_reviews_analysis, game_recommendation

app = FastAPI()

@app.get('/')
def home():
  return {'Message':'Welcome world'}

@app.get('/developer/{dev}')
def developer_endpoint(dev:str):
    try:
        res = developer(dev)
        return res
    except Exception as e:
        return {
            'Message':'Something goes wrong',
            'Error':str(e) }
    
@app.get('/userdata/{user_id}')
def user_data_endpoint(user_id:str):
    try:
        res = user_data(user_id)
        return res
    except Exception as e:
        return {
            'Message':'Something goes wrong',
            'Error':str(e) }
    
@app.get('/userforgenre/{genre}')
def user_for_genre_endpoint(genre:str):
    try:
        res = user_for_genre(genre)
        return res
    except Exception as e:
        return {
            'Message':'Something goes wrong',
            'Error':str(e) }
    
@app.get('/bestdeveloperyear/{year}')
def best_developer_year_endpoint(year:int):
    try:
        res = best_developer_year(year)
        return res
    except Exception as e:
        return {
            'Message':'Something goes wrong',
            'Error':str(e) }
    
@app.get('/developerreviewsanalysis/{developer}')
def developer_reviews_analysis_endpoint(developer:str):
    try:
        res = developer_reviews_analysis(developer)
        return res
    except Exception as e:
        return {
            'Message':'Something goes wrong',
            'Error':str(e) }

@app.get('/gamerecommendation/{product_id}')
def game_recommendation_endpoint(product_id:int):
    try:
        res = game_recommendation(product_id)
        return res
    except Exception as e:
        return {
            'Message':'Something goes wrong',
            'Error':str(e) }