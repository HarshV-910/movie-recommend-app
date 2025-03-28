import streamlit as st
import pickle
import pandas as pd
import requests

# function for fetching recommended movies
def recommend(movie): # movie is title of given movie
  movie_index = final[final['title'] == movie].index[0] # finding index of given movie to access similarity list of its
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

  r_movies = []
  r_movies_poster = []
  for i in movies_list:
    # fetching title of recommended movies
    r_movies.append(final.iloc[i[0]].title)
    # fetching id of recommended movies
    r_movies_id = final.iloc[i[0]].movie_id
    # fetching posters from API using movie id
    r_movies_poster.append(poster(r_movies_id))
  return r_movies,r_movies_poster

# function for fetching posters of recommended movies
def poster(id):
   response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# load pkl files
similarity = pickle.load(open("similarity.pkl",'rb'))
all_movies_dict = pickle.load(open("movies_dict.pkl",'rb'))
final = pd.DataFrame(all_movies_dict)

# title
st.title("Movie Recommendation App")

# selection box
selected_movie = st.selectbox("search movie",final['title'].values)

# button
if st.button("Recommend"):
    names,posters = recommend(selected_movie)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
       st.text(names[0])
       st.image(posters[0])
    with col2:
       st.text(names[1])
       st.image(posters[1])
    with col3:
       st.text(names[2])
       st.image(posters[2])
    with col4:
       st.text(names[3])
       st.image(posters[3])
    with col5:
       st.text(names[4])
       st.image(posters[4])

    # col[5] = st.columns(5)
    # for i in range(5):
    #    with col[i]:
    #       st.text(names[i])
    #       st.image(posters[i])

    
