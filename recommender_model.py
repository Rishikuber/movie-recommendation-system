import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("recommender_movies.csv")
ratings = pd.read_csv("recommender_ratings.csv")

data = pd.merge(ratings, movies, on="movie_id")

user_movie_matrix = data.pivot_table(
    index="user_id",
    columns="title",
    values="rating"
).fillna(0)

movie_similarity = cosine_similarity(user_movie_matrix.T)

movie_similarity_df = pd.DataFrame(
    movie_similarity,
    index=user_movie_matrix.columns,
    columns=user_movie_matrix.columns
)

def recommend_movies(movie_name, num_recommendations=5):

    similar_scores = movie_similarity_df[movie_name]

    similar_movies = similar_scores.sort_values(ascending=False)

    similar_movies = similar_movies.drop(movie_name)

    return similar_movies.head(num_recommendations).index.tolist()