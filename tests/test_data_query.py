import unittest
import pandas as pd
from app.data_query import query_data

class TestDataQuery(unittest.TestCase):
    def test_query_basic_select(self):
        query = "SELECT * FROM nyc_taxi_data LIMIT 1"
        result = query_data(query)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 1)

    def test_query_aggregation(self):
        query = "SELECT COUNT(*) as count FROM nyc_taxi_data"
        result = query_data(query)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result['count'].iloc[0] > 0)

    def test_query_with_condition(self):
        query = "SELECT * FROM nyc_taxi_data WHERE trip_duration > 0 LIMIT 1"
        result = query_data(query)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result['trip_duration'].iloc[0] > 0)

if __name__ == "__main__":
    unittest.main()