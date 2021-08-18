import pandas as pd

class Marketing():
  def __init__(self, df) -> None:
      self.df = df.copy()

  
  def filter_necessary_columns(self):
    '''
    Make data frame to only contain necessary columns for marketing
    '''
    columns = ['MSISDN/Number', 'Handset Type', 'Handset Manufacturer']
    self.df = self.df[columns]

  
  def get_top_manufacturers(self, top=3):
    top_manufacturers = self.df.groupby("Handset Manufacturer").agg({"MSISDN/Number":'count'}).reset_index()
    top_manufacturers = top_manufacturers.sort_values(by='MSISDN/Number', ascending=False).head(top)
    return top_manufacturers

  
  def get_top_handsets(self, top=10):
    top_handset = self.df.groupby("Handset Type").agg({"MSISDN/Number":'count'}).reset_index()
    top_handset = top_handset.sort_values(by='MSISDN/Number', ascending=False).head(top)
    return top_handset


  def get_best_phones(self):
    top_3_manufacturers = self.get_top_manufacturers(3)

    manufacturers = self.df.groupby("Handset Manufacturer")

    for column in top_3_manufacturers['Handset Manufacturer']:
      result = manufacturers.get_group(column).groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(5)
      print(f"**** { column } ***")
      print(result)
      print()


  
  

