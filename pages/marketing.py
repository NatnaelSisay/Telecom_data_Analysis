import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import scripts.ploting as plot


st.set_option('deprecation.showPyplotGlobalUse', False)


def run_marketing():
  st.write("Marketing Analysis")

  file_name = 'data/clean_telco.csv'
  df_clean = pd.read_csv(file_name)
  
  top_10_handset = df_clean.groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(10)
  top_3_manufacturers = df_clean.groupby("Handset Manufacturer")['MSISDN/Number'].nunique().nlargest(3)


  fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(12,7))

  plot.serious_bar(top_3_manufacturers, ax1)
  plot.serious_bar(top_10_handset, ax2)
  plt.xticks(rotation=75)
  st.pyplot()

  st.write("## Analysis Insight")
  st.write("From The above two graphes, the Most sold phone rancking number 1 is Huawei B528S-23A \
    And The Number one Manufacturer is Apple. So, when we look at the handset next to Huawei most of them are \
      Products of Apple. ")
  st.write("## So this shows, The Marketing Team Need to focus on selling Apple Products")
