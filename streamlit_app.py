import streamlit
streamlit.title('My Parents new healthy diner')
streamlit.header('BREAKFAST favourites')
streamlit.text('🥣 omega 3 and oatmeal')
streamlit.text('🥗 kale,spinach and smoothie')
streamlit.text('🥑 avacado')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
