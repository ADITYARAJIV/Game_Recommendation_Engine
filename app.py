import pickle
import streamlit as st
import pandas as pd
from game_recommendation_engine import recommendation_system

game_dict = pickle.load(open('game_dict.pkl', 'rb'))
game = pd.DataFrame(movies_dict)
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