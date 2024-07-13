import boto3
import pandas as pd


def extract(date):
    """
    This function extracts the raw data

    args:
        date (date): a given date corresponding to the name of the targeted file.

    output:
        extracted_df (dataframe) : the extracted data, loaded into a pandas dataframe
    """
    s3 = boto3.client("s3")
    bucket_name = "alg-data-public"
    file_name = f'{date.strftime("%Y-%m-%d")}.csv'

    obj = s3.get_object(Bucket=bucket_name, Key=file_name)
    extracted_df = pd.read_csv(obj["Body"])
    extracted_df["file_date"] = date
    return extracted_df
