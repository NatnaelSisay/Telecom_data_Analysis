 
import pandas as pd

from scripts import utils

def run_cleaning():

    print("Data Cleaning ....")

    file_name = 'data/Week1_challenge_data_source.csv'

    df = pd.read_csv(file_name, na_values=['?','Na','NaN', 'undefined', None])

    df_initial_shape = f'Data Frame Contains {df.shape[0]} rows and {df.shape[1]} columns'
    null_percentage_in_df = utils.null_percentage(df)

    # Clean up Began
    df.dropna(subset=['Bearer Id', 'MSISDN/Number'], inplace=True)

    # drop columns with more than 30% null Values
    df_clean = utils.drop_column_with_many_null(df)

    columns_object_type = ['Start', 'End', 'Last Location Name', 'Handset Manufacturer', 'Handset Type']

    for column in columns_object_type:
        mode = df_clean[column].mode()[0]
        df_clean[column] = df_clean[column].fillna(mode)

    ## i could get away by filling them all with Median
    # they should be filled with median, but lots of columns to fill
    for column in df_clean.columns:
        # if column have null value fill 
        if(df[column].isnull().sum() > 0):
            mode = df_clean[column].mode()[0]
            df_clean[column] = df_clean[column].fillna(mode)

    null_percentage_after_clean = utils.null_percentage(df_clean)

    ### save the cleaned data
    for_save_df = df_clean.set_index('Bearer Id')
    for_save_df.to_csv('data/clean_telco.csv')
    print("Data Frame cleand an Saved!")
    return (df_initial_shape,  null_percentage_in_df, null_percentage_after_clean)
        