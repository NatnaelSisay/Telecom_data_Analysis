import pandas as pd

class DataFrameInfo():
  def __init__(self, df):
    self.df = df.copy()


  def info(self):
    '''
    Display number of rows and columns in the Data frame
    '''

    print(f"Data Frame contain {self.df.shape[0]} rows and {self.df.shape[1]} columns")


  def detail_info(self):
    '''
    Display detail Dataframe info
    '''

    print(self.df.info())


  def skewness(self):
    '''
    Display The skew value of each column.

    skewness b/n -0.5 - 0.5 : good
    skewness b/n -1 - -0.5  : negative skew
    skewness b/n 0.5 - 1    : positive skew
    other values: are highly skewed
    '''
    print(self.df.skew())


  def describe(self):
    '''
    Display Numerical Description of the Dataframe
    '''
    print(self.df.describe())  


  def null_percentage(self):
    '''
    Display Total Null percentage of the Data Frame
    '''

    number_of_rows, number_of_columns = self.df.shape
    df_size = number_of_rows * number_of_columns
    
    null_size = (self.df.isnull().sum()).sum()
    percentage = round((null_size / df_size) * 100, 2)
    print(f"Data Frame contain null values of { percentage }%")


  def get_columns_list(self):
    '''
    Return Column list of the Dataframe
    '''
    return self.df.columns.to_list()


  def get_null_counts(self):
    '''
    Display Null Counts of each column
    '''

    print(self.df.isnull().sum())



