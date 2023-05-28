# MANAGE ENVIRONNEMENT
from dash import html
from .graphics import graphic1, graphic2, graphic3
import dash_bootstrap_components as dbc

counters = ['X2H20063162', 'X2H19070220', 'X2H20042632', 'X2H20042634']

# IMPORT GRAPHICS
col_graphic1, div_graphic1 = graphic1(counters=counters)
col_graphic2, div_graphic2 = graphic2(counters=counters)
col_graphic3, div_graphic3 = graphic3()


def layout() -> html.Div:
    """layout of the app"""

    return html.Div([

        # Header -----------------------
        # dbc.Col([html.Div("Dash Bike", className='title'
        #                   )
        #          ]),

        dbc.Col([

            html.Div([

                html.Span("Dash Bike", className="title me-2"),
                html.Span(className="bi bi-bicycle",
                          style={'font-size': '40px',
                                 'color': 'rgb(46, 172, 207)'})
            ])

            ], width=12, className="d-flex justify-content-center"),

        dbc.Col([

            # Title -----------------------
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

            # First graphic -----------------------
            col_graphic1, div_graphic1,

            html.Div(html.Hr(className="hr-style-thinner"),
                     style={'padding-bottom': '3%'}),

            # Second graphic -----------------------
            col_graphic2, div_graphic2,

            html.Div(html.Hr(className="hr-style-thinner"),
                     style={'padding-bottom': '3%'}),

            # # Third graphic ------------------------
            col_graphic3, div_graphic3

            ], className="background-graphic")

        ], width=12, className="style-col"),

    ], style={'margin-top': '20px', 'padding-bottom': '1%'})
