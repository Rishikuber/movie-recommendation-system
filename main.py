from fastapi import FastAPI
from Model.recommender_model import recommend_movies

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Movie Recommendation API is running"}

@app.get("/recommend/{movie_name}")
def get_recommendations(movie_name: str):
    
    results = recommend_movies(movie_name)

    return {
        "movie": movie_name,
        "recommendations": results
    }