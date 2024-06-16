import streamlit as st
import pickle
import requests
from PIL import Image
import os

# Load movies and similarity matrices
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarilty.pkl", 'rb'))

# Extract movie titles
movies_list = movies['title'].values

# Directory containing local poster images for testing
POSTER_DIR = "posters/"  # Make sure to replace this with the actual directory path

# Function to fetch movie poster from local directory (for testing)
def fetch_poster_local(movie_id):
    poster_path = os.path.join(POSTER_DIR, f"{movie_id}.jpg")
    if os.path.exists(poster_path):
        return poster_path
    else:
        return "https://via.placeholder.com/500"  # Fallback image if local poster is not found

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster_local(movie_id))
    return recommended_movies, recommended_posters

# Streamlit layout and styling
st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# CSS for custom styling
st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
            color: #f0f0f0;
        }
        .main {
            background-color: #0f0f0f;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput>div>input {
            border-radius: 8px;
            padding: 10px;
        }
        .sidebar .sidebar-content {
            background-color: #1c1c1c;
            padding: 20px;
            border-radius: 10px;
        }
        .st-markdown h1, h2, h3, h4, h5, h6 {
            color: #4CAF50;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.header("Movie Recommendation System")
st.sidebar.write("Select your favorite movie from the dropdown to get recommendations.")
selectvalue = st.sidebar.selectbox("Select movie from dropdown", movies_list)

# Main content
st.title("Movie Recommendation System")
st.markdown("### Find your next favorite movie!")
st.write("Select a movie from the sidebar to get recommendations.")

# Show recommendations on button click
if st.button("Show Recommended Movies"):
    movie_names, movie_posters = recommend(selectvalue)
    st.subheader(f"Recommendations for '{selectvalue}':")
    cols = st.columns(5)
    for col, name, poster in zip(cols, movie_names, movie_posters):
        with col:
            st.markdown(f"**{name}**")
            st.image(poster)

# Add a footer
st.markdown("***")
st.markdown("**Developed by Saniya Ahemad :)**")
st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://github.com/saniyaahemad12) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/saniya-ahemad-65560a252/)")
