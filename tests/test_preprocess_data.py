#  MANAGEMENT ENVIRONMENT
from src.preprocess.preprocess_data import preprocess_json_files, dict_of_df
import os
import pandas as pd
import unittest


# TESTS
class TestPreprocessData(unittest.TestCase):

    def setUp(self):
        # variable configuration
        self.json_file = os.path.join("data", "preprocess", "X2H19070220.json")
        self.invalid_type_counter = 1

    def test_preprocess_json_files(self):

        # Checks whether the function output is a dataframe
        result = preprocess_json_files(path_to_json_file=self.json_file)
        self.assertIsInstance(result, pd.DataFrame)

        #  Expected columns
        expected_columns = ['intensity', 'id', 'Date', 'week', 'lon', 'lat']

        result = preprocess_json_files(path_to_json_file=self.json_file)

        # Check columns
        result_columns = result.columns.tolist()
        self.assertListEqual(result_columns, expected_columns)

    def test_dict_of_df(self):

        # Checks whether the function output is a dict
        result = dict_of_df()
        self.assertIsInstance(result, dict)

        # Checks if a function generates an AttributeError
        with self.assertRaises(TypeError):
            dict_of_df(counters=self.invalid_type_counter)


if __name__ == '__main__':
    unittest.main()
