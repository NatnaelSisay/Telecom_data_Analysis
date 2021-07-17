import pandas as pd


def null_percentage(df):
    number_of_rows, number_of_columns = df.shape
    df_size = number_of_rows * number_of_columns
    
    null_size = (df.isnull().sum()).sum()
    percentage = round((null_size / df_size) * 100, 2)
    return f"Data Fraame contain null values of { percentage }%"

def drop_column_with_many_null(df):
    df_size = df.shape[0]
    
    columns_list = df.columns
    bad_columns = []
    
    for column in columns_list:
        null_per_column = df[column].isnull().sum()
        percentage = round( (null_per_column / df_size) * 100 , 2)
        
        if(percentage > 30):
            bad_columns.append(column)
    bad_columns.append('Dur. (ms).1')
    df = df.drop(bad_columns, axis=1)
    return df