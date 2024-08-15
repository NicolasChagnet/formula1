from dash_extensions.enrich import html, dcc, no_update
from dash import get_asset_url
from src import config, data
import plotly.graph_objects as go
import pandas as pd


def DetailSection(driver_list, circuit_list, id_list_driver, id_list_circuits, id_container):
    """Main component for the details section including the two dropdowns and the graph container"""
    return html.Div(
        className="flex flex-col",
        children=[
            html.Div(
                className="grid grid-cols-2 gap-x-2",
                children=[
                    DriversDropdown(driver_list, id_list_driver),
                    CircuitsDropdown(circuit_list, id_list_circuits),
                ],
            ),
            html.Div(id=id_container, className="mt-4", children=[]),
        ],
    )


def DriversDropdown(driver_list, id_list):
    """Dropdown to select a driver in a given year"""
    return dcc.Dropdown(
        id=id_list,
        placeholder="Select driver...",
        options=[
            {
                "label": html.Span(
                    className="flex flex-row gap-2 items-center",
                    children=[
                        html.Img(
                            className="w-4",
                            src=get_asset_url(f"flags/1x1/{config.nationality_map[driver_row['driver_country']]}.svg"),
                        ),
                        driver_row["driver_fullname"],
                    ],
                ),
                "value": driver_row["driverId"],
                "search": driver_row["driver_fullname"],
            }
            for _, driver_row in driver_list.sort_values(by="driver_surname").iterrows()
        ],
    )


def CircuitsDropdown(circuit_list, id_list):
    """Dropdown to select a circuit in a given year"""
    return dcc.Dropdown(
        id=id_list,
        placeholder="Select circuit...",
        options=[
            {
                "label": html.Span(
                    className="flex flex-row gap-2 items-center",
                    children=[
                        html.Img(
                            className="w-4",
                            src=get_asset_url(f"flags/1x1/{config.country_map[circuit_row['circuit_country']]}.svg"),
                        ),
                        html.Span(
                            children=[
                                html.Span(
                                    className="",
                                    children=circuit_row["circuit_city"] + " " + circuit_row["circuit_country"],
                                ),
                                html.Span(className="text-gray-400", children=f" ({circuit_row['race_date']})"),
                            ]
                        ),
                    ],
                ),
                "value": circuit_row["circuit_id"],
                "search": circuit_row["name"]
                + " "
                + circuit_row["circuit_city"]
                + " "
                + circuit_row["circuit_country"],
            }
            for _, circuit_row in circuit_list.sort_values(by="race_date").iterrows()
        ],
    )


def make_graph_details(data, axis_name, year_value):
    # Make the bar chart
    fig_details = go.Figure(
        go.Bar(
            x=data["position"],
            y=data["label"],
            name="Race position",
            orientation="h",
        ),
    )
    fig_details.add_trace(
        go.Bar(
            x=data["grid"],
            y=data["label"],
            name="Grid position",
            orientation="h",
        )
    )
    # Add vertical line for podium positions
    line_colors = {"gold": "#fcb434", "silver": "#c7d1da", "bronze": "#88540b"}
    fig_details.add_vline(x=1, line_width=3, opacity=0.75, line_color=line_colors["gold"])
    fig_details.add_vline(x=2, line_width=3, opacity=0.75, line_color=line_colors["silver"])
    fig_details.add_vline(x=3, line_width=3, opacity=0.75, line_color=line_colors["bronze"])
    # Add medals which go with the podium annotations
    fig_details.add_annotation(
        dict(
            font=dict(color="black", size=16),
            # x=x_loc,
            x=1,
            y=1.06,
            showarrow=False,
            text=chr(0x1F947),
            textangle=0,
            xref="x",
            yref="paper",
        )
    )
    fig_details.add_annotation(
        dict(
            font=dict(color="black", size=16),
            # x=x_loc,
            x=2,
            y=1.06,
            showarrow=False,
            text=chr(0x1F948),
            textangle=0,
            xref="x",
            yref="paper",
        )
    )
    fig_details.add_annotation(
        dict(
            font=dict(color="black", size=16),
            # x=x_loc,
            x=3,
            y=1.06,
            showarrow=False,
            text=chr(0x1F949),
            textangle=0,
            xref="x",
            yref="paper",
        )
    )
    # Graph title
    fig_details.add_annotation(
        text=f"Results for {axis_name} in {year_value}",
        xref="paper",
        yref="paper",
        x=0.5,
        y=1.05,
        showarrow=False,
        font=dict(size=14),
    )
    # Style the figure
    fig_details.update_layout(
        barmode="group",
        xaxis={"range": [0, 22]},
        yaxis={
            "showticklabels": True,
            "type": "category",
        },
        height=550,
        margin=dict(l=0, r=0, b=0, t=25, pad=4),
        legend=dict(orientation="v", yanchor="top", y=0.99, xanchor="right", x=0.99),
    )
    return dcc.Graph(id="graph-details", figure=fig_details, config={"displayModeBar": False})


def make_details_driver(driver_value, year_value):
    # Load the data about the driver and the circuits of that year
    data_driver = data.get_data_query_file("driver_detail", id=driver_value, year_chosen=year_value)
    data_circuits = data.get_data_query_file("list_circuits_year", year_chosen=year_value).set_index("name")
    # The driver data only has data for the races the driver participated in
    # Add the other circuits with position 0
    missing_circuits = pd.DataFrame(
        [
            {
                "circuit_name": circuit,
                "position": 0,
                "grid": 0,
                "race_date": data_circuits.loc[circuit, "race_date"],
                "circuit_city": data_circuits.loc[circuit, "circuit_city"],
                "circuit_country": data_circuits.loc[circuit, "circuit_country"],
            }
            for circuit in list(set(data_circuits.index.to_list()) - set(data_driver["circuit_name"].values))
        ]
    )
    data_driver_concat = pd.concat([data_driver, missing_circuits])
    # Sort from first to last race
    data_driver_concat = data_driver_concat.sort_values("race_date", ascending=False)
    data_driver_concat["label"] = data_driver_concat.apply(
        lambda row: row["circuit_city"] + ", " + row["circuit_country"], axis=1
    )
    return make_graph_details(data_driver_concat, data_driver.iloc[0]["driver_fullname"], year_value)


def make_details_circuit(circuit_value, year_value):
    # Load the data about the driver and the circuits of that year
    data_drivers = data.get_data_query_file(
        "drivers_at_circuit_year", circuit_id=circuit_value, year_chosen=year_value
    )
    if data_drivers.empty:
        return no_update
    data_drivers["label_circuit"] = data_drivers.apply(
        lambda row: row["circuit_city"] + ", " + row["circuit_country"], axis=1
    )
    data_drivers["position"] = pd.to_numeric(data_drivers["position"], errors="coerce")
    data_drivers["position"] = data_drivers["position"].fillna(999)
    data_drivers = data_drivers.sort_values(by="position", ascending=False)
    data_drivers.loc[data_drivers["position"] == 999, "position"] = 0
    data_drivers["label"] = data_drivers["driver_fullname"]
    # Make the bar chart
    return make_graph_details(data_drivers, data_drivers.iloc[0]["label_circuit"], year_value)
