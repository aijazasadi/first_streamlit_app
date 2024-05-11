import streamlit as st
from snowflake.snowpark.functions import col

st.title('Zena\'s Amazing Athleisure Catalog')

cnx = st.connection("snowflake")
session = cnx.session()

colors_dataframe = session.table("ZENAS_ATHLEISURE_DB.products.catalog_for_website").select(col('COLOR_OR_STYLE'))   
# colors_dataframe = session.sql("SELECT COLOR_OR_STYLE from ZENAS_ATHLEISURE_DB.products.catalog_for_website").collect()

option = st.selectbox(
   "Pick a sweatsuit color or style",
   colors_dataframe
)

st.write("You selected:", option)

            
