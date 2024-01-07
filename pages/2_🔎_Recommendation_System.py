import streamlit as st

from RecommendationSystem1 import final_top_items
from RecommendationSystem2 import get_purchase_history, recommend_products
from RecommendationSystem3 import show_recommendations
from program import dataset, history

st.set_page_config(page_title="Home", page_icon="🏠")
st.markdown("# Recommendation System created for the e-commerce platform")

st.sidebar.markdown("# Try this: ")

st.sidebar.markdown("## *User ID:*")
st.sidebar.write("AE22E2AXODSPNK3EBIHNGYS5LOSA")
st.sidebar.write("AE2JTMRKTUOIVIZWS2WDGTMNTU4Q")
st.sidebar.write("AE27UOZENYSWCQVQRRUQIV2ZM7VA")

st.sidebar.markdown("## *Word:* ")
st.sidebar.write("cable")
st.sidebar.write("heater")
st.sidebar.write("camera")

# First RS
st.write("Recommendation System 1: Rating based", final_top_items)

# 2nd RS
st.write(" ")
st.write(" ")
st.write(" ")

st.write("Recommendation System 2: Purchase history based")
# Get user input for the user ID as string
user_id_input = st.text_input("Enter User ID:")
btn_enter = st.button("Enter")
st.write("Purchase history: ")
output21 = st.empty()
st.write("Products recommendation: ")
output22 = st.empty()

# Create a button to trigger functions
if btn_enter:
    if user_id_input:
        if user_id_input in history['user_id'].unique():
            user_history = get_purchase_history(dataset, history, user_id_input)
            recommendations = recommend_products(dataset, history, user_id_input)

            # Update 21 output
            with output21:
                st.subheader("Purchase History")
                st.write(user_history)

            # Update 22 output
            with output22:
                st.subheader("Product Recommendations")
                st.write(recommendations)

        else:
            st.warning("User does not exist")
    else:
        st.warning("Please enter a User ID")

# 3rd RS
st.write(" ")
st.write(" ")
st.write(" ")

st.write("Recommendation System 3: Search based")

# Get user input
word = st.text_input("Enter a word:")
btn_search = st.button("Search")
st.write("Products recommendation: ")
output31 = st.empty()

# Create a button to trigger recommendations
if btn_search:
    if not word:
        st.warning("Please enter a word")
    else:
        recommendations = show_recommendations(word)  # Get recommendations based on the word
        # Update 31 output
        with output31:
            # Show recommendations as a table
            st.write(recommendations)
