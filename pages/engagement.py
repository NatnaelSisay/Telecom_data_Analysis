import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

import scripts.ploting as plot

import scripts.utils as utils

st.set_option('deprecation.showPyplotGlobalUse', False)

def get_user_related_columns(df_clean):

  aggrigate = {
      'Total Social Media':'sum',
      'Total Google': 'sum', 
      'Total Youtube': 'sum', 
      'Total Netflix':'sum',
      'Total Gaming':'sum',
      'Total Other':'sum',
      'Total Email': 'sum',
      'Total':'sum'
  }
  user_app_usage = df_clean.copy()

  user_app_usage["Total Google"]    = user_app_usage["Google DL (Bytes)"] + user_app_usage["Google UL (Bytes)"]
  user_app_usage["Total Youtube"]   = user_app_usage["Youtube DL (Bytes)"] + user_app_usage["Youtube UL (Bytes)"]
  user_app_usage["Total Netflix"]   = user_app_usage["Netflix DL (Bytes)"] + user_app_usage["Netflix UL (Bytes)"]
  user_app_usage["Total Email"]     = user_app_usage["Email DL (Bytes)"] + user_app_usage["Email UL (Bytes)"]
  user_app_usage["Total Gaming"]    = user_app_usage["Gaming DL (Bytes)"] + user_app_usage["Gaming UL (Bytes)"]
  user_app_usage["Total Social Media"] = user_app_usage["Social Media DL (Bytes)"] + user_app_usage["Social Media UL (Bytes)"]
  user_app_usage["Total Other"]     = user_app_usage["Other DL (Bytes)"] + user_app_usage["Other UL (Bytes)"]
  user_app_usage['Total']           = user_app_usage['Total UL (Bytes)'] + user_app_usage['Total DL (Bytes)']

  # Remove Outliers
  columns = ['Total Google', 'Total Youtube', 'Total Netflix', 'Total Email', 'Total Gaming', 'Total Social Media', 'Total Other', 'Total']
  
  
    
  user_behaviour = user_app_usage.groupby('MSISDN/Number').agg(aggrigate)
  user_behaviour = utils.fix_outlier(user_behaviour, columns)
  return user_behaviour

def bivariant(user_behaviour):
  fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4,figsize=(15,8))
  # plot_scatter(user_behaviour.sample(1000), "Total", "Total Social Media", "Total Vs Social Media",ax1, "", "")

  def bivariant_sactter(df, x_col, y_col, ax):
    sns.scatterplot(data = df, x=x_col, y=y_col, ax=ax)

  sample_df = user_behaviour.sample(1000)
  # sns.scatterplot(data = sample_df)
  bivariant_sactter(sample_df, 'Total', 'Total Social Media', ax1)
  bivariant_sactter(sample_df, 'Total', 'Total Google', ax2)
  bivariant_sactter(sample_df, 'Total', 'Total Youtube', ax3)
  bivariant_sactter(sample_df, 'Total', 'Total Netflix', ax4)
  bivariant_sactter(sample_df, 'Total', 'Total Gaming', ax5)
  bivariant_sactter(sample_df, 'Total', 'Total Email', ax6)
  bivariant_sactter(sample_df, 'Total', 'Total Other', ax7)
  # bivariant_sactter(sample_df, 'Total', 'Total', ax8)
  st.pyplot()

def univriant(user_df):
  fig, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4,figsize=(15,8))

  # user_df = user_df.sample(1000)
  # sns.displot(data=user_df, x="Total Google", color="Green", ax=ax1)
  # sns.displot(data=user_df, x="Total Youtube", color="Green", ax=ax2)

  ax1.hist(user_df['Total Google'])
  ax1.set_title("Total Google")
  
  ax2.hist(user_df['Total Youtube'])
  ax2.set_title("Total Youtube")

  ax3.hist(user_df['Total Netflix'])
  ax3.set_title("Total Netflix")

  ax4.hist(user_df['Total Email'])
  ax4.set_title("Total Email")

  ax5.hist(user_df['Total Gaming'])
  ax5.set_title("Total Gaming")

  ax6.hist(user_df['Total Social Media'])
  ax6.set_title("Total Social Media")

  ax7.hist(user_df['Total Email'])
  # sns.displot(data=user_df, x='Total Email', color="green", kde=True, ax=ax7)
  ax7.set_title("Total Netflix")

  ax8.hist(user_df['Total Other'])
  ax8.set_title("Total Other")
  

def app_engagement(user_df):
  fix, ax = plt.subplots(1, 1, figsize=(12,7))
  engagement = user_df.copy()
  data = []
  # Social Media engagement
  columns = engagement.columns.tolist()[:-1]

  for column in columns:
      data.append(engagement[column].sum())

  data_df = pd.DataFrame({"Application": columns, "counts":data})
  data_df.sort_values(by='counts', ascending=False)[:3]
  sns.barplot(data = data_df, x='Application', y='counts', ax=ax)
  plt.show()

def run_engagement():
  file_name = 'data/clean_telco.csv'
  df_clean = pd.read_csv(file_name)


  st.write("## User Engagement Analysis")
  user_df = get_user_related_columns(df_clean)
  st.write(user_df.head())
  
  st.write("### Relation Ship Per applicaton")
  

  st.write("## Bivariant")
  bivariant(user_df)

  # st.write("## Univariant")
  # univriant(user_df)

  
  st.write("App per Engagement ")
  app_engagement(user_df)

  st.write("## From The graph we can see Users are Engaged on Gaming, Other ,Youtube and Netflix more than other applications")
  st.write("So The We should give more focus on Gaming Than other apps")
  st.pyplot()
