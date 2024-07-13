import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from algolia_etl.load import load

class TestLoad(unittest.TestCase):

    @patch('algolia_etl.load.create_engine')
    @patch('algolia_etl.load.os.getenv')
    def test_load(self, mock_getenv, mock_create_engine):
        # Mock environment variable and database engine
        mock_getenv.return_value = 'mock_db_uri'
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        # Test data
        test_data = {
            'id': [1, 2],
            'application_id': ['app1', 'app2'],
            'index_prefix': ['shopify_', 'custom_'],
            'has_specific_prefix': [False, True]
        }
        test_df = pd.DataFrame(test_data)

        # Check the function
        load(test_df, 'test_table')

        # Check the db uri
        mock_getenv.assert_called_once_with('ALGOLIA_DB_URI')
        mock_create_engine.assert_called_once_with('mock_db_uri')
        
        # Check if begin() was called on the engine
        mock_engine.begin.assert_called_once()
        
        # Check if execute was called twice (once for each row)
        context_manager = mock_engine.begin.return_value.__enter__.return_value
        self.assertEqual(context_manager.execute.call_count, 2)

        # Check if the SQL query contains the correct table name and ON CONFLICT clause
        call_args = context_manager.execute.call_args_list[0]
        sql_query = str(call_args[0][0])
        self.assertIn('test_table', sql_query)
        self.assertIn('ON CONFLICT (id) DO NOTHING', sql_query)
        self.assertIn('VALUES', sql_query)

if __name__ == '__main__':
    unittest.main()