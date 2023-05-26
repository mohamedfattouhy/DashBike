# MANAGE ENVIRONNEMENT
from preprocess.preprocess_data import dict_of_df
import plotly.express as px
from dash import dcc


def bike_traffic(counter: str) -> dcc.Graph:
    """bicycle traffic plot"""

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
    df['text'] = 'Date: ' + df['Date'] + \
        '<br>Number of passages: ' + \
        (round(df["intensity"], 0)).astype(int).astype(str)

    fig.update_layout(margin={"r": 0, "t": 25, "l": 0,
                      "b": 0})
    fig.update_layout(template='seaborn',
                      font=dict(color='black', size=9,
                      family='Times New Roman')
                      )

    fig.update_traces(hovertemplate=df["text"])

    return dcc.Graph(figure=fig)
