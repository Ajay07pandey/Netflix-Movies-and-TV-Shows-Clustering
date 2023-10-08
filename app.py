import streamlit as st
import pickle
import pandas as pd


movies_list = pickle.load(open("content_dict.pkl",'br'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('cosine_similarity.pkl','rb'))

def recommend(title, cosine_sim=similarity, data=movies):
    recommended_content=[]
    # Get the index of the input title in the programme_list
    programme_list = data['title'].to_list()
    index = programme_list.index(title)

    # Create a list of tuples containing the similarity score and index 
    # between the input title and all other programs in the dataset
    sim_scores = list(enumerate(cosine_sim[index]))

    # Sort the list of tuples by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]

    # Get the recommended movie titles and their similarity scores
    recommend_index = [i[0] for i in sim_scores]
    rec_movie = data['title'].iloc[recommend_index]
    rec_score = [round(i[1], 4) for i in sim_scores]

    # Create a pandas data frame to display the recommendations
    rec_table = pd.DataFrame(list(zip(rec_movie, rec_score)), columns=['Recommendation', 'Similarity_score(0-1)'])
    # recommended_content.append(rec_table['Recommendation'].values)

    return rec_table['Recommendation'].values

# Displaying title
st.header('Movie Recommender System')



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
