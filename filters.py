import streamlit as st

def get_category_filters(df):
    st.sidebar.header("Filter by Category")
    
    categories = ["All Categories"] + list(df['Major_category'].unique())
    selected_category = st.sidebar.selectbox(
        "Choose a Major Category to explore:", 
        options=categories
    )
    
    return selected_category
