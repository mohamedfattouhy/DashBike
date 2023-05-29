"""
This module contains the functions that produce the dashboard graphics.
"""

# MANAGE ENVIRONNEMENT
from src.preprocess.preprocess_data import dict_of_df
import plotly.graph_objs as go
import plotly.express as px
from dash import dcc
import pandas as pd

# import the dictionary containing the data frames
df_dict = dict_of_df()


def bike_traffic(counter: str) -> dcc.Graph:
    """bicycle (curved graph) traffic plot"""

    df = df_dict[counter]

    title = '<sub>(Eco-counter: ' + str(df["id"].unique()[0]) + ')</sub>'

    # Draw graph from dataframe
    fig = px.line(df, x="Date", y="intensity",
                  title=title, markers=True)

    fig.update_layout(title_x=0.5, yaxis_title="Number of bicycle passages",
                      xaxis=dict(tickangle=45, nticks=10,
                                 griddash="dash"),
                      title_font=dict(size=15))

    fig.update_layout(plot_bgcolor="#FFD54F", paper_bgcolor="#FFD54F")
    fig.update_traces(marker_color='red', line_color='#8E44AD', xaxis="x1",
                      hoverlabel=dict(bgcolor="#FFD54F"))

    # Column containing text
    df['text_hover'] = 'Date: ' + df['Date'] + \
        '<br>Number of passages: ' + \
        (round(df["intensity"], 0)).astype(int).astype(str)

    fig.update_layout(margin={"r": 0, "t": 25, "l": 0,
                      "b": 0})
    fig.update_layout(template='seaborn',
                      font=dict(color='black', size=9,
                      family='Times New Roman')
                      )

    fig.update_traces(hovertemplate=df["text_hover"])

    return dcc.Graph(figure=fig)


def traffic_week(counter: str) -> dcc.Graph:
    """plot (bar graphic) the passage per day"""

    df = df_dict[counter]

    df = df[["intensity", "id", "week"]].groupby(
        ['id', 'week']).sum(["intensity"]).reset_index()

    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Sunday", "Saturday"]

    df["week_int"] = df['week'].map(
        dict(zip(days, range(len(days)))))
    df = df.sort_values(by='week_int')

    df['pct'] = df["intensity"]/df["intensity"].sum()

    # Text column
    df['text_hover'] = 'Day of the week: ' + df['week'] + \
        '<br>Passage rate: ' + \
        (round(df["pct"], 2)*100).astype(int).astype(str) + '%'

    # Text column
    df['text_over_bar'] = (round(df["pct"]*100, 2)).astype(int)\
                                                   .astype(str) + '%'

    title = 'Average passage rate per week' + '<br>' +\
            '<sub>(Eco-counter: ' + str(df["id"].unique()[0]) + ')</sub>'

    fig = px.bar(df, x='week', y='pct', title=title, text='text_over_bar')

    fig.update_layout(yaxis_tickformat=".0%")

    fig.update_layout(title_x=0.5, xaxis_title="Day of the week", yaxis={
                      'title': {'text': None}}, title_font=dict(size=15))
    fig.update_traces(hovertemplate=df["text_hover"])

    fig.update_layout(margin={"r": 0, "t": 55, "l": 0})
    fig.update_traces(hovertemplate=df["text_hover"], hoverlabel=dict(
        bgcolor="#F1948A"), marker_color='#B03A2E')
    fig.update_layout(plot_bgcolor="#F1948A", paper_bgcolor="#F1948A")

    return dcc.Graph(figure=fig)


def pie_graph(counters: list) -> dcc.Graph:
    """pie chart to visualize the number of bicycles on the road"""

    dff = pd.DataFrame()

    # Loop through the counters
    for counter in iter(counters):

        df = df_dict[counter]

        # Retrieve the last line of the DataFrame
        last_row = df.iloc[-1]

        # Add last line to the df_trafic
        dff = pd.concat([dff, pd.DataFrame([last_row])],
                        ignore_index=True)

    # Text column
    dff['text_hover'] = 'Date: ' + dff['Date'] + \
        '<br>Total number of passages: ' + \
        (round(dff["intensity"], 0)).astype(int).astype(str)

    title = 'Distribution of bike passages' + \
            '<br>' +\
            '<sub>' + '(Date: ' + dff['Date'].iloc[0] + ')'\
            + '</sub>'

    colors = ['orange', '#dd1e35', 'green', '#e55467']

    graph_pie_bike = {

        'data': [go.Pie(
                        labels=['X2H20063162', 'X2H19070220',
                                'X2H20042632', 'X2H20042634'],
                        # values=[intensity for intensity in dff["intensity"]],
                        values=dff["intensity"].tolist(),
                        marker=dict(colors=colors,
                                    line=dict(color='#000000',
                                              width=0.8)),
                        textinfo='percent',
                        textposition="inside",
                        hovertemplate=dff["text_hover"],
                        textfont=dict(size=10),
                        hole=.65,
                        rotation=45,
                        name=""
                        )
                 ],

        'layout': go.Layout(
                        plot_bgcolor='#1A237E',
                        paper_bgcolor='#1A237E',
                        hovermode='closest',
                        title={
                            'text': title,
                            'y': 0.95,
                            'x': 0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'
                            },
                        uniformtext_minsize=12,
                        uniformtext_mode='hide',
                        titlefont={'color': '#B71C1C',
                                   'size': 18},
                        legend={'orientation': 'h',
                                'bgcolor': '#1A237E',
                                'xanchor': 'center', 'x': 0.5, 'y': -0.07
                                },
                        font=dict(
                            family="sans-serif",
                            size=12,
                            color='white')
                        )
        }

    return graph_pie_bike


def map_traffic_bike(counters: list) -> dcc.Graph:
    """map to visualize the number of bicycles on the road"""

    df_trafic = pd.DataFrame()

    # Loop through the counters
    for counter in iter(counters):

        df = df_dict[counter]

        # Retrieve the last line of the DataFrame
        last_row = df.iloc[-1]

        # Add last line to the df_trafic
        # df_trafic = df_trafic.append(last_row, ignore_index=True)
        df_trafic = pd.concat([df_trafic, pd.DataFrame([last_row])],
                              ignore_index=True)

    df_trafic["size"] = df_trafic["intensity"].apply(
        lambda x: x if x >= 100 else 100)

    fig = px.scatter_mapbox(
        df_trafic,
        lon='lon',
        lat='lat',
        size="size",
        size_max=35,
        zoom=11,
        center=dict(lat=df_trafic['lat'].mean(),
                    lon=df_trafic['lon'].mean()),
    )

    # Text column
    df_trafic['text_hover'] = 'Eco-counter identifier: '\
        + df_trafic["id"] + \
        '<br>Date: ' + df_trafic['Date'] + \
        '<br>Total number of passages: ' + \
        (round(df_trafic["intensity"], 0)).astype(int).astype(str)

    fig.update_layout(mapbox_style="open-street-map",
                      plot_bgcolor="#81C784", paper_bgcolor="#81C784",
                      title_font=dict(size=18))

    fig.update_layout(margin={"r": 0, "t": 5, "l": 0,
                      "b": 0})

    fig.update_layout(template='seaborn',
                      font=dict(color='black',
                                size=9, family='Times New Roman'))

    fig.update_traces(hovertemplate=df_trafic["text_hover"], hoverlabel=dict(
        bgcolor="#EC7063"),  marker=dict(color='#E74C3C'))

    return dcc.Graph(figure=fig)
