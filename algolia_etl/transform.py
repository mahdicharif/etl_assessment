def transform(df):
    """
    This function transforms the raw data by filtering out unwanted rows

    input:
        df (dataframe): the extracted dataframe

    output:
        transformed_df (dataframe): the transformed dataframe
    """
    # Filter out rows with empty application_id
    transformed_df = df[df["application_id"].notna()]

    # Add has_specific_prefix column
    transformed_df["has_specific_prefix"] = transformed_df["index_prefix"].apply(
        lambda x: x != "shopify_"
    )
    return transformed_df
