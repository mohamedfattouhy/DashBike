# MANAGE ENVIRONNEMENT
from callback.callback_functions import bike_traffic, traffic_week
import dash_bootstrap_components as dbc
from src.build.dashbike import layout
from dash import Dash, Input, Output
import webbrowser as wb


app = Dash(__name__,  title='Dashbike',
           external_stylesheets=[dbc.themes.SUPERHERO,
                                 dbc.icons.BOOTSTRAP,
                                 dbc.icons.FONT_AWESOME,
                                 'assets/style.css'],
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width,\
                        initial-scale=1.0, maximum-scale=2,\
                        minimum-scale=1'}]
           )

# application layout
app.layout = dbc.Container(children=layout(), fluid=True)


# callback to make the graphic interactive
@app.callback(Output(component_id="output-counter",
                     component_property="children"),
              [Input(component_id="input-counter",
                     component_property="value")]
              )
def update_trafic_velos(counter):
    return bike_traffic(counter)


@app.callback(Output(component_id="output-week",
                     component_property="children"),
              [Input(component_id="input-week",
                     component_property="value")]
              )
def update_traffic_week(counter):
    return traffic_week(counter)


# run the app locally
if __name__ == '__main__':
    wb.open_new("http://127.0.0.1:8050/")
    app.run_server(debug=False)
