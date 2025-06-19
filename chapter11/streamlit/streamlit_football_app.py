import streamlit as st
import logging
import pandas as pd

if 'base_url' not in st.session_state:
    st.session_state['base_url'] = 'https://curly-adventure-4x7vx4r44xq2j79p-8000.app.github.dev/'

logging.basicConfig(filename='football_app.log',
                    level=logging.INFO)

st.set_page_config(page_title='Football App',  page_icon=":material/thumb_up:")

page_1 = st.Page("page1.py", title="Team Rosters", icon=":material/trophy:")
page_2 = st.Page("page2.py", title="Team Stats", icon=":material/star_border:")

pg = st.navigation([page_1, page_2])
pg.run()
