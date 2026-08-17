import streamlit as st
import pickle
import pandas as pd
import requests

API_KEY = st.secrets["TMDB_API_KEY"]
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"

def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"{BASE_URL}/movie/{movie_id}",
            params={
                "api_key": API_KEY,
                "language": "en-US"
            },
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")
        if poster_path:
            return IMAGE_BASE + poster_path

        return None

    except requests.exceptions.RequestException as e:
        print(f"TMDB error for movie {movie_id}: {e}")
        return None


def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
'What would you like to watch?',
movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    columns = st.columns(len(names))

    for col, name, poster in zip(columns, names, posters):
        with col:
            st.text(name)
            if poster:
                st.image(poster)
            else:
                st.image("https://via.placeholder.com/500x750?text=No+Poster")
