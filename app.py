import numpy as np
import pandas as pd
import streamlit as st

# pages
import pages.intro as intro


st.set_page_config(page_title="Day 5", layout="wide")
st.title("TelCo Data analysis")
st.sidebar.markdown("# Side Bar")


page = st.sidebar.selectbox('Choose Page', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'])

if(page == 'Intro'):
  intro.run()
elif(page == 'Marketing'):
  pass
elif(page == 'Engagement'):
  pass
elif(page == 'Experiance'):
  pass
elif(page == 'Satisfaction'):
  pass
else:
  intro.run()
