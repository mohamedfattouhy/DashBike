# MANAGE ENVIRONNEMENT
import dash_bootstrap_components as dbc
from dash import html, dcc

counters = ['X2H20063162', 'X2H19070220', 'X2H20042632', 'X2H20042634']


def layout() -> html.Div:
    """layout of the app"""

    return html.Div([

        dbc.Col([html.Div("Dash Bike", className='title'
                          )
                 ]),

        dbc.Col([

            html.Div("Bicycle traffic in Montpellier",
                     className="header-text"),

            html.Div(html.A("(Data: https://data.montpellier3m.fr)",
                            href="https://data.montpellier3m.fr/dataset/comptages-velo-et-pieton-issus-des-compteurs-de-velo",
                            className="text-decoration-none",
                            target="_blank",
                            style={'color': '#1A237E'}
                            ),
                     className="data-link"
                     ),

            html.Div([

            html.Div(html.Hr(className="hr-style"),
                     style={'padding-bottom': '4%'}
                     ),

            dbc.Col([

                dbc.Col([

                    # First graphic -----------------------
                    html.P("Select an eco-counter :",
                           className="p-graphic1")

                         ], xs=12, sm=12, md=12, lg=12, xl=12, xxl=12,
                        style={'padding-left': '10px',
                               'padding-right': '10px'}
                        ),

                dbc.Col([

                    html.Div(
                        dcc.Dropdown(id='input-counter', clearable=False,
                                        value="X2H20063162",
                                        options=counters,
                                        className="dropdown-graphic1"),
                        style={'backgroundColor': "#81C784",
                               'margin-top': 0
                               }
                            ),
                        ],
                        xs=10, sm=10, md=4, lg=3, xl=2, xxl=2,
                        style={'padding-left': '10px',
                               'padding-right': '10px'}
                        ),


                        ], style={'backgroundColor': "#81C784",
                                  'padding-bottom': '1%'}
                    ),

            html.Div(id="output-counter", children=[],
                     className="output-counter-div"),

            # html.Div(html.Hr(className="hr-style-thinner"),
            #          style={'padding-bottom': '3%'}),

                ], className="background-graphic")
        ], width=12, className="style-col")

        ], style={'margin-top': '40px', 'padding-bottom': '1%'})
