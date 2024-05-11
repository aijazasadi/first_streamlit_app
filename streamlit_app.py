import streamlit as st
from snowflake.snowpark.functions import col

st.title('Zena\'s Amazing Athleisure Catalog')

cnx = st.connection("snowflake")
session = cnx.session()

# colors_dataframe = session.table("ZENAS_ATHLEISURE_DB.products.catalog_for_website").select(col('COLOR_OR_STYLE'))   
colors_dataframe = session.sql("SELECT COLOR_OR_STYLE from ZENAS_ATHLEISURE_DB.products.catalog_for_website").collect()

selected_color = st.selectbox(
   "Pick a sweatsuit color or style",
   colors_dataframe
)

catalog_dataframe = session.sql("SELECT * from ZENAS_ATHLEISURE_DB.products.catalog_for_website where color_or_Style='"+selected_color+"'").collect()
selected_item = catalog_dataframe[0]

st.image(selected_item["DIRECT_URL"], use_column_width  = "auto", caption="Our warm, comfortable, " + selected_color + " sweatsuit!")
st.metric(label="Price", value=str(selected_item["PRICE"]))
# st.write("**Price:** " + str(selected_item["PRICE"]))
st.write("**Sizes Available:** " + selected_item["SIZE_LIST"])
st.write(selected_item["UPSELL_PRODUCT_DESC"])


            
