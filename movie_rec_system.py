import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
moviess = pd.DataFrame(movies_dict)

# Set page title and header
st.title('Movie Recommendation System')
st.markdown("---")

# Selectbox to choose a movie
selectbox = st.selectbox('Please select a movie', moviess['title'].values)
st.markdown("---")

# Function to recommend movies based on selected movie
def recommend(movie):
    movie_index = moviess[moviess['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(moviess.iloc[i[0]]['title'])
    return recommended_movies

# Button to trigger recommendation
if st.button('Recommend'):
    recommendations = recommend(selectbox)
    st.subheader("Recommended Movies:")
    for movie_title in recommendations:
        # Generate clickable link to Google search with customized styling
        google_search_url = f"https://www.google.com/search?q={movie_title.replace(' ', '+')}+'movie"
        st.markdown(f'<a href="{google_search_url}" target="_blank" style="text-decoration: none; color: #FFF; font-size: 16px;">{movie_title}</a>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Developed by Thebug Developer")
