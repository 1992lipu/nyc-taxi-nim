import unittest
from app.sql_generator import generate_sql

class TestSQLGeneration(unittest.TestCase):
    def setUp(self):
        self.schema = """vendor_id,pickup_datetime,dropoff_datetime,passenger_count,trip_distance,pickup_longitude,pickup_latitude,rate_code,store_and_fwd_flag,dropoff_longitude,dropoff_latitude,payment_type,fare_amount,surcharge,tip_amount,tolls_amount,total_amount"""

    def test_generate_sql_simple_select(self):
        query = generate_sql("show all trips from Manhattan", self.schema)
        self.assertIn("SELECT", query.upper())
        self.assertIn("NYC_TAXI_DATA", query.upper())

    def test_generate_sql_with_conditions(self):
        query = generate_sql("trips with fare amount greater than 50", self.schema)
        self.assertIn("FARE_AMOUNT", query.upper())
        self.assertIn(">", query)
        self.assertIn("50", query)

    def test_generate_sql_with_aggregation(self):
        query = generate_sql("average fare amount by passenger count", self.schema)
        self.assertIn("AVG", query.upper())
        self.assertIn("GROUP BY", query.upper())

if __name__ == "__main__":
    unittest.main()
