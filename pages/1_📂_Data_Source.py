import streamlit as st

from program import datasetbefore, dataset, history

# Dataset overview
st.markdown("# Dataset used for the program")
st.sidebar.markdown("# Dataset source: ")
st.sidebar.write("**Platform:** Kaggle")
st.sidebar.write("**Title:** Amazon Sales Dataset")
st.sidebar.write("**Author:** KARKAVELRAJA J")
st.sidebar.write("**Source:** Amazon official website")
st.sidebar.write("**Url:** https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset")
st.sidebar.write("**About:** This dataset is having the data of 1K+ Amazon Product's Ratings and Reviews as per their "
                 "details listed on the official website of Amazon")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write("**Features:**")
st.sidebar.write("product_id - Product ID")
st.sidebar.write("product_name - Name of the Product")
st.sidebar.write("category - Category of the Product")
st.sidebar.write("discounted_price - Discounted Price of the Product")
st.sidebar.write("actual_price - Actual Price of the Product")
st.sidebar.write("discount_percentage - Percentage of Discount for the Product")
st.sidebar.write("rating - Rating of the Product")
st.sidebar.write("rating_count - Number of people who voted for the Amazon rating")
st.sidebar.write("about_product - Description about the Product")
st.sidebar.write("user_id - ID of the user who wrote review for the Product")
st.sidebar.write("user_name - Name of the user who wrote review for the Product")
st.sidebar.write("review_id - ID of the user review")
st.sidebar.write("review_title - Short review")
st.sidebar.write("review_content - Long review")
st.sidebar.write("img_link - Image Link of the Product")
st.sidebar.write("product_link - Official Website Link of the Product")

st.write("Original dataset: ", datasetbefore)
st.write("Dataset after cleaning and formatting: ", dataset)
st.write("User purchase history extraction: ", history)
