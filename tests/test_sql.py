import unittest
from app.sql_generator import generate_sql

class TestSQLGeneration(unittest.TestCase):
    def test_generate_sql(self):
        query = generate_sql("pickup_location='Manhattan'")
        self.assertEqual(query, "SELECT * FROM nyc_taxi_data WHERE condition='pickup_location='Manhattan';")

if __name__ == "__main__":
    unittest.main()
