#  MANAGEMENT ENVIRONMENT
from callback.callback_functions import (bike_traffic,
                                         traffic_week,
                                         pie_graph,
                                         map_traffic_bike)
from dash import dcc
import unittest


# TESTS
class TestCallbackFunctions(unittest.TestCase):

    def setUp(self):
        # variable configuration
        self.counter = 'X2H20063162'
        self.counters_list = ['X2H20063162',
                              'X2H19070220',
                              'X2H20042632',
                              'X2H20042634']
        self.invalid_type_counter = 1
        self.invalid_list_counters = [1, 2, 3, 4]

    def test_callback_functions(self):

        # Call the function to be tested
        result_f1 = bike_traffic(counter=self.counter)
        result_f2 = traffic_week(counter=self.counter)
        result_f3 = pie_graph(counters=self.counters_list)
        result_f4 = map_traffic_bike(counters=self.counters_list)

        # Check output type
        assert isinstance(result_f1, dcc.Graph)
        assert isinstance(result_f2, dcc.Graph)
        assert isinstance(result_f3, dict)
        assert isinstance(result_f4, dcc.Graph)

        # Checks if a function generates an AttributeError
        with self.assertRaises(KeyError):
            bike_traffic(counter=self.invalid_type_counter)
            traffic_week(counter=self.invalid_type_counter)
            pie_graph(counters=self.invalid_list_counters)
            map_traffic_bike(counters=self.invalid_list_counters)


if __name__ == '__main__':
    unittest.main()
