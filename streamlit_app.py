import streamlit
streamlit.title('My Parents new healthy diner')
streamlit.header('BREAKFAST favourites')
streamlit.text('🥣 omega 3 and oatmeal')
streamlit.text('🥗 kale,spinach and smoothie')
streamlit.text('🥑 avacado')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
streamlit.write('The user entered ', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "Apple")

#json response and normalization 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()
import snowflake.connector
add_my_fruit = fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
my_cur.execute("insert into fruit_load_list values ('from streamlit')")


import streamlit
import pandas
import requests
import.snowflake.connector

from urllib.error import URLERROR
