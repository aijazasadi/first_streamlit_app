import streamlit as st
from snowflake.snowpark.functions import col

st.title('Zena\'s Amazing Athleisure Catalog')

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("CATALOG_FOR_WEBSITE").select(col('COLOR_OR_STYLE'))     

option = st.selectbox(
   "Pick a sweatsuit color or style",
   my_dataframe
)

st.write("You selected:", option)

            
