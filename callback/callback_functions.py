# MANAGE ENVIRONNEMENT
from preprocess.preprocess_data import dict_of_df
import plotly.express as px
from dash import dcc


def bike_traffic(counter: str) -> dcc.Graph:
    """bicycle (curved graph) traffic plot"""

    df_dict = dict_of_df()
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

    df_dict = dict_of_df()
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
