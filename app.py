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

selected_game_name = st.selectbox(
    'How would you like to be contacted ?',
    game['Name'].values)

if st.button('recommend'):
    try:
        recommedations = recommendation_system(selected_game_name, game)
        for game_name in recommendatons:
            st.write(game_name)
    except Exception as e:
        print(e)
        st.write('No recommendations')
