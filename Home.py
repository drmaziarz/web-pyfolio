import pandas as pd
import streamlit as st


def get_datails():
    st.header(row["title"])
    st.write(row["description"])
    st.image(f"images/{row['image']}")
    st.markdown(f"[Source code]({row['url']})")


st.set_page_config(layout="wide",
                   page_title='PyFolio | Dorota Maziarz',
                   page_icon='🐍',
                   menu_items={
                       'Get Help': 'mailto:dr.maziarz@gmail.com',
                       'Report a bug': 'mailto:dr.maziarz@gmail.com',
                       'About': None
                   })

margin_l, col1, col2, margin_r = st.columns([0.5, 1.5, 1.5, 0.5])

with col1:
    with st.container():
        st.image("images/photo2.jpg")

with col2:
    st.title("Dorota Maziarz")
    content = """
    Welcome to my Pyfolio web!
    This web showcases some of my most notable projects, as well as provides basic information
    about me and my experience. If you have any questions or would like to discuss a potential cooperation, please
    don't hesitate to reach out to me. Below you can find some of the apps I have built in Python.
    """
    st.info(content)


col3, empty, col4 = st.columns([1.5, 0.3, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        get_datails()

with col4:
    for index, row in df[10:].iterrows():
        get_datails()
