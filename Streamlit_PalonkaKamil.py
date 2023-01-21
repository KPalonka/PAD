import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def main_page():
    st.title("First Streamlit")
    st.header('Palonka Kamil')
    st.markdown('## Select appropriate page on the sidebar :)')
def page2():
    st.title('Ankieta')
    firstname = st.text_input("Please, enter your first name", "First name")
    lastname = st.text_input("Please, enter your second name", "Last name")
    if st.button("Submit"):
        st.success('Survey saved successfully!')

def page3():
    st.title('Staty')
    # uploading data
    import time
    data = st.file_uploader("Upload your dataset", type=['csv'])
    my_bar = st.progress(0)
    
    if data is not None:
        with st.spinner("Waiting..."):
            time.sleep(1)
            st.success("Finished!")
        df = pd.read_csv(data)
        st.dataframe(df.head(15))
    
        columns = df.columns
        columns2 = df.columns
        col1 = st.columns(2)
        choice1 = st.selectbox('Select axis X:', columns)
        choice2 = st.selectbox('Select axis Y:', columns2)

        fig = px.scatter(df,x = choice1, y = choice2 ,title = "Custom chart")
        st.plotly_chart(fig)

page_names_to_funcs = {
    'General':main_page,
    'Ankieta': page2,
    'Staty': page3
}

selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()



