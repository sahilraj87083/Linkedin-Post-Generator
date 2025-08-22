import streamlit as st
from few_shot import  FewShotPosts


def main():
    st.title("LinkedIn Post Generator")
    col1 , col2, col3 = st.columns(3)

    with col1:
        st.selectbox("Title", options=[])
if __name__ == "__main__":
    main()