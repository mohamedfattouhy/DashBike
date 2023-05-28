# MANAGE ENVIRONNEMENT
import dash_bootstrap_components as dbc
from dash import html, dcc


def graphic1(counters: list) -> tuple:
    """First graphic of the dashoard"""
    return dbc.Col([

            dbc.Col([

              # First graphic -----------------------
              html.Span("Select an eco-counter ",
                        className="p-graphic"),
              html.Span(className="bi bi-list",
                        style={'font-size': '18px',
                               'color': 'black'})

              #   html.P("Select an eco-counter :",
              #          className="p-graphic")

                        ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12,
                    style={'padding-left': '10px',
                           'padding-right': '10px'}
                    ),

            dbc.Col([

                html.Div(
                    dcc.Dropdown(id='input-counter', clearable=False,
                                    value="X2H20063162",
                                    options=counters,
                                    className="dropdown-graphic"),
                    style={'backgroundColor': "#81C784",
                           'margin-top': 0}
                        ),
                    ],
                    xs=10, sm=10, md=4, lg=3, xl=2, xxl=2,
                    style={'padding-left': '10px',
                           'padding-right': '10px'}
                    )],
                   style={'backgroundColor': "#81C784",
                          'padding-bottom': '1%'}
                   ), html.Div(id="output-counter",
                               children=[],
                               className="output-graphic-div")


def graphic2(counters: list) -> tuple:
    """Second graphic of the dashoard"""
    return dbc.Col([

            dbc.Col([

                # Second graphic -----------------------
                html.Span("Select an eco-counter ",
                          className="p-graphic"),
                html.Span(className="bi bi-list",
                          style={'font-size': '18px',
                                 'color': 'black'})

                ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12,
                    style={'padding-left': '10px',
                           'padding-right': '10px'}),

            dbc.Col([

                html.Div(
                    dcc.Dropdown(id='input-week', clearable=False,
                                    value="X2H20063162",
                                    options=counters,
                                    className="dropdown-graphic"),
                    style={'backgroundColor': "#81C784",
                           'margin-top': 0}
                    ),
                ], xs=10, sm=10, md=4, lg=3, xl=2, xxl=2,
                    style={'padding-left': '10px',
                           'padding-right': '10px'}
                    ),
            ], style={'backgroundColor': "#81C784",
                      'padding-bottom': '1%'}
            ), html.Div(id="output-week",
                        style={'margin-bottom': 0},
                        className="output-graphic-div")


def graphic3():
    """Third graphic of the dashoard"""
    return html.Div(id="input-pie"), html.Div([dcc.Graph(id="output-pie")],
                                              className="output-graphic-div")


def graphic4():
    """Fourth graphic of the dashoard"""
    return html.Div("(Some of) Montpellier's eco-counters",
                    id="input-map",
                    className="style-title-graphic3"
                    ), html.Div(className="style-div-map",
                                id="output-map")
