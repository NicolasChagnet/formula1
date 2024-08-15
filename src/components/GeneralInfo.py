from dash_extensions.enrich import html, dcc, Output, callback, Input, ctx
from src.components.YearSelector import YearSelector
from src import config, data
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


def GeneralInfo(id_slider, id_input, id_left_container):
    """General information component containing a slider and a container"""
    return html.Div(
        children=[
            YearSelector(id_slider=id_slider, id_input=id_input),
            html.Div(
                id=id_left_container,
                className="mt-4",
                children=make_sub_left_container(config.default_year),
            ),
        ]
    )


def make_sub_left_container(year):
    """Generates the graph and visuals on the left container"""
    return [
        dcc.Graph(id="most-wins", figure=make_graph_races(year), config={"displayModeBar": False}),
    ]


def make_graph_races(year):
    # Query the data
    data_races_year = data.get_data_query_file("data_races_year", year_chosen=year)
    # Filter the data to only include race winners
    data_most_wins = data_races_year.loc[data_races_year["nb_race_wins"] > 0]
    data_most_wins = data_most_wins.sort_values(by="team_name")
    # Filter the data to only include qualification winners
    data_most_quals = data_races_year.loc[data_races_year["nb_qual_wins"] > 0]
    data_most_quals = data_most_quals.sort_values(by="team_name")
    # All teams in both plots
    all_teams = list(set(data_most_wins["team_name"]).union(set(data_most_quals["team_name"])))
    all_colors_dict = {team: px.colors.qualitative.Plotly[i] for i, team in enumerate(all_teams)}
    data_most_wins["color"] = data_most_wins["team_name"].apply(lambda team: all_colors_dict[team])
    data_most_quals["color"] = data_most_quals["team_name"].apply(lambda team: all_colors_dict[team])
    # Subplots
    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=["Top race winners", "Top qualifiers"],
        specs=[[{"type": "domain"}, {"type": "domain"}]],
    )
    fig_1 = fig.add_trace(
        go.Pie(
            labels=data_most_quals["driver_fullname"],
            values=data_most_quals["nb_qual_wins"],
            marker=dict(colors=data_most_quals["color"]),
            name="Quali. poles",
            showlegend=False,
        ),
        row=1,
        col=1,
    )
    fig_2 = fig.add_trace(
        go.Pie(
            labels=data_most_wins["driver_fullname"],
            values=data_most_wins["nb_race_wins"],
            name="Race poles",
            marker=dict(colors=data_most_wins["color"]),
            showlegend=False,
        ),
        row=1,
        col=2,
    )
    fig.update_layout(
        title_text=f"Results for the {data_most_wins['nb_race_wins'].sum()} races in {year}",
        showlegend=False,
        legend=dict(orientation="h", yanchor="top", y=-0.01, xanchor="center", x=0.5),
    )
    fig.update_traces(
        textposition="inside",
        textinfo="value+label",
        textfont_size=20,
        hoverinfo="label+percent+name",
        hole=0.3,
        marker=dict(line=dict(color="#000000", width=2)),
    )
    return fig


# Callback to sync the slider and input value
@callback(
    Output("year_input", "value"),
    Output("year_slider", "value"),
    Input("year_input", "value"),
    Input("year_slider", "value"),
)
def sync_year_input(input_value, slider_value):
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "year_input" else slider_value
    return value, value
