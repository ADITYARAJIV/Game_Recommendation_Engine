import pickle
import streamlit as st
import pandas as pd
from game_recommender_engine import recommendation_system

games_dict = pickle.load(open('games_dict.pkl', 'rb'))
game = pd.DataFrame(games_dict)
ft_vector = pickle.load(open('ft_vector.pkl', 'rb'))
ft_model = pickle.load(open('ft_model.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to be contacted ?',
    game['Name'].values)

if st.button('recommend'):
    recommendations = recommendation_system(game, ft_vector, ft_model)

for i in recommendations:
    st.write(i)
