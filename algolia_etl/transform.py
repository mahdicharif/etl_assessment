import pandas as pd

def transform(df):
    """
    This function transforms the raw data by filtering out unwanted rows

    input:
        df: a dataframe
    
    output:
        df: the transformed df
    """
    # Filter out rows with empty application_id
    df = df[df['application_id'].notna()]
    
    # Add has_specific_prefix column
    df['has_specific_prefix'] = df['index_prefix'].apply(lambda x: x != 'shopify_')
    
    return df