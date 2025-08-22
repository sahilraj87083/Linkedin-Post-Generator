import streamlit as st
from few_shot import  FewShotPosts

length_options = ["Short" , "Medium", "Long"]
language_options = ["English" , "Hinglish"]


def main():
    st.title("LinkedIn Post Generator")
    col1 , col2, col3 = st.columns(3)
    fs = FewShotPosts()

    with col1:
        st.selectbox("Title", options = fs.get_tags())

    with col2:
        st.selectbox("Length" , options=length_options)

    with col3:
        st.selectbox("Language" , options=language_options)
if __name__ == "__main__":
    main()