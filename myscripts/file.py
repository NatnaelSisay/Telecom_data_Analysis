import pandas as pd
def read_csv(file_name):
  try:
    null_values = ["n/a", "na", "undefined"]
    df = pd.read_csv(f'../data/{file_name}', na_values=null_values)
    return df
  except:
    print("Log:-> File Not Found")

def save_file(file_name):
  pass