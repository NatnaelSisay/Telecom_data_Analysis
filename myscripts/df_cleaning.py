import pandas as pd
import numpy as np

class DataFrameCleaning():
  def __init__(self, df):
    self.df = df.copy()


  def get_column_with_many_null(self):
    '''
    Return List of Columns which contain more than 30% of null values
    '''
    df_size = self.df.shape[0]
    
    columns_list = self.df.columns
    bad_columns = []
    
    for column in columns_list:
        null_per_column = self.df[column].isnull().sum()
        percentage = round( (null_per_column / df_size) * 100 , 2)
        
        if(percentage > 30):
            bad_columns.append(column)
    
    return bad_columns

  
  def drop_columns(self, columns):
    '''
    Return Dataframe with Most null columns removed.
    '''

    self.df.drop(columns, axis=1, inplace=True)


  def drop_column(self, column):
    '''
    Drop un-wanted columns
    '''
    self.drop_columns(column)


  def drop_rows(self, columns):
    '''
    Drop Rows of specified columns, which contain null values
    apply it on columns with small number of nulls
    '''
    self.df.dropna(subset=columns, inplace=True)


  def convert_datetime(self, columns):
    '''
    Convert columns to date time.
    '''

    for column in columns:
      self.df[column] = pd.to_datetime(self.df[column])
    
    return self.df


  def convert_to(self, columns, data_type):
    '''
    Convert Columns to desired data types.
    '''

    for column in columns:
      self.df[column] = self.df[column].astype(data_type)
    
    return self.df


  def fill_catagorical_column(self, column):
    '''
    Return DataFrame
    Fill Null Value of catagorical columns with Mode
    '''

    mode = self.df[column].mode()[0]
    self.df[column] = self.df[column].fillna(mode)


  def fill_catagorical_columns(self, columns):
    '''
    Fill Null values of multiple columns with Mode.
    '''
    for column in columns:
      self.fill_catagorical_column(column)
  

  def fill_numerical_column(self, column):
    '''
    Reuturn DataFrame with Numerical null values filled with 
    mean or median depending on the skewness of the column
    '''

    skewness = self.df[column].skew()
    if((-1 < skewness) and (skewness < -0.5)):
      # Negative skew
      self.df[column].fillna(self.df[column].mean())

    elif((0.5 < skewness) and (skewness < 1)):
      # Positive skew
      self.df[column].fillna(self.df[column].median())

    else:
      # highly skewed 
      self.df[column].fillna(self.df[column].median())


  def fill_numerical_columns(self, columns):
    '''
    Fill Numerical multiple numerical columns with median and mode
    depending on their skewness.
    '''
    for column in columns:
      self.fill_numerical_column(column)


  def fix_outliers(self, col):
    '''
    Handle outliers of specified column
    '''
    q1 = self.df[col].quantile(0.25)
    q3 = self.df[col].quantile(0.75)

    lower_bound = q1 - ((1.5) * (q3 - q1))
    upper_bound = q3 + ((1.5) * (q3 - q1))

    self.df[col] = np.where(self.df[col] < lower_bound, lower_bound, self.df[col])
    self.df[col] = np.where(self.df[col] > upper_bound, upper_bound, self.df[col])


  def save_clean(self):
    try:
      self.df.to_csv('../data/clean_telecom_data.csv', index=False)
    except:
      print('Log: Error while Saving File')
  