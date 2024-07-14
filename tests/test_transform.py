import unittest
import pandas as pd
from algolia_etl.transform import transform

class TestTransform(unittest.TestCase):

    def test_transform(self):
        # Test data
        input_data = {
            'id': [1, 2, 3, 4],
            'application_id': ['app1', 'app2', None, 'app4'],
            'index_prefix': ['shopify_', 'custom_', 'shopify_', 'another_']
        }
        input_df = pd.DataFrame(input_data)

        # Call the function
        result_df = transform(input_df)

        # Assertions
        self.assertEqual(len(result_df), 3)  # Removed row with None application_id
        self.assertIn('has_specific_prefix', result_df.columns)
        self.assertEqual(result_df['has_specific_prefix'].tolist(), [False, True, True])

    def test_transform_empty_df(self):
        # Test with empty dataframe
        empty_df = pd.DataFrame(columns=['id', 'application_id', 'index_prefix'])
        result_df = transform(empty_df)
        self.assertTrue(result_df.empty)
        self.assertIn('has_specific_prefix', result_df.columns)

if __name__ == '__main__':
    unittest.main()