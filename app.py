"""
This file contains the code to create and run the
"""

# MANAGE ENVIRONNEMENT
import os
import webbrowser as wb
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output
from flask_caching import Cache
from callback.callback_functions import (
       bike_traffic,
       traffic_week,
       pie_graph,
       map_traffic_bike)
import src.build.dashbike as sbd
from src.build.dashbike import layout
from src.preprocess.import_data import create_folder, load_json_files
from src.preprocess.formatting_data import format_json_files


# create 'data' folder if it does not already exist
create_folder(dirpath_name='data', subdir_names=["raw", "preprocess"])

# loads json files
load_json_files()

# formatting json files
dir_json_path = os.path.join("data", "raw")
dir_save_json = os.path.join("data", "preprocess")
format_json_files(dir_json_path, dir_save_json)


# Create the app
app = Dash(__name__,  title='Dashbike',
           external_stylesheets=[dbc.themes.SUPERHERO,
                                 dbc.icons.BOOTSTRAP,
                                 'assets/style.css'],
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width,\
                        initial-scale=1.0, maximum-scale=2,\
                        minimum-scale=1'}]
           )

# Initialize cache with simple caching strategy
cache = Cache(app.server, config={'CACHE_TYPE': 'simple'})

# application layout
app.layout = dbc.Container(children=layout(), fluid=True)


# callback to make the graphic interactive
@app.callback(Output(component_id="output-counter",
                     component_property="children"),
              [Input(component_id="input-counter",
                     component_property="value")]
              )
@cache.memoize()  # Decorator to cache function results
def update_traffic_bike(counter):
    """Update bike traffic curve graph"""
    return bike_traffic(counter)


@app.callback(Output(component_id="output-week",
                     component_property="children"),
              [Input(component_id="input-week",
                     component_property="value")]
              )
@cache.memoize()
def update_traffic_week(counter):
    """Update of the bar chart on the
    rate of bike passages per week"""
    return traffic_week(counter)


@app.callback(Output(component_id="output-pie",
                     component_property="figure"),
              [Input(component_id="input-pie",
                     component_property="children")]
              )
def update_pie_graph(children=None):
    """Circular chart of the number of bike"""
    return pie_graph(counters=sbd.counters)


@app.callback(Output(component_id="output-map",
                     component_property="children"),
              [Input(component_id="input-map",
                     component_property="children")]
              )
def update_map_traffic_bike(children=None):
    """Map to visualize the number of bike"""
    return map_traffic_bike(counters=sbd.counters)


# run the app locally
if __name__ == '__main__':
#     wb.open_new("http://127.0.0.1:8050/")
    app.run_server(debug=False)
