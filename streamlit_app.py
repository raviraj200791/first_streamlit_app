import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🥪 Avocado Toast')

streamlit.header('🍌🍓 Build Your Own Fruit Smoothie 🍇🥝')
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
# streamlit.dataframe(my_fruit_list)

# Let's put a pick listhere so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruites:", list(my_fruit_list))

# display the table on the page
streamlit.dataframe(my_fruit_list)
