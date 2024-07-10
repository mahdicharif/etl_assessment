import boto3
import pandas as pd

def extract(date):
    """
    This function extracts the raw data

    input:
        date: a given date corresponding to the name of the targeted file.
    
    output:
        output_df : the extracted data, loading into a pandas dataframe
    """
    s3 = boto3.client('s3')
    bucket_name = 'alg-data-public'
    file_name = f'{date.strftime("%Y-%m-%d")}.csv'
    
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    output_df = pd.read_csv(obj['Body'])
    return output_df