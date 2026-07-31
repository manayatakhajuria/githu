from typing import Any

import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie=[]
    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie


similarity=pickle.load(open('similarity.pkl','rb'))
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('MOVIE RECOMMENDER SYSTEM')
selected_movie_name=st.selectbox('select a movie?',
                    movies['title'].values )
if st.button('recommend'):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
    st.write(selected_movie_name)


