
# MANAGE ENVIRONNEMENT
import dash_bootstrap_components as dbc
from dash import html, dcc


def graphic1(counters: list) -> tuple:
    """First graphic of the dashoard"""
    return dbc.Col([

            dbc.Col([

                # First graphic -----------------------
                html.P("Select an eco-counter :",
                       className="p-graphic")

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
                          'padding-bottom': '1%'}), html.Div(id="output-counter",
                                                             children=[],
                                                             className="output-graphic-div")


def graphic2(counters: list) -> tuple:
    """Second graphic of the dashoard"""
    return dbc.Col([

            dbc.Col([

                # Second graphic -----------------------
                html.P("Sélectionner un éco-compteur :",
                       className="p-graphic")
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
                      'padding-bottom': '1%'}), html.Div(id="output-week",
                                                         style={'margin-bottom': 0},
                                                         className="output-graphic-div")
