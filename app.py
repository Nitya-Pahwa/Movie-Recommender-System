import streamlit as st
import pickle
import pandas as pd
import string

movie_dict = pickle.load(open('movie.pkl', 'rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl', 'rb'))

def rec(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = similarity[index]
    recomm = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    movie_list=[]
    for i in recomm:
        movie_list.append(movies.iloc[i[0]].title)
    return movie_list


st.title("Movie Recommender System")

option = st.selectbox('Select a movie',movies['title'].values)

if(st.button('Recommend')):
    recommendations=rec(option)
    for i in recommendations:
        st.write(i)

