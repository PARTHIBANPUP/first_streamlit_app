import streamlit
streamlit.title('My Parents new healthy diner')
streamlit.header('BREAKFAST favourites')
streamlit.text('🥣 omega 3 and oatmeal')
streamlit.text('🥗 kale,spinach and smoothie')
streamlit.text('🥑 avacado')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
  streamlit.error("Please select a fruit to get information.")
  else
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  STREAMLIT.ERROR()
streamlit.stop()
#import snowflake.connector
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit load list contains:")
streamlit.dataframe(my_data_rows)
streamlit.write('Thanks for adding', add_my_fruit)
DEF INSERT_ROW_SNOWFLAKE(new_fruit):
  with my_cnx.cursor()as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+ jackfruit +"')")
    return "thanks for adding" + new_fruit
  add_my_fruit = fruit_choice = streamlit.text_input('What fruit would you like to add?')
  if streamlit.button('add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = INSERT_ROW_SNOWFLAKE(new_fruit)
    streamlit.text(back_from_function)
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLERROR
  if streamlit.button('get fruit list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
 
