import pickle
import streamlit as st
import pandas as pd
from game_recommender_engine import recommendation_system

games_dict = pickle.load(open('games_dict.pkl', 'rb'))
game = pd.DataFrame(games_dict)
ft_vector = pickle.load(open('ft_vector.pkl', 'rb'))
ft_model = pickle.load(open('ft_model.pkl', 'rb'))
recommendations = []
st.title("Game Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to be contacted ?',
    game['Name'].values)

if st.button('recommend'):
    recommendations = recommendation_system(game, ft_vector, ft_model)
    if len(recommendations) != 0:
        for game_name in recommendations:
            st.write(game_name)
    else:
        st.write("No games recommended")
