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
    try:
        for game_name in recommendation_system(game, ft_vector, ft_model):
            print(game_name)
    except Exception as e:
        print(e)
