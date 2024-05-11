import streamlit as st

st.title('Zena\'s Amazing Athleisure Catalog')

option = st.selectbox(
   "Pick a sweatsuit color or style",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)

st.write("You selected:", option)

