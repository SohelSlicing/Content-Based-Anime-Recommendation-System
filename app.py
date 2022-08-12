import streamlit as st
import pickle
import requests

def get_image(anime_id):
     response = requests.get('https://api.myanimelist.net/v0/anime/{}'.format(anime_id))
     data = response.json()
     return data['main_picture']['medium']


def recommend(anime):
     anime_index = animes[animes['Name'] == anime].index[0]
     distances = anismililarity[anime_index]
     recomend_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_anime = []
     recommended_anime_image = []
     for i in recomend_list:
          ani_id = animes.iloc[i[0]].MAL_ID
          recommended_anime.append(animes.iloc[i[0]].Name)
          # fetching image from API
          recommended_anime_image.append(get_image(ani_id))
     return recommended_anime, recommended_anime_image



animes = pickle.load(open('animes.pkl', 'rb'))
anime_list = animes['Name'].values

anismililarity = pickle.load(open('anisimilarity.pkl', 'rb'))

st.title('Anime Recommender System')

selected_anime = st.selectbox(
     'Select an anime which you liked',
     anime_list)

if st.button('Recommend'):
     names, posters = recommend(selected_anime)
     col1, col2, col3, col4, col5 = st.columns(5)

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