import unittest
from unittest.mock import patch, MagicMock
from datetime import date
import pandas as pd
from io import BytesIO

from algolia_etl.extract import extract

class TestExtract(unittest.TestCase):

    @patch('boto3.client')
    def test_extract(self, mock_boto3_client):
        # Mock S3 client and object
        mock_s3 = MagicMock()
        mock_boto3_client.return_value = mock_s3
        
        # Create a BytesIO object to simulate file content
        csv_content = b"id,application_id,index_prefix\n1,app1,shopify_\n2,app2,custom_"
        mock_body = BytesIO(csv_content)
        
        # Mock S3 object
        mock_obj = {
            'Body': mock_body
        }
        mock_s3.get_object.return_value = mock_obj

        # Test data
        test_date = date(2024, 1, 1)
        
        # Call the function
        result_df = extract(test_date)

        # Assertions
        mock_s3.get_object.assert_called_once_with(
            Bucket="alg-data-public",
            Key="2024-01-01.csv"
        )
        
        self.assertIsInstance(result_df, pd.DataFrame)
        self.assertEqual(len(result_df), 2)
        self.assertIn('file_date', result_df.columns)
        self.assertTrue((result_df['file_date'] == test_date).all())

if __name__ == '__main__':
    unittest.main()