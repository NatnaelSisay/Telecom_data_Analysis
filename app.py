import numpy as np
import pandas as pd
import streamlit as st

# pages
import pages.intro as intro
import pages.marketing as marketing
import pages.engagement as enngagement
import pages.experiance as experiance
import pages.satisfaction as satisfaction

st.set_page_config(page_title="Day 5", layout="wide")
st.title("TelCo Data analysis")
st.sidebar.markdown("# Side Bar")


page = st.sidebar.selectbox('Choose Page', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'])

if(page == 'Intro'):
  intro.run()
elif(page == 'Marketing'):
  marketing.run_marketing()
elif(page == 'Engagement'):
  enngagement.run_engagement()
elif(page == 'Experiance'):
  experiance.run_experiance()
elif(page == 'Satisfaction'):
  satisfaction.run_satisfaction()
else:
  intro.run()
