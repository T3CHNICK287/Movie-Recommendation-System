import streamlit as st
import pickle
import pandas as pd
import difflib
import requests
import numpy as np

file=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(file)

similarity=pickle.load(open('similarity.pkl','rb'))

# Setting Layout
st.set_page_config(layout="wide")

st.title('Movie Recommender System')

input_movie_name=st.selectbox("Search Movies",sorted(movies['title'].values), placeholder='Search Movie')


all_titles = movies['title'].tolist()

def get_poster(movie_id):
  response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=36c5dab4ef4c5b43ad4dffdb6061df74&language=en-US'.format(movie_id))
  
  # Check if the response status code is OK (200)
  if response.status_code == 200:
    data=response.json()
    
    # Check if the 'poster_path' key exists in the response data and if it's not empty
    if 'poster_path' in data and data['poster_path']:
      path=data['poster_path']
      return "https://image.tmdb.org/t/p/w500/"+path
    else:
      # Return a default image URL if 'poster_path' is missing or empty
      return "https://www.prokerala.com/movies/assets/img/no-poster-available.jpg"
  else:
    # Handle the case where the request to the API fails
    return "https://www.prokerala.com/movies/assets/img/no-poster-available.jpg"  



# Same functions from main file
def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distances=similarity[movie_index]
  movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:16]
  recommended_movies=[]
  recommended_movies_posters=[]


  for i in movies_list:
    recommended_movies.append(movies.iloc[i[0]].title)
    #fetch movie poster
    recommended_movies_posters.append(get_poster(movies.iloc[i[0]].movie_id))
  return recommended_movies,recommended_movies_posters

# Showing results
if st.button('Recommend'):
  names,posters=recommend(input_movie_name)

  st.header('Your Movie')
  # Find the movie ID for the selected movie title
  selected_movie_id = movies[movies['title'] == input_movie_name]['movie_id'].values[0]

  # Get the poster using the movie ID
  main_poster = get_poster(selected_movie_id)

  col1,col01,col02,col03,col04 = st.columns(5)  # Use st.columns without 'with' as it's not a context manager
  with col1:
    st.subheader(input_movie_name)
    st.image(main_poster)

  st.header('Similar Movies')

  col2, col3, col4, col5, col6 = st.columns(5)

  with col2:
    st.subheader(names[0])
    st.image(posters[0])

  with col3:
    st.subheader(names[1])
    st.image(posters[1])

  with col4:
    st.subheader(names[2])
    st.image(posters[2])

  with col5:
    st.subheader(names[3])
    st.image(posters[3])

  with col6:
    st.subheader(names[4])
    st.image(posters[4])

  col7, col8, col9, col10, col11 = st.columns(5)
  with col7:
    st.subheader(names[5])
    st.image(posters[5])

  with col8:
    st.subheader(names[6])
    st.image(posters[6])

  with col9:
    st.subheader(names[7])
    st.image(posters[7])

  with col10:
    st.subheader(names[8])
    st.image(posters[8])

  with col11:
    st.subheader(names[9])
    st.image(posters[9])

  col12, col13, col14, col15, col16 = st.columns(5)
  with col12:
    st.subheader(names[10])
    st.image(posters[10])

  with col13:
    st.subheader(names[11])
    st.image(posters[11])

  with col14:
    st.subheader(names[12])
    st.image(posters[12])

  with col15:
    st.subheader(names[13])
    st.image(posters[13])

  with col16:
    st.subheader(names[14])
    st.image(posters[14])

