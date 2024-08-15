from dash_extensions import DeferScript
from dash_extensions.enrich import DashProxy, html, dcc, Input, Output, callback, ctx, no_update, State
from src import data, config, utils
from src.components.DriverDetails import DetailSection, make_details_driver, make_details_circuit
from src.components.GeneralInfo import GeneralInfo, make_sub_left_container

# Stylesheets hosted externally and loaded in the header
external_stylesheets = [
    {"src": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css"},
    {"src": "https://cdn.jsdelivr.net/gh/lipis/flag-icons@7.2.3/css/flag-icons.min.css"},
]
app = DashProxy(
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True,
)
server = app.server

# Load custom HTML template
with open(config.path_index, "r") as f:
    app.index_string = f.read()

# Layout of the application
app.layout = html.Div(
    className="h-screen p-8",
    children=[
        # Title
        html.H1(
            className="mb-4 text-center text-xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl mb-6",
            children="Formula 1 results summary",
        ),
        html.Div(
            className="grid grid-cols-2 gap-2",
            children=[
                # Left container containing general information
                html.Div(
                    children=[
                        GeneralInfo("year_slider", "year_input", "left_graph_container"),
                    ],
                    id="left_container",
                ),
                # Right container containing driver and circuit details
                html.Div(
                    children=[
                        DetailSection(
                            data.get_data_query_file("list_drivers_year", year_chosen=config.default_year),
                            data.get_data_query_file("list_circuits_year", year_chosen=config.default_year),
                            "list_drivers",
                            "list_circuits",
                            "container_details",
                        )
                    ],
                    id="right_container",
                ),
            ],
        ),
        # JS scripts to be loaded and deferred
        html.Div(
            children=[
                DeferScript(src="https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js"),
                DeferScript(src="https://cdn.tailwindcss.com"),
            ]
        ),
    ],
)

# Callbacks
# These are the functions triggered by user input and actions


@callback(
    Output("left_graph_container", "children"),
    Output("right_container", "children"),
    Input("year_slider", "value"),
)
def update_year(year):
    year = utils.convert_int_safe(year)
    if year > config.seasons[1] or year < config.seasons[0]:
        return no_update, no_update
    return (
        # Update general information left container
        make_sub_left_container(year),
        # Update the right columns (especially the dropdowns)
        DetailSection(
            data.get_data_query_file("list_drivers_year", year_chosen=year),
            data.get_data_query_file("list_circuits_year", year_chosen=year),
            "list_drivers",
            "list_circuits",
            "container_details",
        ),
    )


@callback(
    Output("container_details", "children"),
    Output("list_drivers", "value"),
    Output("list_circuits", "value"),
    Input("list_drivers", "value"),
    Input("list_circuits", "value"),
    State("year_input", "value"),
)
def update_detail(driver_value, circuit_value, year_value):
    if year_value is None or (driver_value is None and circuit_value is None):
        return no_update
    # Depending on whether the driver or the circuit dropdown is triggered
    # we plot the appropriate graph
    if ctx.triggered_id == "list_drivers":
        return make_details_driver(driver_value, year_value), driver_value, ""
    else:
        return make_details_circuit(circuit_value, year_value), "", circuit_value


if __name__ == "__main__":
    app.run(debug=True)
