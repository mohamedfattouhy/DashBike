#  MANAGEMENT ENVIRONMENT
from src.build.dashbike import layout
from src.build.graphics import (graphic1,
                                graphic2,
                                graphic3,
                                graphic4)
from dash import html
import dash_bootstrap_components as dbc
import unittest


# TESTS
class TestBuildFunctions(unittest.TestCase):

    def setUp(self):
        # variable configuration
        self.counters_list = ['X2H20063162',
                              'X2H19070220',
                              'X2H20042632',
                              'X2H20042634']
        self.invalid_list_counters = [1, 2, 3, 4]

    def test_build_functions(self):

        # Call the function to be tested
        result_layout = layout()
        # Check output type
        assert isinstance(result_layout, html.Div)

        result_g1 = graphic1(counters=self.counters_list)
        result_g2 = graphic2(counters=self.counters_list)
        result_g3 = graphic3()
        result_g4 = graphic4()

        assert isinstance(result_g1[0], dbc.Col)
        assert isinstance(result_g1[1], html.Div)

        assert isinstance(result_g2[0], dbc.Col)
        assert isinstance(result_g2[1], html.Div)

        assert isinstance(result_g3[0], html.Div)
        assert isinstance(result_g3[1], html.Div)

        assert isinstance(result_g4[0], html.Div)
        assert isinstance(result_g4[1], html.Div)


if __name__ == '__main__':
    unittest.main()
