import streamlit as st
import pickle
import pandas as pd
import scipy

movies_list = pickle.load(open("content_dict.pkl",'br'))
movies = pd.DataFrame(movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

# Displaying title
st.header('Movie Recommender System')

similarity = pickle.load(open('cosine_similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Setting a button
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for j in recommended_movie_names:
        st.write(j)