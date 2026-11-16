
import streamlit as st

# Set page title
st.set_page_config(page_title="My First Streamlit App")

# App title
st.title("My First Streamlit App")

# Description
st.write("Welcome! Enter your text below.")

# Text input
user_text = st.text_input("Enter your text:")

# Display entered text
if user_text:
    st.success("You entered:")
    st.write(user_text)
else:
    st.info("Please enter some text.")
