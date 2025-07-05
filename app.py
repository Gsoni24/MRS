import streamlit as st
import pickle
import requests


page_bg_img = f"""
<style>

.st-emotion-cache-1yiq2ps {{
background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)),url("https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg");    
background-size: cover;
}}


</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)




url = "https://api.themoviedb.org/3/movie/{}?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1YTI5NTk3ODljZjY5YmI1YTMxMjM2ZmVhNGNkNWU5ZiIsIm5iZiI6MTc0NDcwNjE0Ny45NjQsInN1YiI6IjY3ZmUxYTYzMzAxNTM2MzI4NmQ5N2RhOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hE5Q56VOrtbNTjruHhzGQNHTTPmO5jQfevEPjzp1A7A"
}


def fetch_poster(movie_id):
    response = requests.get(url.format(movie_id),headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies_list1[movies_list1['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies_list1.iloc[i[0]].id

        recommended_movies.append(movies_list1.iloc[i[0]].title)
        #fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters


movies_list1 = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list1['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('',movies_list)

if st.button("Recommend",type='primary'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5  = st.columns(5,vertical_alignment='top')

    with col1:
        st.image(posters[0])
        st.text(names[0])

    with col2:
        st.image(posters[1])
        st.text(names[1])

    with col3:
        st.image(posters[3])
        st.text(names[2])

    with col4:
        st.image(posters[3])
        st.text(names[3])

    with col5:
        st.image(posters[4])
        st.text(names[4])